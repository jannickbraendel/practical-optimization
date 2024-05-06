from gurobipy import *


def solve(m, a, b):
    model = Model('Makespan-Scheduling')
    model.params.LogToConsole = True
    # amount of jobs
    n = len(a)
    # job j is assigned to machine k
    x = model.addVars(n, m, vtype=GRB.BINARY)
    # Makespan: Duration until every job is performed
    cMax = model.addVar(0, vtype=GRB.CONTINUOUS)

    # obj: minimize makespan
    model.setObjective(cMax, GRB.MINIMIZE)

    # constraint: perform every job i
    for j in range(n):
        model.addConstr(quicksum(x[j, k] for k in range(m)) == 1)

    # constraint: total durations determine makespan
    for k in range(m):
        model.addConstr(quicksum(a[j] * x[j, k] for j in range(n)) <= cMax)

    # experiment constraint (accelerated process):
    model.addConstr(cMax <= 70)

    model.optimize()