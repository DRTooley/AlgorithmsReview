#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    unused_state = 1
    for pattern in patterns:
        current_state = 0
        for letter in pattern:
            if current_state not in tree:
                tree[current_state] = {letter:unused_state}
                current_state = unused_state
                unused_state += 1
            elif letter in tree[current_state]:
                current_state = tree[current_state][letter]
            else:
                tree[current_state][letter] = unused_state
                current_state = unused_state
                unused_state += 1



    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
