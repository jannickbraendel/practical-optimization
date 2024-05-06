from gurobipy import *


def aggregate(l, d):
    lengths = []
    demands = []

    # Create a dictionary to store aggregated demands
    aggregated_demands = {}

    # Iterate through the lengths and demands simultaneously
    for length, demand in zip(l, d):
        # If the length is already in the dictionary, add the demand to its value
        if length in aggregated_demands:
            aggregated_demands[length] += demand
        # If the length is not in the dictionary, create a new entry
        else:
            aggregated_demands[length] = demand

    # Create lists to store the aggregated lengths and demands
    aggregated_lengths = []
    aggregated_demands_list = []

    # Iterate through the aggregated dictionary and append values to the lists
    for length, demand in aggregated_demands.items():
        lengths.append(length)
        demands.append(demand)
    return lengths, demands


def solve(m, L, d, l):
    model = Model('cuttingstockmodel')
    model.params.LogToConsole = True

    l, d = aggregate(l, d)
    # amount of orders
    n = len(l)
    # how often order i is cut from roll j
    x = model.addVars(n, m, vtype=GRB.INTEGER, lb=0)
    # true if roll j is used
    y = model.addVars(m, vtype=GRB.BINARY)

    # minimize number of used rolls
    model.setObjective(quicksum(y[j] for j in range(m)), GRB.MINIMIZE)

    # every order has to be cut as often as the demand specifies
    for i in range(n):
        model.addConstr(quicksum(x[i, j] for j in range(m)) == d[i])
    # do not exceed rolls' length
    for j in range(m):
        model.addConstr(quicksum(l[i] * x[i, j] for i in range(n)) <= L)

    # constraint to link x and y vars
    model.addConstrs(x[i, j] <= d[i]*y[j] for i in range(n) for j in range(m))

    model.optimize()