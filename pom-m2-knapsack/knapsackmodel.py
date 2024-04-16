#!/usr/bin/env python3

from gurobipy import *


# item sizes a, item profits p, capacity b
def solve(a, p, b):
    model = Model("knapsack")
    model.params.LogToConsole = True
    # a binary variable per item (selected or not); gives profit if selected
    n = len(a)
    vars = model.addVars(n, vtype=GRB.BINARY)
    model.setObjective(quicksum(p[i] * vars[i] for i in range(n)), GRB.MAXIMIZE)

    # capacity constraint
    model.addConstr(quicksum(a[i] * vars[i] for i in range(n)) <= b)

    # optimize
    model.optimize()
    items = []
    for i in range(n):
        if vars[i].X > 0.5:
            items.append(i)
        # print(vars[i].X)
    print(items)