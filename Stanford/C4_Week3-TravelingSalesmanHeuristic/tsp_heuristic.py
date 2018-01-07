# In this assignment we will revisit an old friend, the traveling salesman problem (TSP). This week you will implement a
# heuristic for the TSP, rather than an exact algorithm, and as a result will be able to handle much larger problem
# sizes. Here is a data file describing a TSP instance (original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.
# tsp).

# The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates
# the x- and y-coordinates of a single city.

# The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and
# (z,w) have distance (x−z)2+(y−w)2 between them.

# You should implement the nearest neighbor heuristic:

#    Start the tour at the first city.
#    Repeatedly visit the closest city that the tour hasn't visited yet. In case of a tie, go to the closest city with
#      the lowest index. For example, if both the third and fifth cities have the same distance from the first city
#      (and are closer than any other city), then the tour should begin by going from the first city to the third city.
#    Once every city has been visited exactly once, return to the first city to complete the tour.

# In the box below, enter the cost of the traveling salesman tour computed by the nearest neighbor heuristic for this
# instance, rounded down to the nearest integer.

# [Hint: when constructing the tour, you might find it simpler to work with squared Euclidean distances (i.e., the
# formula above but without the square root) than Euclidean distances. But don't forget to report the length of the tour
# in terms of standard Euclidean distance.]


from utils.euclidean_distance import EuclideanDistance
import time

class EuclideanPoint:
    def __init__(self, identifier, x, y):
        self.x = x
        self.y = y


def ReadTSPFile(filename):
    nodes = []
    with open(filename, 'r') as tsp:
        city_count  = tsp.readline()
        for i, line in enumerate(tsp):
            line = line.split()
            identifier, x, y = int(line[0]), float(line[1]), float(line[2])
            nodes.append(EuclideanPoint(identifier, x, y))

    return nodes

def solve_tsp_with_heuristic(points):
    tsp_distance = 0
    unvisited_cities = set(range(len(points)))
    current_city = 0
    unvisited_cities.remove(0)
    time_1000 = time.time()
    while unvisited_cities:
        nearest_city_dist = float('inf')
        next_city = None
        for uv_city in unvisited_cities:
            city_dist = EuclideanDistance(points[current_city], points[uv_city], memory=False)
            if city_dist < nearest_city_dist:
                nearest_city_dist = city_dist
                next_city = uv_city
        tsp_distance += nearest_city_dist

        current_city = next_city
        unvisited_cities.remove(next_city)

        if len(unvisited_cities) % 1000 == 0:
            print('Execution of previous 1000 took {0:.2f} seconds.'.format(time.time()-time_1000))
            time_remaining = len(unvisited_cities)//1000 * (time.time()-time_1000)
            print('{0} cities remaining. Estimated time left: {1:.2f}'.format(len(unvisited_cities), time_remaining))
            time_1000 = time.time()

    return tsp_distance + EuclideanDistance(points[current_city], points[0])








if __name__ == '__main__':
    nodes = ReadTSPFile('nn.txt')

    val = solve_tsp_with_heuristic(nodes)
    print("Min TSP: {}".format(val))