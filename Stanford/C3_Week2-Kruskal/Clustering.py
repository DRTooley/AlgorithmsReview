# In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a
# max-spacing k-clustering.
#
# Download the text file below.
# clustering1.txt
#
# This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:
#
# [number_of_nodes]
#
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
#
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
#
# ...
#
# There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of nodes.
#
# For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3
# (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT
# assume that they are distinct.
#
# Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number
# k of clusters is set to 4. What is the maximum spacing of a 4-clustering?
#
# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then
# post them to the discussion forum!

import heapq
import gc

class Edge:
    def __init__(self, cost, head_node, tail_node):
        self.cost = int(cost)
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
        self.identifier = int(identifier)
        self.visited = False
        self.greedy_score = 1000000
        self.leader = self

    def AddEdge(self, edge):
        self.edges.add(edge)

    def GetLeader(self):
        if self.leader != self:
            # Update leader if not looking at the correct node
            self.leader = self.leader.GetLeader()
        return self.leader

    def UpdateLeader(self, new_lead):
        if self.leader != self:
            self.leader.UpdateLeader(new_lead)
        self.leader = new_lead

    def __lt__(self, other):
        return self.greedy_score < other.greedy_score

    def __gt__(self, other):
        return not self.__lt__(other)





def ReadInFile(file_name):
    my_heap = []
    nodes = dict()
    with open(file_name, 'r') as cluster_file:
        number_of_nodes = cluster_file.readline()
        number_of_nodes =int(number_of_nodes)
        for line in cluster_file:
            l_split = line.split()
            if int(l_split[0]) not in nodes:
                nodes[int(l_split[0])] = Node(int(l_split[0]))
            if int(l_split[1]) not in nodes:
                nodes[int(l_split[1])] = Node(int(l_split[1]))

            edge = Edge(int(l_split[2]), nodes[int(l_split[0])], nodes[int(l_split[1])])
            nodes[int(l_split[0])].AddEdge(edge)
            nodes[int(l_split[1])].AddEdge(edge)
            heapq.heappush(my_heap, edge)
    if number_of_nodes == len(nodes):
        print('Not a Problem!')
    return my_heap, number_of_nodes


def clustering1():
    my_heap, clusters = ReadInFile('clustering1.txt')
    # number of clusters to find max distance
    k = 4
    while my_heap:
        edge = heapq.heappop(my_heap)
        head_lead = edge.head_node.GetLeader()
        tail_lead = edge.tail_node.GetLeader()
        if head_lead.identifier != tail_lead.identifier:
            #if head_lead.identifier == edge.head_node.identifier:
            #    print("Head:  Self Lead")
            #else:
            #    print("Head: Other Lead")
            #if tail_lead.identifier == edge.tail_node.identifier:
            #    print("Tail:  Self Lead")
            #else:
            #    print("Tail: Other Lead")
            clusters -= 1
            #print('{} != {}'.format(edge.head_node.leader.identifier, edge.tail_node.leader.identifier))
            edge.head_node.UpdateLeader(edge.tail_node.GetLeader())
            #print('{} == {}, {}'.format(edge.head_node.GetLeader(), edge.tail_node.GetLeader(), edge.head_node.GetLeader() == edge.tail_node.GetLeader()))
            #print("Clusters: {}".format(clusters))
            print('Edge Cost: {}'.format(edge.cost))
            if clusters == k-1:
                max_edge_space = edge
                print("Max Spacing: {}".format(max_edge_space.cost))
                break
        else:
            pass#print('{} == {}'.format(edge.head_node.leader.identifier, edge.tail_node.leader.identifier))


HammingMemory = dict()
def HammingWeight(c):
    if c not in HammingMemory:
        c0 = (c >> 0) & int('01010101010101010101010101010101', 2)
        c1 = (c >> 1) & int('01010101010101010101010101010101', 2)
        d = c0 + c1
        d0 = (d >> 0) & int('00110011001100110011001100110011', 2)
        d1 = (d >> 2) & int('00110011001100110011001100110011', 2)
        e = d0 + d1
        e0 = (e >> 0) & int('00001111000011110000111100001111', 2)
        e1 = (e >> 4) & int('00001111000011110000111100001111', 2)
        f = e0 + e1
        f0 = (f >> 0) & int('00000000111111110000000011111111', 2)
        f1 = (f >> 8) & int('00000000111111110000000011111111', 2)
        g = f0 + f1
        g0 = (g >> 0) & int('00000000000000001111111111111111', 2)
        g1 = (g >> 16) & int('00000000000000001111111111111111', 2)

        HammingMemory[c] = g0 + g1

    return HammingMemory[c]


def HammingDistance(a, b):
    c = a ^ b
    return HammingWeight(c)


def ReadInClusteringBig(file_name):
    bits = []
    with open(file_name, 'r') as clust_big:
        nn = clust_big.readline()
        nn = nn.split()
        number_of_nodes = int(nn[0])
        number_of_bits = int(nn[1])
        for line in clust_big.readlines():
            line = ''.join(line.split())
            bits.append(int(line, 2))

    return bits

def GetK(location):
    unique = []
    for node in range(len(location)):
        matched  = False
        for cluster in unique:
            if location[node] is cluster:
                matched = True
                break
        if not matched:
            unique.append(location[node])

    return len(unique)


def ClusteringBig():
    bits = ReadInClusteringBig('clustering_big.txt')
    print(len(bits))
    print("Sorting...")
    bits.sort()
    location = dict()
    for i in range(len(bits)):
        connecting_sets = list()
        for j in range(i-1, -1, -1):
            if HammingDistance(bits[i], bits[j]) <= 2:
                connecting_sets.append(location[j])

        if not connecting_sets:
            location[i] = set([i])
        else:
            base_set = connecting_sets.pop()
            base_set.add(i)
            location[i] = base_set
            for other_set in connecting_sets:
                if other_set is not base_set:
                    base_set = base_set.union(other_set)
                    for val in other_set:
                        location[val] = base_set




        if i % 10000 == 0:
            print('i: {}'.format(i))
            gc.collect()
            k_val = GetK(location)
            print('Max K value: {}'.format(k_val))
            print()

    k_val = GetK(location)
    print('Final Max K value: {}'.format(k_val))

if __name__ == '__main__':
    #clustering1()
    ClusteringBig()




