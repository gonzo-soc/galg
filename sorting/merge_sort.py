#! /usr/bin/env python3.7

'''
Chapter 04 - 1. Merge sort implementation (O(n * log(n)))
'''


def merge_sort(in_array, left, right):
    if len(in_array) == 1:
        return in_array

    me = int((left + right) / 2)

    left_array = []
    right_array = []
    # single element
    if left == me:
        left_array.append(in_array[left])
    elif me - left == 1:
        left_array = in_array[left:me + 1]
        if in_array[left] > in_array[me]:
            left_array[0:1], left_array[1:] = left_array[1:], left_array[0:1]

    if right == me + 1:
        right_array.append(in_array[right])

    if me - left < 2:
        return merge(left_array, right_array)

    return merge(merge_sort(in_array, left, me),
                 merge_sort(in_array, me + 1, right))


def merge(left_array, right_array):
    left_len = len(left_array)
    right_len = len(right_array)
    if left_len > 0 and right_len == 0:
        return left_array
    elif right_len > 0 and left_len == 0:
        return right_array

    # merge left and right in merged_cut,
    k = 0
    m = 0
    merged_array = []
    left_len = len(left_array)
    right_len = len(right_array)
    while k < left_len or m < right_len:
        if k < left_len and ((m < right_len and left_array[k] <= right_array[m]) or m >= right_len):
            merged_array.append(left_array[k])
            k += 1
        elif m < right_len:
            merged_array.append(right_array[m])
            m += 1

    return merged_array


if __name__ == "__main__":
    print('\nDebug merge sort: Test 008 \n')
    print('-' * 80)
    in_array = [10, 3, 2, -1, 0, 4]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('Debug merge sort: Test 003 \n')
    print('-' * 80)
    in_array = [2, 1, -1, 0, -100]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('Debug merge sort: Test 001 \n')
    print('-' * 80)
    in_array = [1]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('Debug merge sort: Test 002 \n')
    print('-' * 80)
    in_array = [2, 1, -1]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('\nDebug merge sort: Test 006 \n')
    print('-' * 80)
    in_array = [4, 3, 2, 1, 0]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('\nDebug merge sort: Test 007 \n')
    print('-' * 80)
    in_array = [1, 2, 3, 4, 5]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('\nDebug merge sort: Test 007 \n')
    print('-' * 80)
    in_array = [10, 3, 2, -1, -1]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)

    print('\nDebug merge sort: Test 009 \n')
    print('-' * 80)
    in_array = [10, 3, 2, -1, 0, 4, -3, -3, -100, -3]
    print('\nDebug: Primary array\n')
    print(in_array)

    s_array = merge_sort(in_array, 0, len(in_array) - 1)
    print('\n Debug sorted array: ')
    for v in s_array:
        print(v)
