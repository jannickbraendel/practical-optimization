from gurobipy import *
import jssLibrary


def solve_disjunctive():

    n, m, operations = jssLibrary.parseStandard("abz5.txt")
    print(n, m, operations)

solve_disjunctive()