# The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.

# The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your
# array of integers, with the ith row of the file specifying the ith entry of the array.

# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there
# are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line
# addition to the algorithm from lecture.)

# Write your numeric answer (an integer between 0 and 20001) in the space provided.

# OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example,
# you could compare performance under the chaining and open addressing approaches to resolving collisions.

import multiprocessing
import functools

def TargetExists(h, t):
    for key, value in h.items():
        needed = t - key
        if needed in h and (needed != key or value > 1):
            print("t exists: {}".format(t))
            return True
    return False

if __name__ == '__main__':
    h = dict()
    with open('2sum.txt', 'r') as sum_file:
        for line in sum_file:
            line = int(line)
            if line not in h:
                h[line] = 1
            else:
                h[line] += 1



    targets = 0

    tep = functools.partial(TargetExists, h)

    mp = multiprocessing.Pool(multiprocessing.cpu_count())

    valid_targets = mp.map(tep, range(-10000,10001, 1))


    for i in valid_targets:
        if i:
            targets += 1

    print(targets)