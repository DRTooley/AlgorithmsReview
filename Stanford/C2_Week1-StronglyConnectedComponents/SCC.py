# The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row
# indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head
# (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex).
# So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge
# to the vertex with label 47646

# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and
# to run this algorithm on the given graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
# separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500,
# 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds
# less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are
# 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer
# should not have any spaces in it.)

# WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may
# have to manage memory carefully. The best way to do this depends on your programming language and environment, and we
# strongly suggest that you exchange tips for doing this on the discussion forums.

import sys

def ParseGraphFile(document):
    g = Graph()
    with open(document, 'r') as graph_file:
        for line in graph_file:
            verts = line.split()
            tail_vert = int(verts[0])
            head_vert = int(verts[1])
            g.AddEdge(tail_vert, head_vert)

    return g



class Node:
    def __init__(self):
        #self.vert = vert
        self.outgoing_edges = set()
        self.incoming_edges = set()
        self.explored = False
        self.t = None

    def AddOutgoingEdge(self, vert_num):
        self.outgoing_edges.add(vert_num)

    def AddIncomingEdge(self, vert_num):
        self.incoming_edges.add(vert_num)

    def SetExplored(self, val=True):
        self.explored = val


class Graph(dict):
    def __init__(self, *args, **kwargs):
        super(dict, self).__init__(*args, **kwargs)
        self.t = 0
        self.time_stack = list()
        self.leader = None

    def AddEdge(self, tail_vert, head_vert):
        if tail_vert not in self:
            self[tail_vert] = Node()
        if head_vert not in self:
            self[head_vert] = Node()

        self[tail_vert].AddOutgoingEdge(head_vert)
        self[head_vert].AddIncomingEdge(tail_vert)


    def ProcessEdge(self, n, rev):
        edges = []

        if rev:
            edges.extend(self[n].incoming_edges)
        else:
            edges.extend(self[n].outgoing_edges)

        return edges


    def iterativeDFS(self, n, rev=False):
        if self[n].explored:
            return

        self[n].SetExplored()
        edges = self.ProcessEdge(n, rev)
        timeCount = dict()

        while edges:
            current = edges.pop()
            if not self[current].explored:
                self[current].SetExplored()
                if len(edges) not in timeCount:
                    timeCount[len(edges)] = [current]
                else:
                    timeCount[len(edges)].append(current)

                edges.extend(self.ProcessEdge(current, rev))
            # This vertex has been processed
            if len(edges) in timeCount:
                for finished_vert in reversed(timeCount[len(edges)]):
                    self[finished_vert].t = self.t
                    self.time_stack.append(finished_vert)
                    self.t += 1
                del timeCount[len(edges)]


        self[n].t = self.t
        self.time_stack.append(n)
        self.t += 1







def FindFinishingTimes(g):
    for vert in g:
        g.iterativeDFS(vert, True)

    [g[vert].SetExplored(False) for vert in g]
    return g

def FindLeaders(g):
    i = 0
    g.t = 0
    vals = []
    while g.time_stack:
        vert = g.time_stack.pop()
        g.iterativeDFS(vert)
        if g.t != 0:
            i += 1
            print("SSC {} Found. Size:  {} ".format(i, g.t))
            vals.append(g.t)
            g.t = 0

    print()
    print("The 5  largest values are:")
    s_v = list(reversed(sorted(vals)))
    for i in range(5):
        print(s_v[i])



def SizeOfSSCs(g):
    pass

if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    graph = ParseGraphFile('SCC.txt')
    FindFinishingTimes(graph)
    FindLeaders(graph)