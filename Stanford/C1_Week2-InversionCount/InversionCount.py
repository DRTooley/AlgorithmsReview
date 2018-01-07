# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer
# repeated.

# Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith
# entry of an array.

# Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the
# video lectures.

# The numeric answer for the given input file should be typed in the space below.

# So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any
# other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

# (We do not require you to submit your code, so feel free to use any programming language you want --- just type the
# final numeric answer in the following space.)

# [TIP: before submitting, first test the correctness of your program on some small test files or your own devising.
# Then post your best test cases to the discussion forums to help your fellow students!]

# basically merge sort

def DoCountInversions(my_arr):
    _, inv_count = RecursiveCountInversions(my_arr)

    return inv_count

def RecursiveCountInversions(my_arr):
    if len(my_arr) <= 1:
        return my_arr, 0
    my_arr_1, x = RecursiveCountInversions(my_arr[:len(my_arr)//2])
    my_arr_2, y = RecursiveCountInversions(my_arr[len(my_arr) // 2:])
    z = CountInversions(my_arr, my_arr_1, my_arr_2)

    return my_arr, x+y+z

def CountInversions(my_arr, a1, a2):
    i, j = 0, 0
    inv_count = 0
    for k in range(len(my_arr)):
        if j >= len(a2) or (i < len(a1) and a1[i] <= a2[j]):
            my_arr[k] = a1[i]
            i += 1
        else:
            my_arr[k] = a2[j]
            j += 1
            inv_count += len(a1) - i

    return inv_count




def ReadInList(file_name):
    l = []
    with open(file_name, 'r') as list_file:
        for num in list_file:
            l.append(int(num))

    return l


if __name__ == '__main__':
    l = ReadInList('IntegerArray.txt')
    inv_count = DoCountInversions(l)
    print(inv_count)