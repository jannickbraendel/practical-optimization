from pyscipopt import Model, quicksum

def solve(a, p, b):
    model = Model('scip-knapsackmodel')
    n = len(a)
    vars = []
    for i in range(n):
        vars.append(model.addVar(vtype='B'))

    model.setObjective(quicksum(p[i] * vars[i] for i in range(n)), "maximize")

    model.addCons(quicksum(a[i] * vars[i] for i in range(n)) <= b)
    model.optimize()

    print("Optimal value is:", model.getObjVal())