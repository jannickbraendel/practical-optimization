from gurobipy import *

def solve(m, L, d, l):
    model = Model('cuttingstockmodel')
    model.params.LogToConsole = True
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