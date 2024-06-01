from gurobipy import *
from tspLibrary import parse, plotTour

# Müller, Tucker, Zemlin Model
def solve_mtz():
    n, nodes, edge_tuples = parse("berlin52.tsp")
    # print(n, len(nodes))
    model = Model('TSP-Model')
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

    # get edges that are part of the tour with optimal length to plot
    selectedEdges = []
    for (i, j), var in x.items():
        if var.X > 0.9:
            selectedEdges.append((i, j))
    print(selectedEdges)
    plotTour(nodes, selectedEdges)


solve_mtz()

