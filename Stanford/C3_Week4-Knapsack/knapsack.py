# In this programming problem and the next you'll code up the knapsack algorithm from lecture.
#
# Let's start with a warm-up. Download the text file below.
# knapsack1.txt
#
# This file describes a knapsack instance, and it has the following format:
#
# [knapsack_size][number_of_items]
#
# [value_1] [weight_1]
#
# [value_2] [weight_2]
#
# ...
#
# For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659,
# respectively.
#
# You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are
# integers.
#
# In the box below, type in the value of the optimal solution.
#
# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then
# post them to the discussion forum!
# 1
# point
# 2.
#
# This problem also asks you to solve a knapsack instance, but a much bigger one.
#
# Download the text file below.
# knapsack_big.txt
#
# This file describes a knapsack instance, and it has the following format:
#
# [knapsack_size][number_of_items]
#
# [value_1] [weight_1]
#
# [value_2] [weight_2]
#
# ...
#
# For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size
# 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.
#
# This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space.
# So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation,
# solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis.
# Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.
#
# In the box below, type in the value of the optimal solution.
#
# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then
# post them to the discussion forum!

import time

class operation:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value


def ReadKnapsackFile(filename):
    operations = []
    with open(filename, 'r') as KNAP:
        line = KNAP.readline()
        knapsack_size, number_of_items = line.split()
        knapsack_size = int(knapsack_size)
        for line in KNAP:
            split = line.split()
            op = operation(int(split[0]), int(split[1]))
            operations.append(op)

    return operations, knapsack_size


def OptimalKnapsackSolution(V, W):
    table = []
    print("{} x {}".format(len(V)+1, W))
    for i in range(2):
        table.append([0 for j in range(W)])

    current_tbl = 1
    previous_tbl = 0

    for i, op in enumerate(V, 1):

        print("Processing {} of {}.".format(i, len(V)))
        start_time = time.time()

        for weight in range(W):
            if weight >= op.weight:
                table[current_tbl][weight] = max(table[previous_tbl][weight], table[previous_tbl][weight-op.weight]+op.value)
            else:
                table[current_tbl][weight] = table[previous_tbl][weight]

        current_tbl, previous_tbl = previous_tbl, current_tbl

        end_time = time.time()
        elapsed_time = end_time-start_time
        print("Iteration time was {0:.2f} seconds".format(elapsed_time))

    return table[previous_tbl][W-1]


if __name__ == '__main__':
    knapsack1, size1 = ReadKnapsackFile('knapsack1.txt')
    knapsack_big, size_big = ReadKnapsackFile('knapsack_big.txt')

    val1 = OptimalKnapsackSolution(knapsack1, size1)
    print("Knap Small Solution: {}".format(val1)) # 2493893
    val_big = OptimalKnapsackSolution(knapsack_big, size_big)
    print("Knap Big Solution : {}".format(val_big)) # 4243395
