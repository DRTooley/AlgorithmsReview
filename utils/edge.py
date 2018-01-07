class Edge:
    def __init__(self, cost, head_node, tail_node):
        self.cost = float(cost)
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
        return int('123456789{}123456789{}'.format(self.head_node.identifier, self.tail_node.identifier))


