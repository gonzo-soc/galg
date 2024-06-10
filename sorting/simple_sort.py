#! /usr/bin/env python3.7

def insertion_sort(in_array):
    debug_prefix = f'Debug [ {insertion_sort.__name__} ]'
    outcome = []
    if in_array is None:
        print(debug_prefix + " Error: argument is None\n")
        return outcome

    for i in range(0, len(in_array)):
        min_ind = find_min_ind(in_array)
        outcome.append(in_array[min_ind])
        in_array.remove(in_array[min_ind])

    return outcome


def find_min_ind(in_array):
    min = in_array[0]
    min_ind = 0

    for i in range(1, len(in_array)):
        if min > in_array[i]:
            min = in_array[i]
            min_ind = i

    return min_ind


def binary_search(sort_array, wanted, left, right):
    mi = int((left + right)/2)
    print(f"Debug binarySearch_SORT_GALG mi {mi} left {left} right {right}\n")
    if sort_array[mi] > wanted:
        if mi == 0:
            print(f"Debug binarySearch_SORT_GALG {wanted} < minimal value in the array {sort_array[0]} \n")
            return None
        else:
            return binary_search(sort_array, wanted, left, mi)
    elif sort_array[mi] < wanted:
        length = len(sort_array)
        if (length - mi) == 1:
            print(f"Debug binarySearch_SORT_GALG {wanted} > maximal value in the array {sort_array[length - 1]} \n")
            return None
        else:
            return binary_search(sort_array, wanted, mi, right)
    elif sort_array[mi] == wanted:
        return mi


def search_value_more_than(search_array, wanted, left, right):
    '''
    Search the least element in the list that bigger than wanted
    '''

    if right == left:
        if wanted < search_array[left]:
            return search_array[left]
        else:
            return None

    if right - left == 1 and right == len(search_array) - 1:
        if wanted < search_array[left]:
            return search_array[left]
        elif wanted < search_array[right]:
            return search_array[right]
        else:
            return None

    medium = int((left + right)/2)
    if search_array[medium] > wanted:
        return search_count_less_than(search_array, wanted, left, medium)
    elif search_array[medium] < wanted:
        return search_count_less_than(search_array, wanted, medium, right)


def search_count_less_than(search_array, wanted, left, right):
    if right == left:
        if wanted < search_array[left]:
            return 0
        else:
            return 1

    if right - left == 1:
        length = len(search_array)
        if search_array[left] < wanted < search_array[right]:
            # the count of nodes which are less than wanted
            return right
        elif right == length - 1:
            if wanted > search_array[right]:
                return length
            else:
                return length - 1

    medium = int((left + right)/2)
    if search_array[medium] > wanted:
        return search_count_less_than(search_array, wanted, left, medium)
    elif search_array[medium] < wanted:
        return search_count_less_than(search_array, wanted, medium, right)


def set_sort(in_array):
    i = 0
    while len(in_array) > i:
        if in_array[i] != i + 1:
            swap_v = in_array[i]
            next_i = None
            end_swap_i = None
            is_swap_stop = False

            while swap_v:
                next_i = in_array[swap_v - 1] - 1
                in_array[swap_v - 1] = swap_v
                if end_swap_i is None:
                    end_swap_i = i
                    in_array[i] = i + 1

                # a cycle (size of 2)
                if swap_v == in_array[next_i]:
                    is_swap_stop = True

                # end swapping:
                if is_swap_stop and next_i == end_swap_i:
                    swap_v = None
                    next_i = None
                    end_swap_i = None
                    is_swap_stop = False
                else:
                    is_swap_stop = True
                    # continue swapping
                    swap_v = in_array[next_i]
                    in_array[next_i] = next_i + 1
        else:
            i += 1

    return in_array


def main():
    # test insertion sort
    in_array = [1, 5, 3, -1, 4, -2]
    print("-" * 80 + f"\nInsertion sorting\n\tArray before {in_array}")
    sort_array = insertion_sort(in_array)
    print(f"\n\tArray after {sort_array}\n")

    # test binary search
    wanted = -3
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binary_search(sort_array, wanted, 0, len(sort_array))}')
    wanted = 20
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binary_search(sort_array, wanted, 0, len(sort_array))}')
    wanted = -2
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binary_search(sort_array, wanted, 0, len(sort_array))}')
    wanted = 5
    print("\n" + "-" * 80 + f'\nBinary search.\n\tInfo: wanted [{wanted}] index: {binary_search(sort_array, wanted, 0, len(sort_array))}')

    return True


if __name_ == "__main__":
    main()
