import networkx as nx
from gurobipy import *
def solve(n, E, s, t):
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(n)])
    G.add_weighted_edges_from(E)

    #path = nx.dijkstra_path(G, source=s, target=t)
    shortestpathlength = nx.dijkstra_path_length(G, s, t)
    print(shortestpathlength)
