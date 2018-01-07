# The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap
# applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this
# as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is
# defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk;
# if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

# In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is,
# you should compute (m1+m2+m3+⋯+m10000)mod10000.

# OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the
# algorithm.

import heapq
from enum import Enum

class Indicator(Enum):
    HIGH = 0
    LOW = 1
    MEAN = 2
    INVALID = 3


class MeadianHeapq:
    def __init__(self):
        self.__heap_low = []
        self.__heap_high = []

    def PeakMedian(self):
        indic = self.__FindMedianHomeHeap()
        if indic == Indicator.HIGH:
            return self.__PeakHigh()
        elif indic == Indicator.LOW:
            return self.__PeakLow()
        elif indic == Indicator.MEAN:
            low = self.__PeakLow()
            high = self.__PeakHigh()
            return (low+high)/2
        else:
            raise NotImplementedError

    def __FindMedianHomeHeap(self):
        self.__Balance()
        balance = len(self.__heap_high) - len(self.__heap_low)
        if balance == 1:
            # self.__heap_high has the median
            return Indicator.HIGH
        elif balance == -1 or balance == 0:
            # self.__heap_low has the median
            return Indicator.LOW
        elif len(self.__heap_high) > 0 and len(self.__heap_low) > 0:
            # The median is the mean of the two options
            return Indicator.MEAN
        else:
            # There are no values in either heap
            return Indicator.INVALID

    def Insert(self, value):
        if self.__heap_low and self.__heap_high:
            if value < self.__PeakLow():
                self.__InsertLow(value)
            else:
                self.__InsertHigh(value)
        else:
            self.__InsertLow(value)

        self.__Balance()

    def __PeakLow(self):
        return -1 * self.__heap_low[0]

    def __PopLow(self):
        return -1 * heapq.heappop(self.__heap_low)

    def __InsertLow(self, value):
        heapq.heappush(self.__heap_low, -1 * value)

    def __PeakHigh(self):
        return self.__heap_high[0]

    def __InsertHigh(self, value):
        heapq.heappush(self.__heap_high, value)

    def __PopHigh(self):
        return heapq.heappop(self.__heap_high)

    def __Balance(self):
        balance = len(self.__heap_high) - len(self.__heap_low)
        if abs(balance) > 1:
            if balance < 0:
                # rebalance self.__heap_low
                val = self.__PopLow()
                self.__InsertHigh(val)
            else:
                # rebalance self.__heap_high
                val = self.__PopHigh()
                self.__InsertLow(val)

            self.__Balance()










if __name__ == '__main__':
    median_maintainer = MeadianHeapq()
    programming_assignment_value = 0
    with open('Median.txt') as input_file:
        for value in input_file:
            value = int(value)
            median_maintainer.Insert(value)
            median = median_maintainer.PeakMedian()

            programming_assignment_value += median
            programming_assignment_value %= 10000
            print("Median: {}".format(median))
            print("PA: {}".format(programming_assignment_value))



