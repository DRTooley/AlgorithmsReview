# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False


def build_trie(patterns):
    tree = dict()
    # write your code here
    unused_state = 1
    for pattern in patterns:
        current_state = 0
        for letter in pattern:
            if current_state not in tree:
                tree[current_state] = dict()

            if letter in tree[current_state]:
                current_state = tree[current_state][letter]
            else:
                tree[current_state][letter] = unused_state
                current_state = unused_state
                unused_state += 1
        if current_state not in tree:
            tree[current_state] = dict()
        tree[current_state]["$"] = ''


    return tree

def pat_match(text, pat_def):
    state = 0
    for t in text:

        if t in pat_def[state]:
            state = pat_def[state][t]
        elif "$" not in pat_def[state]:
            return False
        if "$" in pat_def[state]:
            return True

    return False

def solve (text, n, patterns):
    result = []
    pat_def = build_trie(patterns)

    for i in range(len(text)):
        if pat_match(text[i:], pat_def):
            result.append(i)

    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
