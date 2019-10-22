#! /usr/bin/env python3.7

'''
Chapter 04 - 1. Quick sort implementation (O(n * log(n)))
'''


def quick_sort_SORT_GALG(in_array, left, right):
    if len(in_array) < 2:

        print("Debug quick_sort: return array is less then 2 in length")
        print(in_array)

        return in_array

    sn_ind = int((left + right)/2)
    sn = in_array[sn_ind]

    less_stable_nodes = filterLessStableNode_SORT_GALG(in_array, sn)
    higher_stable_nodes = filterHigherStableNode_SORT_GALG(in_array, sn)
    equal_stable_nodes = filterEqualStableNode_SORT_GALG(in_array, sn)

    print('Debug quick_sort: less_stable_nodes')
    print(less_stable_nodes)
    print('Debug quick_sort: higher_stable_nodes')
    print(higher_stable_nodes)
    print('Debug quick_sort: equal_stable_nodes')
    print(equal_stable_nodes)

    '''
    every recursive call will return his result
    (although we don't apply return to the function call directly
    - we use concatenation - "+")
    '''
    return quick_sort_SORT_GALG(
        less_stable_nodes,
        0, len(less_stable_nodes)
    ) + equal_stable_nodes + quick_sort_SORT_GALG(
        higher_stable_nodes, 0, len(higher_stable_nodes)
    )


def filterLessStableNode_SORT_GALG(in_array, sn):
    return [i for i in in_array[0:] if i < sn]


def filterHigherStableNode_SORT_GALG(in_array, sn):
    return [i for i in in_array[0:] if i > sn]


def filterEqualStableNode_SORT_GALG(in_array, sn):
    return [i for i in in_array[0:] if i == sn]


print('Debug quick sort: Test 001 \n')
print('-' * 80)
print('\nDebug: Primary array\n')
in_array = [3, 2, 1]
print(in_array)

out_array = []
sorted_array = quick_sort_SORT_GALG(in_array, 0, len(in_array))

print('Debug: Sorted_array:\n')
print(sorted_array)
print('-' * 80)

print('Debug quick sort: Test 002 \n')
print('-' * 80)
print('\nDebug: Primary array\n')
in_array = [5, 4, 3, 2, 1]
print(in_array)

out_array = []
sorted_array = quick_sort_SORT_GALG(in_array, 0, len(in_array))

print('Debug: Sorted_array:\n')
print(sorted_array)
print('-' * 80)


print('Debug quick sort: Test 003 \n')
print('-' * 80)
print('\nDebug: Primary array\n')
in_array = [5, 5, 4, 3, 2, 4, 1]
print(in_array)

out_array = []
sorted_array = quick_sort_SORT_GALG(in_array, 0, len(in_array))

print('Debug: Sorted_array:\n')
print(sorted_array)
print('-' * 80)


print('Debug quick sort: Test 004 \n')
print('-' * 80)
print('\nDebug: Primary array\n')
in_array = [1, 2, 3, 4, 5, 6, 7]
print(in_array)

out_array = []
sorted_array = quick_sort_SORT_GALG(in_array, 0, len(in_array))

print('Debug: Sorted_array:\n')
print(sorted_array)
print('-' * 80)


print('Debug quick sort: Test 005 \n')
print('-' * 80)
print('\nDebug: Primary array\n')
in_array = [-9, 0, 1, -1, 2, 8, 10, -10, -20, -15]
print(in_array)

out_array = []
sorted_array = quick_sort_SORT_GALG(in_array, 0, len(in_array))

print('Debug: Sorted_array:\n')
print(sorted_array)
print('-' * 80)
