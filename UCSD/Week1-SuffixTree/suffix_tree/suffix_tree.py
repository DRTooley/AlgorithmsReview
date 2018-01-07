# python3
import sys

class Edge:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

class Node:
    def __init__(self, value, edges=None):
        self.value = value
        if edges is None:
            self.edges = set()
        else:
            self.edges = edges

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    root = Node(0)
    end = Node(len(text)-1)
    e = Edge(root, end)

    for i in range(1, len(text), 1):
        n = root
        current_index = i
        while n:
            for e in n.edges:
                if text[current_index] == text[n.value]


    result = []
    # Implement this function yourself
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))