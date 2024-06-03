import sys
import re


# parse standard jss instance (return number of machines m, number of jobs n,
# list of lists of operations: [[(duration, machine)]]
def parseTaillard(fileName):
    with open(fileName, "r") as file:
        n = 0
        m = 0
        operations = []

        lines = file.readlines()

        # get number of machines and jobs
        firstLine = lines[0].split()
        n = int(firstLine[0])
        m = int(firstLine[1])

        for jobIndex in range(n):
            job_operations = []
            for opIndex in range(m):
                duration = int(lines[jobIndex + 1].split()[opIndex])
                # subtract 1 as machine counting starts with 0
                machine = int(lines[jobIndex + 1 + n].split()[opIndex]) - 1
                job_operations.append((duration, machine))
                print(job_operations)
            operations.append(job_operations)
        return n, m, operations
