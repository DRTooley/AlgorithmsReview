# In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic
# programming algorithm covered in the video lectures. Here is a data file describing a TSP instance.
# tsp.txt
#
# The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates
# the x- and y-coordinates of a single city.
#
# The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and
# (z,w) have distance (x−z)2+(y−w)2 between them.
#
# In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest
# integer.
#
# OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here. The
# smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. What's the
# largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely
# different method?
#
# HINT: You might experiment with ways to reduce the data set size. For example, trying plotting the points. Can you
# infer any structure of the optimal solution? Can you use that structure to speed up your algorithm?

import os
import itertools
from utils.euclidean_distance import EuclideanDistance
from utils.node import Node
from utils.edge import Edge

class EuclideanNode(Node):
    def __init__(self, identifier, x, y):
        super(EuclideanNode, self).__init__(identifier)
        self.x = x
        self.y = y


def solve_tsp_dynamic(points):
    #calc all lengths
    all_distances = [[EuclideanDistance(x,y) for y in points] for x in points]
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]


def solve_tsp_dynamic_2(points):
    #calc all lengths
    all_distances = [[EuclideanDistance(x,y) for y in points] for x in points]
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                A[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[0]

def ReadTSPFile(filename):
    nodes = []
    with open(filename, 'r') as tsp:
        city_count  = tsp.readline()
        for i, line in enumerate(tsp):
            line = line.split()
            x, y = float(line[0]), float(line[1])
            nodes.append(EuclideanNode(i, x, y))

    for i, node in enumerate(nodes[:-1]):
        for other_node in nodes[i+1:]:
            dist = EuclideanDistance(node, other_node)
            e = Edge(dist, node, other_node)
            node.AddEdge(e)
            other_node.AddEdge(e)

    return nodes


def solve_tsp_self(nodes):
    # 2-D array indexed by [Set of visited vertices, S][destination vertex, j]
    tsp_values = [[float("inf") for __ in range(len(nodes))] for _ in range(len(nodes))]

    # The distance to the initial node when s is empty is zero
    for i in range(len(nodes)):
        # EuclideanDistance(nodes[0], nodes[i])
        tsp_values[i][0] = EuclideanDistance(nodes[0], nodes[i])
        if tsp_values[i][0] == 0:
            tsp_values[i][0] = float('inf')

    # iterate over the cardinality of the set S (all nodes excluding the starting point)
    for n, node in enumerate(nodes[1:]):
        n = n + 1
        # for every vertex in the set of visited vertices
        for s in range(len(nodes)):

            # for every destination of visited vertices that are in the set S, excluding the starting vertex
            # destination = j
            for destination in range(len(nodes)):
                for k in range(len(nodes)):
                    if k != destination:
                        k_to_j = tsp_values[k][s-1] + EuclideanDistance(nodes[k], nodes[destination])
                        tsp_values[destination][s] = \
                            min(
                                tsp_values[destination][s],
                                k_to_j
                            )


    potential_values = [tsp_values[-1][e.tail_node.identifier] + e.cost for e in nodes[0].edges]

    print("Min TSP: {0:.02f}".format(min(potential_values)))



if __name__ == '__main__':
    nodes = ReadTSPFile('tsp_test.txt')

    val = solve_tsp_dynamic(nodes)
    print("Min TSP: {}".format(val))
