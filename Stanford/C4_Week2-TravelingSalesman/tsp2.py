
from traveling_salesman import ReadTSPFile
from itertools import combinations
from utils.euclidean_distance import EuclideanDistance
import time

def solve_tsp(nodes):
    init_node = nodes[0].identifier
    init_sets = combinations([node.identifier for node in nodes], 1)
    next_sets = {frozenset(s): dict() for s in init_sets}
    tsp_values = next_sets
    for n in tsp_values:
        if n == frozenset([init_node]):
            tsp_values[n][init_node] = 0
        else:
            tsp_values[n][init_node] = float('inf')

    for m in range(1, len(nodes), 1):
        iter_time = time.time()
        next_combo = combinations([node.identifier for node in nodes], m+1)

        # All subsets of the graph for which we need to calculate distances to potential destinations must contain
        # the init_node. Otherwise they are not valid subsets to calculate a TSP distance for.
        next_combo = [frozenset(s) for s in next_combo if init_node in frozenset(s)]

        # Update the valid sets and add a dictionary to hold the distance to each destination in S
        tsp_values.update({s: dict() for s in next_combo})

        # Update progress to user
        print('{} : {} : {}'.format(m, len(next_combo), len(tsp_values)))

        # For every valid subset of size m+1 of the initial graph
        for S in next_combo:
            # For every possible destination in S
            for j in S:
                # init_node is an invalid destination until the end
                if j != init_node:
                    # Use the set containing all distances to 'end nodes' that does not contain the current end node
                    previous_set = S-frozenset([j])
                    current_min = float('inf')
                    for k in previous_set:
                        # This is here to exclude init_node from being the previous end node in every case except for m=1
                        if k in tsp_values[previous_set]:
                            next_guess = EuclideanDistance(nodes[k], nodes[j]) + tsp_values[previous_set][k]
                            current_min = min(current_min, next_guess)

                    tsp_values[S][j] = current_min

        items_to_delete = []
        for S_to_del in tsp_values:
            if len(S_to_del) == m:
                items_to_delete.append(S_to_del)
        for item in items_to_delete:
            del tsp_values[item]

        print("Iteration {0} Complete in: {1:.2f} seconds".format(m, time.time()-iter_time))


    final_set = frozenset([node.identifier for node in nodes])
    c_min = float('inf')
    for k, tot_cost in tsp_values[final_set].items():
        c_min = min(c_min, tot_cost+EuclideanDistance(nodes[k], nodes[init_node]))

    return c_min



if __name__ == '__main__':
    nodes = ReadTSPFile('tsp.txt')

    val = solve_tsp(nodes)
    print("Min TSP: {}".format(val))