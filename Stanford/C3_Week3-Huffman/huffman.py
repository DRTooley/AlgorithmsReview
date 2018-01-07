# In this programming problem and the next you'll code up the greedy algorithm
# from the lectures on Huffman coding.

# Download the text file below.
# huffman.txt

# This file describes an instance of the problem. It has the following format:
# [number_of_symbols]
# [weight of symbol #1]
# [weight of symbol #2]
# ...

# For example, the third line of the file is "6852892," indicating that the
# weight of the second symbol of the alphabet is 6852892. (We're using weights
# instead of frequencies, like in the "A More Complex Example" video.)

# Your task in this problem is to run the Huffman coding algorithm from lecture
# on this data set. What is the maximum length of a codeword in the resulting
# Huffman code?

# ADVICE: If you're not getting the correct answer, try debugging your
# algorithm using some small test cases. And then post them to the discussion
# forum!

import heapq

class Node:
    def __init__(self, symbol=None, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right


    def GetWeight(self, find_min=False):
        if self.symbol is not None:
            return self.symbol.weight, 0

        left_weight = 0
        if self.left is not None:
            left_weight, l_depth = self.left.GetWeight(find_min)

        right_weight = 0
        if self.right is not None:
            right_weight, r_depth = self.right.GetWeight(find_min)

        if find_min:
            ret_depth = min(r_depth+1, l_depth+1)
        else:
            ret_depth = max(r_depth+1, l_depth+1)

        return (left_weight+right_weight), ret_depth

    def __lt__(self, other):
        sw, _ = self.GetWeight()
        ow, _ = other.GetWeight()
        return sw < ow


class Symbol:
    def __init__(self, num, weight):
        self.identifier = num
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight


if __name__ == '__main__':
    nodes = []

    with open('huffman.txt', 'r') as huff_weights:
        symbol_count = huff_weights.readline()

        for i, symbol_weight in enumerate(huff_weights):
            s = Symbol(i, int(symbol_weight))
            n = Node(symbol=s)
            nodes.append(n)

    heapq.heapify(nodes)

    while len(nodes) >= 2:
        min1 = heapq.heappop(nodes)
        min2 = heapq.heappop(nodes)
        n = Node(left=min1, right=min2)
        heapq.heappush(nodes, n)

    root_node = heapq.heappop(nodes)

    _, max_depth = root_node.GetWeight()
    _, min_depth = root_node.GetWeight(True)

    print("Max Depth: {}".format(max_depth))
    print("Min Depth: {}".format(min_depth))

