import gurobipy as gurobi

GRB = gurobi.GRB

MODEL_NAME = "multipacking"
"""
I = #items
B = #bins
R = #resources
"""


def solve_gurobi(I, B, R, required, available, copies):
    model = gurobi.Model(f"{MODEL_NAME}_gurobi")

    n = I
    m = B

    ### variables ###

    x = model.addVars(n, m, name="x", vtype=GRB.BINARY)  # pack item i into bin j
    s = model.addVars(m, name="s", vtype=GRB.CONTINUOUS, lb=0)  # surplus load in bin j

    ### constraints ###

    # place every item i according to copies[i]
    # TODO: what happens if we change this == to >= ?
    model.addConstrs((gurobi.quicksum(x[i, j] for j in range(m)) == copies[i] for i in range(n)), "assingment")

    # capacity of bin j in dimension r
    for r in range(R):
        model.addConstrs(
            (gurobi.quicksum(required[i][r] * x[i, j] for i in range(n)) <= available[j][r] for j in range(m)),
            "capacity")

    # meaure surplus load in bin j
    copies_mean = sum(copies) / m
    model.addConstrs((gurobi.quicksum(x[i, j] for i in range(n)) <= copies_mean + s[j] for j in range(m)), "surplus")

    ### optimize ###
    model.setObjective(gurobi.quicksum(s), gurobi.GRB.MINIMIZE)
    model.optimize()


solve = solve_gurobi