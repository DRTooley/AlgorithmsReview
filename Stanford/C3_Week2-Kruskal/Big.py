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









def ReadInClusteringBig(file_name):
    tree = Tree()
    with open(file_name, 'r') as clust_big:
        nn = clust_big.readline()
        nn = nn.split()
        number_of_nodes = int(nn[0])
        number_of_bits = int(nn[1])
        for line in clust_big.readlines():
            tree.AddValue(''.join(line.split()))

    return tree

class Tree:
    def __init__(self):
        self.d = dict()
        self.gen_vals = set()

    def AddValue(self, val):
        cur_d = self.d
        for p in val:
            if p not in cur_d:
                cur_d[p] = dict()
            cur_d = cur_d[p]



    def GetRandomValue(self, value):
        if not value:
            return ''
        for key, v in value.items():
            return key + self.GetRandomValue(v)

    def RemoveValue(self, value, current):
        for bit in value:
            if len(current) > 1:
                current = current[bit]
            else:
                del current[bit]
                break

    def RemoveAssociatedBits(self, value, current, k):
        if not value:
            return True
        if not current:
            return True
        bit = value[0]
        if bit in current:
            remove = self.RemoveAssociatedBits(value[1:], current[bit], k)
            if remove:
                del current[bit]
                #print("removed {}".format(bit))
        else:
            #print("DNE")
            pass

        if k > 0:
            if bit == '0':
                not_bit = '1'
            else:
                not_bit = '0'
            if not_bit in current:
                remove_other = self.RemoveAssociatedBits(value[1:], current[not_bit], k-1)
                if remove_other:
                    del current[not_bit]
                    #print("notbit removed {}".format(not_bit))
            else:
                #print("Notbit DNE")
                pass
        #print('k: {} : {}'.format(k,value))
        return not bool(current)



    def RemoveCluster(self, k=2):
        str_bits = self.GetRandomValue(self.d)
        if str_bits in self.gen_vals:
            self.d = dict()
            print("ERROR Multi Generation problem")
        self.gen_vals.add(str_bits)
        print(str_bits)
        if len(str_bits) != 24:
            print("ERROR word count")
            self.d = dict()
            return
        self.RemoveAssociatedBits(str_bits, self.d, k)
        print()



if __name__ == '__main__':
    bits = ReadInClusteringBig('clustering_big.txt')
    cluster_count = 0
    while bits.d:
        bits.RemoveCluster()
        cluster_count += 1
        print(cluster_count)

    print("Final Cluster Count: {}".format(cluster_count))
