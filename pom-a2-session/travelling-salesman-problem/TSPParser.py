import sys
import re


def parse(fileName):
    with open(fileName, "r") as file:
        nodes = []
        # iterate through file line by line
        for line in file:
            # get dimension of graph
            if line.find("DIMENSION") > -1:
                n = int(line.split(":")[1])
            # lines containing capital letters are not needed
            if re.match("[A-Z]", line) is not None:
                continue
            # line contains graph information
            coordValues = line.split(" ")
            if len(coordValues) == 3:
                nodes.append((float(coordValues[1]), float(coordValues[2])))

        return n, nodes
