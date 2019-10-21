#! /usr/bin/env python3.7

def insertion_sort_SORT_GALG(in_array):
    debug_prefix = f'Debug [ {insertion_sort_SORT_GALG.__name__} ]'
    outcome = []
    if in_array is None:
        print(debug_prefix + " Error: argument is None\n")
        return outcome

    for i in range(0, len(in_array)):
        min_ind = findMinInd_SORT_GALG(in_array)
        outcome.append(in_array[min_ind])
        in_array.remove(in_array[min_ind])

    return outcome


def findMinInd_SORT_GALG(in_array):
    min = in_array[0]
    min_ind = 0

    for i in range(1, len(in_array)):
        if min > in_array[i]:
            min = in_array[i]
            min_ind = i

    return min_ind


def binarySearch_SORT_GALG(sort_array, wanted, left, right):
    mi = int((left + right)/2)
    print(f"Debug binarySearch_SORT_GALG mi {mi} left {left} right {right}\n")
    if sort_array[mi] > wanted:
        if mi == 0:
            print(f"Debug binarySearch_SORT_GALG {wanted} < minimal value in the array {sort_array[0]} \n")
            return None
        else:
            return binarySearch_SORT_GALG(sort_array, wanted, left, mi)
    elif sort_array[mi] < wanted:
        length = len(sort_array)
        if (length - mi) == 1:
            print(f"Debug binarySearch_SORT_GALG {wanted} > maximal value in the array {sort_array[length - 1]} \n")
            return None
        else:
            return binarySearch_SORT_GALG(sort_array, wanted, mi, right)
    elif sort_array[mi] == wanted:
        return mi


def main_SORT_GALG():
    # test insertion sort
    in_array = [1, 5, 3, -1, 4, -2]
    print("-" * 80 + f"\nInsertion sorting\n\tArray before {in_array}")
    sort_array = insertion_sort_SORT_GALG(in_array)
    print(f"\n\tArray after {sort_array}\n")

    # test binary search
    wanted = -3
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binarySearch_SORT_GALG(sort_array, wanted, 0, len(sort_array))}')
    wanted = 20
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binarySearch_SORT_GALG(sort_array, wanted, 0, len(sort_array))}')
    wanted = -2
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binarySearch_SORT_GALG(sort_array, wanted, 0, len(sort_array))}')
    wanted = 5
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binarySearch_SORT_GALG(sort_array, wanted, 0, len(sort_array))}')

    return True


main_SORT_GALG()
