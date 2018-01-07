# The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
# Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge.
# For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The
# next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length
# 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the
# corresponding edges.

# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex,
# and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a
# vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

# You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,
# 197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these
# vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be
# 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should
# be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type
# your answer in the space provided.

# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's
# algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the
# heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind
# of mapping between vertices and their positions in the heap.

import heapq

from utils.node import Node
from utils.edge import Edge




def ReadInGraph(file_name):
    nodes = dict()
    with open(file_name, 'r') as undirected_graph:
        for node_line in undirected_graph:
            node_line = node_line.split()
            starting_node_id = int(node_line.pop(0))
            if starting_node_id not in nodes:
                nodes[starting_node_id] = Node(starting_node_id)
            for connected_node in node_line:
                t = connected_node.split(',')
                node_id, length = int(t[0]), int(t[1])
                if node_id not in nodes:
                    nodes[node_id] = Node(node_id)

                e = Edge(length, nodes[starting_node_id], nodes[node_id])
                nodes[starting_node_id].AddEdge(e)
                nodes[node_id].AddEdge(e)

    return nodes

def ExploreNode(node, potential_nodes):
    if not node.visited:
        node.visited = True
        for e in node.edges:
            if e.head_node is not node:
                new_node = e.head_node
            else:
                new_node = e.tail_node
            if new_node.greedy_score > node.greedy_score + e.cost:
                new_node.greedy_score = node.greedy_score + e.cost

            heapq.heappush(potential_nodes, new_node)




#O(m*n) implementation
# O(m*log(n)) is optimal. I am tired
def Dijkstra(node):
    potential_nodes = list()
    node.greedy_score = 0
    ExploreNode(node, potential_nodes)

    while potential_nodes:
        next_node = heapq.heappop(potential_nodes)
        ExploreNode(next_node, potential_nodes)




if __name__ == '__main__':
    nodes = ReadInGraph('dijkstraData.txt')
    Dijkstra(nodes[1])
    required_vals = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    print("Shortest Path from 1 to ${node}")
    for num in required_vals:
        print('{},'.format(nodes[num].greedy_score), end='')
        #print('{}: {}'.format(num, nodes[num].greedy_score))