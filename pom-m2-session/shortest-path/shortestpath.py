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

    # each edge is apart of shortest path or not
    edge_count = len(E)
    vars = model.addVars(edge_count, vtype=GRB.BINARY)
    # path costs should be minimized (shortest path)
    model.setObjective(quicksum(vars[i] * E[i][2] for i in range(edge_count)), GRB.MINIMIZE)

    # constraints:
    for i in range(n):
        sum_selected_succ = 0
        sum_selected_pred = 0
        for edge in edge_tuples.select(i, '*'):
            sum_selected_succ += vars[E.index(edge)]

        for edge in edge_tuples.select('*', i):
            sum_selected_pred += vars[E.index(edge)]

        # selected_succ = quicksum(vars[E.index(edge)] for edge in edge_tuples.select(i, '*'))
        # selected_pred = quicksum(vars[E.index(edge)] for edge in edge_tuples.select('*', i))

        val = sum_selected_succ - sum_selected_pred
        # if i == s:
            # current node is the source node and should not have predecessors
            # model.addConstr(sum_selected_succ - sum_selected_pred == 1)


