import sys
import re


# parse standard jss instance (return number of machines m, number of jobs n,
# tuplelist of operations: [(job, duration, machine)]
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
            for opIndex in range(m):
                duration = int(lines[jobIndex + 1].split()[opIndex])
                # subtract 1 as machine counting starts with 0
                machine = int(lines[jobIndex + 1 + n].split()[opIndex]) - 1
                operations.append((jobIndex, duration, machine))
        return n, m, operations
