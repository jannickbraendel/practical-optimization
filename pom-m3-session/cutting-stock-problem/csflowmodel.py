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
    A_2 = [(i, i+1) for i in range(L)]
    # combine edge s0 -> v0, flattened A1 and A2
    A = [(-1, 0)] + reduce(iconcat, A_1, []) + A_2
    # create tuple list from edges and their index in A (working)
    edge_tuples = tuplelist([(edge[0], edge[1], A.index(edge)) for edge in A])
    # add variable for first edge (amount of paths = amount of rolls used)
    start = model.addVar(vtype=GRB.INTEGER, lb=0)
    # variables for remaining edges
    x = model.addVars(len(A)-1, GRB.CONTINUOUS)
    # x01 is the first edge and obtains value from x vars
    x[0] = start
    # objective: minimize amount of rolls used (minimize x01)
    model.setObjective(start, GRB.MINIMIZE)

    # constraint that order i is cut d_i amount of times
    # count how many arcs (are as long as l[i]) are part of A_1[i] and see if it is GE
    # than the demand d[i]
    model.addConstrs((quicksum(x[edge_tuples.select(v1, v2)[0][2]] for (v1, v2) in A_1[i]) >= d[i]) for i in range(n))

    # flow conservation constraint
    for k in range(L):
        sum_predecessors = quicksum(x[edge_tuples.index(predEdge)] for predEdge in edge_tuples.select('*', k))
        sum_successors = quicksum(x[edge_tuples.index(predEdge)] for predEdge in edge_tuples.select(k, '*'))

        model.addConstr(sum_predecessors - sum_successors == 0)

    model.optimize()