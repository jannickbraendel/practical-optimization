import operator
from functools import reduce
from operator import iconcat

from gurobipy import *
from cuttingstockmodel import aggregate


def solve(m, L, d, l):
    model = Model("Cutting-Stock Flow Model")
    model.params.LogToConsole = True

    d, l = aggregate(d, l)

    n = len(l)
    # build graph
    A_1 = [[(k, k+l[i]) for k in range(L - l[i] + 1)] for i in range(n)]
    A_2 = [(k, k+1) for k in range(L)]
    # flatten A_1, combine with A_2 and add (s,v0) as (-1,0)
    A = reduce(iconcat, A_1, []) + A_2 + [(-1, 0)]
    # create tuple list from edges and their index in A (working)
    edge_tuples = tuplelist(map(lambda x: (x[1][0], x[1][1], x[0]), enumerate(A)))
    # add variable for first edge (amount of paths = amount of rolls used)
    start = model.addVar(vtype=GRB.INTEGER, lb=0)
    # variables for remaining edges
    x = model.addVars(len(A)-1, GRB.CONTINUOUS)
    # x01 is the last edge saved in A
    x[len(A)-1] = start
    # objective: minimize amount of rolls used (minimize x01)
    model.setObjective(start, GRB.MINIMIZE)

    # flow conservation constraint
    sum_edges = lambda v1, v2: quicksum(x[idx] for (_, _, idx) in edge_tuples.select(v1, v2))
    model.addConstrs((sum_edges(k, '*') - sum_edges('*', k) == 0 for k in range(L)), "flow_conservation")

    # constraint that order i is cut d_i amount of times
    # count how many arcs (are as long as l[i]) are part of A_1[i] and see if it is GE
    # than the demand d[i]
    model.addConstrs(
        (d[i] <= quicksum(x[edge_tuples.select(v1, v2)[0][2]] for (v1, v2) in A_1[i]) for i in range(n)), "demand")

    model.optimize()