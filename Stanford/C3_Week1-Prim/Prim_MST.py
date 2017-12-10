# In this programming problem you'll code up Prim's minimum spanning tree algorithm.
#
# Download the text file below.
# edges.txt
#
# This file describes an undirected graph with integer edge costs. It has the format
#
# [number_of_nodes] [number_of_edges]
#
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
#
# [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
#
# ...
#
# For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and
# vertex #3 that has cost -8874.
#
# You should NOT assume that edge costs are positive, nor should you assume that they are distinct.
#
# Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a
# minimum spanning tree --- an integer, which may or may not be negative --- in the box below.
#
# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's
# algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based
# version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a
# heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in
# lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping
# between vertices and their positions in the heap.


import heapq

class Edge:
    def __init__(self, cost, head_node, tail_node):
        self.cost = cost
        self.head_node = head_node
        self.tail_node = tail_node

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return self.cost == other.cost and \
            self.head_node == other.head_node and \
            self.tail_node == other.tail_node

    def __hash__(self):
        return int('{}123456789{}123456789{}'.format(self.cost, self.head_node.identifier, self.tail_node.identifier))


class Node:
    def __init__(self, identifier):
        self.edges = set()
        self.identifier = identifier

    def AddEdge(self, edge):
        self.edges.add(edge)

def ReadInEdges(file_name):
    nodes = dict()
    with open(file_name, 'r') as edge_file:
        graph_defn = edge_file.readline()
        graph_defn = graph_defn.split()
        number_of_nodes = graph_defn[0]
        number_of_edges = graph_defn[1]

        for edge_defn in edge_file:
            edge_defn = edge_defn.split()

            head = int(edge_defn[0])
            if head not in nodes:
                nodes[head] = Node(head)

            tail = int(edge_defn[1])
            if tail not in nodes:
                nodes[tail] = Node(tail)

            cost = int(edge_defn[2])
            e = Edge(cost, nodes[head], nodes[tail])
            nodes[head].AddEdge(e)
            nodes[tail].AddEdge(e)

    return nodes

def AddEdges(node, edge_list):
    for e in node.edges:
        heapq.heappush(edge_list, e)

def CrossesCut(edge, found_nodes):
    return edge.head_node not in found_nodes or \
        edge.tail_node not in found_nodes


def Prim(nodes):
    begin_node = nodes[1]
    found_nodes = set([begin_node])
    available_edges = []
    AddEdges(begin_node, available_edges)
    total_cost = 0
    i = 0
    while available_edges:
        cheapest_edge = heapq.heappop(available_edges)
        if CrossesCut(cheapest_edge, found_nodes):
            if cheapest_edge.tail_node not in found_nodes:
                found_nodes.add(cheapest_edge.tail_node)
                AddEdges(cheapest_edge.tail_node, available_edges)
            else:
                found_nodes.add(cheapest_edge.head_node)
                AddEdges(cheapest_edge.head_node, available_edges)
            print(i)
            i += 1
            total_cost += cheapest_edge.cost

    print(total_cost)


if __name__ == '__main__':
    nodes = ReadInEdges('edges.txt')
    Prim(nodes)
