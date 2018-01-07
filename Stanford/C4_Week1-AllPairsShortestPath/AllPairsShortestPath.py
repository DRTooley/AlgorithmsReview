from utils.node import Node
from utils.edge import Edge

from algos.bellman_ford import BellmanFord
import multiprocessing
import functools
import sys

def ReadGraph(filename):
    nodes = dict()
    with open(filename, 'r') as G:
        header = G.readline()
        header = header.split()
        vertex_count = int(header[0])
        edge_count = int(header[1])
        for line in G:
            line = line.split()
            tail = int(line[0])
            head = int(line[1])
            weight = int(line[2])
            if tail not in nodes:
                nodes[tail] = Node(tail)
            if head not in nodes:
                nodes[head] = Node(head)
            edge = Edge(weight, nodes[tail], nodes[head])
            nodes[tail].AddEdge(edge)
            nodes[head].AddEdge(edge)
    return nodes



if __name__ == '__main__':

    # print("Reading G1...")
    # g1 = ReadGraph('g1.txt')
    # print("Performing BellmanFord on G1...")
    # BellmanFord(g1, g1[1])
    #
    # print("Reading G2...")
    # g2 = ReadGraph('g2.txt')
    # print("Performing BellmanFord on G2...")
    # BellmanFord(g2, g2[1])

    print("Reading G3...")
    g3 = ReadGraph('g3.txt')
    print("Performing BellmanFord on G3...")

    my_ssp = float("inf")
    start = 751
    end = 1001
    
    for i in range(start, end, 1):
        nc, ssp  = BellmanFord(g3, i)
        my_ssp = min(ssp, my_ssp)
        print("Current Min: {}".format(my_ssp))

    print("The Shortest, Shortest Path is {}".format(my_ssp))
