
import math


def EuclideanDistance(coord1, coord2):
    return math.sqrt(math.pow((coord1.x-coord2.x), 2) + math.pow((coord1.y-coord2.y), 2))