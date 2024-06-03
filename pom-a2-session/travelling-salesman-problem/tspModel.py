from gurobipy import *
from tspLibrary import parse, plotTour, plotGraph
import networkx as nx


# Miller, Tucker, Zemlin Model
def solve_mtz():
    n, nodes, edge_tuples = parse("berlin52.tsp")
    # print(n, len(nodes))
    model = Model('tsp_mtz-model')
    model.params.LogToConsole = True
    # variables x_ij: 1 if edge i-j is used, 0 if not
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    # variables u_i >= 0 for position of node i in tour
    u = model.addVars(n, vtype=GRB.CONTINUOUS, lb=0, name="u")

    # objective: minimize distance
    model.setObjective(quicksum(x[i, j] * c for (i, j, c) in edge_tuples), GRB.MINIMIZE)

    # each node should have 1 successor and 1 predecessor only
    for k in range(n):
        model.addConstr(quicksum(x[i, j] for (i, j, _) in edge_tuples.select('*', k)) == 1)
        model.addConstr(quicksum(x[i, j] for (i, j, _) in edge_tuples.select(k, '*')) == 1)

    # tour start
    model.addConstr(u[0] == 1)

    # subtour elimination
    for (i, j, _) in edge_tuples:
        if j == 0:
            continue
        model.addConstr(u[i] - u[j] + n * x[i, j] <= n - 1)

    model.display()
    model.optimize()

    # get edges that are part of the tour with optimal length for plotting purpose
    selectedEdges = []
    for (i, j), var in x.items():
        if var.X > 0.9:
            selectedEdges.append((i, j))
    print(selectedEdges)
    plotTour(nodes, selectedEdges)


# Dantzig, Fulkerson, Johnson Model
def solve_dfj():
    n, nodes, edge_tuples = parse("pr144.tsp")
    edge_tuples = tuplelist(filter(lambda x: x[0] < x[1], edge_tuples))
    model = Model('tsp_dfj-model')
    model.params.LogToConsole = True
    # variables x_ij: 1 if edge i-j is used, 0 if not
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    model._x = x

    # objective: minimize distance
    model.setObjective(quicksum(x[i, j] * c for (i, j, c) in edge_tuples), GRB.MINIMIZE)

    # each node should have degree 2
    for k in range(n):
        sum_predecessors = quicksum(x[i, j] for (i, j, _) in edge_tuples.select('*', k))
        sum_successors = quicksum(x[i, j] for (i, j, _) in edge_tuples.select(k, '*'))
        model.addConstr(sum_successors + sum_predecessors == 2)

    # as graph is undirected: add symmetry to variables (x[i,j] = x[j,i])
    model.addConstrs(x[i, j] == x[j, i] for i in range(n) for j in range(n))

    def subtour_elim(callback_model, where):
        if where == GRB.Callback.MIPSOL:
            # get solution variables
            solution_x = model.cbGetSolution(callback_model._x)
            # construct support graph
            G = nx.Graph()
            for (i, j, _) in edge_tuples:
                weight = max(solution_x[i, j], 0)
                """if weight == 0:
                    continue"""
                G.add_edge(i, j, weight=weight)
            # plotGraph(G)

            cut_val, partition = nx.stoer_wagner(G)
            if cut_val < 1.99999:
                # found minimal cut with smaller cut value than 2 -> add constraint to eliminate that subtour
                # get successors from cut partition (that are not in the cut)
                outgoing_edges = [(i, j) for i in partition[0] for j in partition[1]]
                model.cbLazy(quicksum(callback_model._x[i, j] for i, j in outgoing_edges) >= 2)

    model.params.LazyConstraints = 1
    model.optimize(subtour_elim)

    # get edges that are part of the tour with optimal length for plotting purpose
    selectedEdges = []
    for (i, j), var in x.items():
        if var.X > 0.9:
            selectedEdges.append((i, j))
    # print(selectedEdges)
    plotTour(nodes, selectedEdges)


# solve_mtz()
solve_dfj()

