#!/usr/bin/env python3.7

'''
Chapter 04 - 2. Merge sort implementation (O(n * log(n)))
'''


def merge_sort_SORT_GALG(in_array, left, right):
    if len(in_array) == 1:
        return in_array

    me = int((left + right)/2)

    # print(f"\nDebug merge_sort_SORT_GALG me {me}, left {left}, right {right}")
    # print(f"\nDebug merge_sort_SORT_GALG in_array {in_array}")

    left_array = []
    right_array = []
    # single element
    if left == me:
        left_array.append(in_array[left])
    elif me - left == 1:
        if in_array[left] > in_array[me]:
            swap_SORT_GALG(in_array, left, me)
        left_array = in_array[left:me+1]
    # print(f"\nDebug merge_sort_SORT_GALG left_array {left_array}")

    if right == me + 1:
        right_array.append(in_array[right])
    elif right - me - 1 == 1:
        if in_array[me + 1] > in_array[right]:
            swap_SORT_GALG(in_array, me + 1, right)
        right_array = in_array[me + 1:right + 1]

    # print(f"\nDebug merge_sort_SORT_GALG right_array {right_array}")

    if me - left < 2:
        return merge_SORT_GALG(left_array, right_array)

    return merge_SORT_GALG(merge_sort_SORT_GALG(in_array, left, me), merge_sort_SORT_GALG(in_array, me + 1, right))


def swap_SORT_GALG(in_array, left, right):
    temp = in_array[right]
    in_array[right] = in_array[left]
    in_array[left] = temp
    return True


def merge_SORT_GALG(left_array, right_array):
    # print(f"\nDebug merge sort: left_array {left_array} right_array {right_array}\n")

    left_len = len(left_array)
    right_len = len(right_array)
    if left_len > 0 and right_len == 0:
        return left_array
    elif right_len > 0 and left_len == 0:
        return right_array

    merged_array = []
    i = 0
    j = 0
    while i < left_len or j < right_len:
        if i < left_len and j >= right_len:
            merged_array.append(left_array[i])
            i += 1
        elif j < right_len and i >= left_len:
            merged_array.append(right_array[j])
            j += 1
        elif i < left_len and left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            if left_array[i] == right_array[j]:
                merged_array.append(right_array[j])
                j += 1
            i += 1
        elif j < right_len:
            merged_array.append(right_array[j])
            j += 1

    return merged_array


print('Debug merge sort: Test 001 \n')
print('-' * 80)
in_array = [1]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array)
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))


print('\nDebug merge sort: Test 002 \n')
print('-' * 80)
in_array = [2, 1]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))


print('\nDebug merge sort: Test 003 \n')
print('-' * 80)
in_array = [3, 2, 1]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))


print('\nDebug merge sort: Test 004 \n')
print('-' * 80)
in_array = [1, 2, 3]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))


print('\nDebug merge sort: Test 005 \n')
print('-' * 80)
in_array = [4, 3, 2, 1]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))


print('\nDebug merge sort: Test 006 \n')
print('-' * 80)
in_array = [4, 3, 2, 1, 0]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))


print('\nDebug merge sort: Test 007 \n')
print('-' * 80)
in_array = [1, 2, 3, 4, 5]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))

print('\nDebug merge sort: Test 007 \n')
print('-' * 80)
in_array = [10, 3, 2, -1, -1]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))

print('\nDebug merge sort: Test 008 \n')
print('-' * 80)
in_array = [10, 3, 2, -1, 0, 4]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))

print('\nDebug merge sort: Test 009 \n')
print('-' * 80)
in_array = [10, 3, 2, -1, 0, 4, -3, -3, -100, -3]
print('\nDebug: Primary array\n')
print(in_array)

right = len(in_array) - 1
left = 0

print('-' * 80)
print('\nDebug: Sorted array\n')
print(merge_sort_SORT_GALG(in_array, left, right))
