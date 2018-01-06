
import math

euclidean_memory = dict()
def EuclideanDistance(coord1, coord2):
    fs = frozenset([coord1, coord2])
    if fs not in euclidean_memory:
        euclidean_memory[fs] = math.sqrt(math.pow((coord1.x-coord2.x), 2) + math.pow((coord1.y-coord2.y), 2))
    return euclidean_memory[fs]