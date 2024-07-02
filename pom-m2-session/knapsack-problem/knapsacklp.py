from gurobipy import *


# item sizes a, profits p, capacity b
def solve(a, p, b):

    model = Model('knapsack-longestpath')
    model.params.LogToConsole = True
    # amount of items
    n = len(a)

    # BUILD GRAPH
    nodes = [(c, i) for c in range(b+1) for i in range(n+1)]
    # edges: list of tuples containing two nodes as tuples (c, i) and their edge weight p_i -> item archs, skip archs, waste archs
    item_archs = []
    # item archs
    for i in range(1, n+1):
        for c in range(b - a[i-1] + 1):
            item_archs.append(((c, i - 1), (c + a[i-1], i), p[i-1]))

    # skip archs
    skip_archs = [((c, i - 1), (c, i), 0) for i in range(1, n+1) for c in range(b+1)]
    # waste archs
    waste_archs = [((c, i), (c + 1, i), 0) for i in range(n) for c in range(b)]
    edges = item_archs + skip_archs + waste_archs
    edge_count = len(edges)
    # binary variable: true if edge is selected in path
    edge_selected = model.addVars(edge_count, vtype=GRB.BINARY)
    # objective: maximize path length (profit)
    model.setObjective(quicksum(edge_selected[i] * edges[i][2] for i in range(edge_count)), GRB.MAXIMIZE)

    # Flow constraint:
    s = (0, 0)
    t = (b, n)
    for node in nodes:
        # get edges leading to and from current node and their index (predecessors)
        pred_indices = [idx for idx, (u, v, _) in enumerate(edges) if v == node]
        succ_indices = [idx for idx, (u, v, _) in enumerate(edges) if u == node]
        # count how many are selected
        sum_selected_pred = quicksum(edge_selected[i] for i in pred_indices)
        sum_selected_succ = quicksum(edge_selected[i] for i in succ_indices)

        # current node is the source node
        if node == s:
            model.addConstr(sum_selected_succ - sum_selected_pred == 1)
        # current node is the target node
        elif node == t:
            model.addConstr(sum_selected_succ - sum_selected_pred == -1)
        else:
            # any other node
            model.addConstr(sum_selected_succ - sum_selected_pred == 0)

    model.optimize()

