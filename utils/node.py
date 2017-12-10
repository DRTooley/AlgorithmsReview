class Node:
    def __init__(self, identifier):
        self.identifier = int(identifier)
        self.edges = set()
        self.visited = False
        self.greedy_score = 1000000
        self.leader = self
        self.incoming_edges = self.GetIncomingEdges()

    def AddEdge(self, edge):
        self.edges.add(edge)
        self.incoming_edges = self.GetIncomingEdges()

    def GetIncomingEdges(self):
        rtn = set()

        for e in self.edges:
            if e.head_node == self:
                rtn.add(e)

        return rtn

    def GetOutgoingEdges(self):
        rtn = set()

        for e in self.edges:
            if e.tail_node == self:
                rtn.add(e)

        return rtn

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


    # def __eq__(self, other):
    #     return self.greedy_score == other.greedy_score and \
    #         self.identifier == other.identifier and \
    #         self.edges == other.edges