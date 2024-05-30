from gurobipy import *
import TSPParser


def solve():
    n, nodes = TSPParser.parse("berlin52.tsp")
    model = Model('TSP-Model')


solve()

