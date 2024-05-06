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
    x = model.addVars(n, n, vtype=GRB.BINARY)
    # path costs should be minimized (shortest path)
    model.setObjective(quicksum(x[i, j] * c for (i, j, c) in edge_tuples), GRB.MINIMIZE)

    # constraints:
    for k in range(n):

        sum_selected_pred = quicksum(x[i, j] for (i, j, _) in edge_tuples.select('*', k))
        sum_selected_succ = quicksum(x[i, j] for (i, j, _) in edge_tuples.select(k, '*'))

        # current node is the source node
        if k == s:
            model.addConstr(sum_selected_succ - sum_selected_pred == 1)

        # current node is the target node
        elif k == t:
            model.addConstr(sum_selected_succ - sum_selected_pred == -1)

        else:
            # any other node
            model.addConstr(sum_selected_succ - sum_selected_pred == 0)

    # optimize
    model.optimize()
    '''
    nodes = []
    for i in range(n):
        if vars[i].X > 0.5:
            nodes.append(i)
        # print(vars[i].X)
    print(nodes)
    '''