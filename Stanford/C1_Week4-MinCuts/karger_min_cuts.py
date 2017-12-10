
# The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to
# 200. The first column in the file represents the vertex label, and the particular row (other entries except the first
# column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6 155 56 52
# 120 ......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with
# labels 155,56,52,120,......,etc

# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
# graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
# Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.
# But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make
# sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)
# Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.

import random
import copy
import multiprocessing

def karger(graph):
    random.seed()
    while len(graph) > 2:
        start_node, *_ = random.sample(graph.keys(), 1)
        end_node, *_ = random.sample(graph[start_node], 1)
        graph[end_node] = [e for e in sorted(graph[end_node]) if e != start_node]
        graph[start_node] = [e for e in sorted(graph[start_node]) if e != end_node]
        graph[start_node].extend(graph[end_node])
        if start_node in graph[start_node] or end_node in graph[start_node]:
            raise TypeError
        for node in graph:
            graph[node] = [e if e != end_node else start_node for e in sorted(graph[node])]

        del graph[end_node]

    for k in graph:
        print(len(graph[k]))
        return len(graph[k])

if __name__ == '__main__':
    graph = dict()
    with open('kargerMinCut.txt', 'r') as G:
        for line in G:
            node, *edges = line.split()
            if node in graph:
                raise NotImplementedError
            else:
                node = int(node)
                edges = [int(e) for e in edges]
            graph[node] = edges


    min_cuts = 1000 # 17
    my_runs = 10000

    if True:
        print("Making pool...")
        mp = multiprocessing.Pool(multiprocessing.cpu_count())
        print("Making copies...")
        g_copies = [copy.deepcopy(graph) for i in range(my_runs)]
        results = mp.map(karger, g_copies)
        for r in results:
            min_cuts = min(r, min_cuts)
    else:
        for i in range(my_runs):
            g_copy = copy.deepcopy(graph)
            min_cuts = min(karger(g_copy), min_cuts)

    print("Min Found: {}".format(min_cuts))








