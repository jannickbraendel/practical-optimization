from itertools import combinations

from gurobipy import *
import jssLibrary


def solve_disjunctive():
    # tuplelist of operations: [(job, duration, machine)]
    n, m, operations = jssLibrary.parseTaillard("abz5.txt")
    model = Model('jss-disjunctive')
    # makespan variable
    cMax = model.addVar(lb=0, vtype=GRB.CONTINUOUS)
    # starting time for each operation on job j (assuming there are m operations for each job)
    t = model.addVars(n, m, lb=0, vtype=GRB.CONTINUOUS)
    # binary variable: job i preceeds job j on machine k
    x_keys = [(k, i, j) for k in range(m) for (i, j) in combinations(range(n), 2)]
    x = model.addVars(x_keys, vtype=GRB.BINARY)

    # big number T for "big M" constraints
    T = 3000

    # objective: (here) minimize makespan duration
    model.setObjective(cMax, GRB.MINIMIZE)

    # CONSTRAINTS:

    for jobIndex in range(n):
        # operations of current job
        job_operations = [(j, duration, machine) for (j, duration, machine) in operations if j == jobIndex]
        # total duration determines makespan
        finalOperation = job_operations[-1]
        model.addConstr(t[jobIndex, len(job_operations) - 1] + finalOperation[1] <= cMax)
        # operation precedence constraint (operations of the same job should not overlap)
        for opIndex in range(len(job_operations) - 1):
            model.addConstr(t[jobIndex, opIndex] + job_operations[opIndex][1] <= t[jobIndex, opIndex+1])

    # machine constraints (operations should not overlap):
    for machineIndex in range(m):
        for (i, j) in combinations(range(n), 2):
            # job i preceeds job j on machine k
            # get operations from jobs i, j that run on machine k
            op_i = (0, 0, 0)
            op_j = (0, 0, 0)
            for (jobIndex, duration, machine) in operations:
                if machine != machineIndex:
                    continue
                if jobIndex == i:
                    op_i = (jobIndex, duration, machine)
                elif jobIndex == j:
                    op_j = (jobIndex, duration, machine)

            job_i_ops = [(job, duration, machine) for (job, duration, machine) in operations if job == i]
            job_j_ops = [(job, duration, machine) for (job, duration, machine) in operations if job == j]
            io = job_i_ops.index(op_i)
            jo = job_j_ops.index(op_j)
            # if i preceeds j on k the corresponding x var is set to 1, then T value is not used ( -> constraint is set)
            model.addConstr(t[i, io] + op_i[1] <=
                            t[j, jo] + T * (1 - x[machineIndex, i, j]))
            # print("Machine:", machineIndex, "i:", i, "io:", io, "j:", j, "jo:", jo)
            # if j preceeds i on k the opposite x var is set to 1, then T value is used ( -> constraint is set)
            model.addConstr(t[j, jo] + op_j[1] <=
                            t[j, io] + T * x[machineIndex, i, j])

    model.params.LogToConsole = True
    model.optimize()


solve_disjunctive()
