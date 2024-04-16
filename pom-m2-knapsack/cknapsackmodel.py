from gurobipy import *

def solve(a, p, b, C):
    model = Model('knapsackmodelConstraints')
    model.params.LogToConsole = True
    # a binary variable per item (selected or not); gives profit if selected
    n = len(a)
    vars = model.addVars(n, vtype=GRB.BINARY)

    # capacity constraint
    model.addConstr(quicksum(a[i] * vars[i] for i in range(n)) <= b)
    # conflict constraint
    for tuple in C:
        model.addConstr(vars[tuple[0]] + vars[tuple[1]] <= 1)
    # optimize
    model.setObjective(quicksum(p[i] * vars[i] for i in range(n)), GRB.MAXIMIZE)
    model.optimize()