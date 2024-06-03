import math
import sys
import re

import networkx as nx
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

        """for edge in edge_tuples:
            if edge[0] == 0:
                print(edge)"""

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


def plotGraph(G: nx.Graph):
    pos = nx.spring_layout(G)  # positions for all nodes

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=300, font_size=10)
    # Step 3: Get edge labels (weights) and draw them
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Display the graph
    plot.show()


