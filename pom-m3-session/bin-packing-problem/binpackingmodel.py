from gurobipy import *

# results: found out values 73 and 103 correctly (200s-150 and 400s-150) but for 200l-150 does not terminate (although it stands on wanted optimal value 96)

def solve(m, a, b):
    model = Model('Bin-Packing')
    model.params.LogToConsole = True

    n = len(a)
    # item i goes in bin j
    x = model.addVars(n, m, vtype=GRB.BINARY)
    # used bins
    y = model.addVars(m, vtype=GRB.BINARY)

    # objective: use minimal amount of bins
    model.setObjective(quicksum(y[j] for j in range(m)), GRB.MINIMIZE)

    # CONSTRAINTS:
    # every item has to be assigned
    for i in range(n):
        model.addConstr(quicksum(x[i, j] for j in range(m)) == 1)
    # v1 (variable linking): capacity of bin j
    for j in range(m):
        model.addConstr(quicksum(a[i] * x[i, j] for i in range(n)) <= b * y[j])

    # v3 (variable linking): capacity of bin j
    model.addConstrs(x[i, j] <= y[j] for i in range(n) for j in range(m))

    model.optimize()