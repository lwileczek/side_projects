#!/usr/bin/env python3

"""
Sorting algorithms to write:

  - [X]  Bucket sort
  - [X]  Bubble sort
  - [ ]  Insertion sort
  - [ ]  Selection sort
  - [ ]  Heapsort
  - [ ]  Mergesort 

"""
def bucket_sort(x, max_val=0):
    """
    A variation of the bucket sort. 

    Alg: Create an array as long as the max value in the given array. Then for
    each item in the list, increment the value in our new array whose index is
    the value from the input list. Then for all values that are not 0 list their
    index.

    E.g. Input: [3, 1, 4, 1]
    Max value is 4 => [0, 0, 0, 0, 0]
    Then increment:
        0. [0, 0, 0, 1, 0]
        1. [0, 1, 0, 1, 0]
        2. [0, 2, 0, 1, 0]
        2. [0, 2, 0, 1, 1]
    Output: [1, 1, 3, 4]


    WARNING: currently all values must be non-negative

    O(n)
    Problems may arise with memory and that we must know the max value in the
    list wich requires previous knowledge of the list or added checks.
    """
    sorted_list = [0] * len(x)
    idx = 0
    if max_val == 0:
        for item in x:
            if item > max_val:
                max_val = item
    if max_val == 0:
        # after checking list if max value is 0 either list is all zeros or all
        # negatives. No way to handle negative numbers currently
        return x
    idx_list = [0] * (max_val+1)
    for item in x:
        idx_list[item] += 1
    for val,count in enumerate(idx_list):
        if count > 0:
            for each in range(count):
                sorted_list[idx] = val
                idx += 1

    return sorted_list


def bubble_sort(x):
    """
    Bubble sort algorithm: Go through list and if the number after is larger
    than the number before switch them. Continue this until you go through the
    list and it makes so switches.
    """
    list_copy = x.copy()
    while True:
        flag = 1
        for idx, first, second in zip(range(len(x)), x[:-1], x[1:]):
            if first > second:
                tmp = list_copy[idx]
                list_copy[idx] = list_copy[idx + 1]
                list_copy[idx + 1] = tmp
                if flag:
                    flag = 0

        if flag:  # if there was no switch after all checks then exit
            break
        x = list_copy.copy()  # else update x from copy and run again

    return x


def srt(x, sort_type='quick', max_val=None):
    """
    Building in different sorting algorithms using base python. 
    """
    assert isinstance(x, list), "Input must be a list"
    if len(x) < 2:
        return x
    if sort_type.lower() == 'bucket':
        sorted_list = bucket_sort(x)
    elif sort_type.lower() == 'bubble':
        sorted_list = bubble_sort(x)

    return sorted_list
    

if __name__ == "__main__":
    import numpy as np
    PRNG = np.random.RandomState()
    def test_sort():
## Create lists to test on
        tst0 = list(PRNG.randint(0, 15, size=6)) 
        tst1 = list(PRNG.randint(0, 15, size=6)) 
        tst2 = list(PRNG.randint(0, 115, size=70)) 

## Test Null and single case
        assert srt([], sort_type = 'bucket') == [], 'error with empty case'
        assert srt([0], sort_type = 'bucket') == [0], 'error with [0]'
        assert srt([1], sort_type = 'bucket') == [1], 'error with [1]'

## Test Bucket Sort
        assert  srt(tst1, sort_type = 'bucket') == sorted(tst1), 'Test case {}'\
        ' failed.'.format(tst1)
        assert  srt(tst2, sort_type = 'bucket') == sorted(tst2), 'Test case {}'\
        ' failed.'.format(tst2)
        ans0 = srt(tst0, sort_type = 'bucket')
        print("Bucket Sort:\n\tInput:", tst0, "\n\tOutcome:", ans0, "\n")

## Test Bubble Sort
        assert  srt(tst1, sort_type = 'bubble') == sorted(tst1), 'Test case {}'\
        ' failed.'.format(tst1)
        assert  srt(tst2, sort_type = 'bubble') == sorted(tst2), 'Test case {}'\
        ' failed.'.format(tst2)
        assert  srt(tst0, sort_type = 'bubble') == sorted(tst0), 'Test case {}'\
        ' failed.'.format(tst0)
        print("Bubble Sort:\n\tInput:", tst0, "\n\tOutcome:", 
            srt(tst0, sort_type='bubble'),"\n")

    test_sort()  # run test function 
    
