import networkx as nx
from gurobipy import *


def solve(n, E, s, t):
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(n)])
    G.add_weighted_edges_from(E)

    #path = nx.dijkstra_path(G, source=s, target=t)
    shortestpathlength = nx.dijkstra_path_length(G, s, t)
    print(shortestpathlength)


def solveGurobi(n, E, s, t):
    model = Model('shortestpath')
    model.params.LogToConsole = True

    edge_tuples = tuplelist(E)

    # each edge is a part of shortest path or not
    edge_count = len(E)
    vars = model.addVars(edge_count, vtype=GRB.BINARY)
    # path costs should be minimized (shortest path)
    model.setObjective(quicksum(vars[i] * E[i][2] for i in range(edge_count)), GRB.MINIMIZE)

    # constraints:
    for i in range(n):

        sum_selected_succ = quicksum(vars[E.index(edge)] for edge in edge_tuples.select(i, '*'))
        sum_selected_pred = quicksum(vars[E.index(edge)] for edge in edge_tuples.select('*', i))

        print(sum_selected_succ, sum_selected_pred)

        # current node is the source node
        if i == s:
            model.addLConstr(sum_selected_succ - sum_selected_pred == 1)

        # current node is the target node
        if i == t:
            model.addConstr(sum_selected_succ - sum_selected_pred == -1)

        else:
            # any other node
            model.addConstr(sum_selected_succ - sum_selected_pred == 0)

    # optimize
    model.optimize()

    nodes = []
    for i in range(n):
        if vars[i].X > 0.5:
            nodes.append(i)
        # print(vars[i].X)
    print(nodes)
