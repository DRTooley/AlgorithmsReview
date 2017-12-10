# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer
# in the ith row of the file gives you the ith entry of an input array.

# Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know,
# the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different
# pivoting rules.

# You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you
# should simply add m−1 to your running total of comparisons. (This is because the pivot element is compared to each of
# the other m−1 elements in the subarray in this recursive call.)

# WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give
# you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is
# described in the video lectures (otherwise you might get the wrong answer).

# DIRECTIONS FOR THIS PROBLEM:

# For the first part of the programming assignment, you should always use the first element of the array as the pivot
# element.

# HOW TO GIVE US YOUR ANSWER:

# Type the numeric answer in the space provided.

# So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other
# punctuation marks. You have 5 attempts to get the correct answer.

# (We do not require you to submit your code, so feel free to use the programming language of your choice, just type
# the numeric answer in the following space.)

from statistics import median

class c:
    comps = 0

def GetPivot(my_list, start, end):
    start_pivot = start

    end_pivot = end-1

    mid = start + (end_pivot - start_pivot) // 2


    #pivot = end_pivot
    #my_list[start], my_list[pivot] = my_list[pivot], my_list[start]

    start_val = my_list[start_pivot]
    mid_val = my_list[mid]
    end_val = my_list[end_pivot]

    pivot_val = median([start_val, mid_val, end_val])

    if pivot_val == my_list[start_pivot]:
        pivot = start_pivot

    elif pivot_val == my_list[mid]:
        pivot = mid

    elif pivot_val == my_list[end_pivot]:
        pivot = end_pivot

    else:
        raise NotImplementedError

    my_list[start], my_list[pivot] = my_list[pivot], my_list[start]


def Partition(my_list, start, end):
    pivot = start
    start = start + 1

    c.comps += end - start

    mid = pivot
    for j in range(start, end, 1):
        if my_list[j] < my_list[pivot]:
            mid += 1
            my_list[j], my_list[mid] = my_list[mid], my_list[j]

    my_list[mid], my_list[pivot] = my_list[pivot], my_list[mid]
    return mid

def QuickSort(my_list, start, end):
    if end - start <= 1:
        return
    GetPivot(my_list, start, end)
    # Start is assumed to be the pivot point
    mid = Partition(my_list, start, end)
    QuickSort(my_list, start, mid)
    QuickSort(my_list, mid+1, end)


def ReadQuickSortFile(filename):
    unsorted = []
    with open(filename) as qs_file:
        for line in qs_file:
            unsorted.append(int(line))

    return unsorted


if __name__ == '__main__':
    unsorted = ReadQuickSortFile('QuickSort.txt')

    c.comps = 0
    QuickSort(unsorted, 0, len(unsorted))
    print(unsorted == sorted(unsorted))
    #print(unsorted)
    print("Comparisons: {}".format(c.comps))