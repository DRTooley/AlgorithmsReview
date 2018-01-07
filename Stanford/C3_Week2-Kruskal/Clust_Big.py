# In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So
# big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an
# explicit list.
#
# The data set is below.
# clustering_big.txt
#
# The format is:
#
# [# of nodes] [# of bits for each node's label]
#
# [first bit of node 1] ... [last bit of node 1]
#
# [first bit of node 2] ... [last bit of node 2]
#
# ...
#
# For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits
# associated with node #2.
#
# The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing
# bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above
# and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st
# bits).
#
# The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? That is,
# how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different
# clusters?
#
# NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let
# alone sort the edges by cost. So you will have to be a little creative to complete this part of the question. For
# example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?


import gc

from utils.hamming_calculations import Hamming


def ReadInClusteringBig(file_name):
    bits = []
    with open(file_name, 'r') as clust_big:
        nn = clust_big.readline()
        nn = nn.split()
        number_of_nodes = int(nn[0])
        number_of_bits = int(nn[1])
        for line in clust_big.readlines():
            line = ''.join(line.split())
            bits.append(int(line, 2))

    return bits

def GetK(location):
    unique = []
    for node in range(len(location)):
        matched  = False
        for cluster in unique:
            if location[node] is cluster:
                matched = True
                break
        if not matched:
            unique.append(location[node])

    return len(unique)



def ClusteringBig():
    bits = ReadInClusteringBig('clustering_big.txt')
    print(len(bits))
    print("Sorting...")
    bits.sort()
    location = dict()
    for i in range(len(bits)):
        connecting_sets = list()
        for j in range(i-1, -1, -1):
            if Hamming.Distance(bits[i], bits[j]) <= 2:
                add_this = True
                for add_set in connecting_sets:
                    if location[j] is add_set:
                        add_this = False
                if add_this:
                    connecting_sets.append(location[j])

        if not connecting_sets:
            location[i] = set([i])
        else:
            base_set = max(connecting_sets, key=len)
            base_set.add(i)
            location[i] = base_set
            for other_set in connecting_sets:
                if other_set is not base_set:
                    base_set = base_set.union(other_set)
                    for val in other_set:
                        location[val] = base_set




        if i % 10000 == 0:
            print('i: {}'.format(i))
            gc.collect()
            k_val = GetK(location)
            print('Max K value: {}'.format(k_val))
            print()

    k_val = GetK(location)
    print('Final Max K value: {}'.format(k_val))

if __name__ == '__main__':
    #clustering1()
    ClusteringBig()
