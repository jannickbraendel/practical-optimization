import math
import sys
import re
from gurobipy import tuplelist
import matplotlib.pyplot as plot


def parse(fileName):
    with open(fileName, "r") as file:
        nodes = []
        edge_tuples = []
        # iterate through file line by line
        for line in file:
            # get dimension of graph
            if line.find("DIMENSION") > -1:
                n = int(line.split(":")[1])
            # lines containing capital letters are not needed
            if re.match("[A-Z]", line) is not None:
                continue
            # line contains graph information
            coordValues = line.split()
            if len(coordValues) == 3:
                nodes.append((float(coordValues[1]), float(coordValues[2])))

        # fill edge tuple list with all edges (except self-loops) and their distance
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i == j:
                    continue
                newEdge = (i, j, round(math.dist(nodes[i], nodes[j])))
                edge_tuples.append(newEdge)
        for edge in edge_tuples:
            if edge[0] == 0:
                print(edge)
        # print(edge_tuples)

        return n, nodes, tuplelist(edge_tuples)


def plotTour(points, edges):
    selectedPoints = []
    currentPointIndex = 0
    # fill selected points array in the order of the tour
    while len(edges) > 0:
        for edge in edges:
            if edge[0] == currentPointIndex:
                selectedPoints.append(points[currentPointIndex])
                currentPointIndex = edge[1]
                edges.remove(edge)

    print(selectedPoints)

    xPoints = [point[0] for point in selectedPoints]
    yPoints = [point[1] for point in selectedPoints]

    plot.plot(xPoints, yPoints, marker='o')

    plot.show()

