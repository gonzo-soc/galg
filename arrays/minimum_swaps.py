#! /usr/bin/env python3.7

'''
Minimum Swaps 2 challenge from here:
https://www.hackerrank.com/challenges/minimum-swaps-2/
problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''


def minimum_swaps(in_arr):
    node_to_index_map = {}
    min_swap = 0
    for i in range(len(in_arr)):
        node_to_index_map[in_arr[i]] = i

    i = 0
    while len(in_arr) > i:
        if in_arr[i] != i + 1:
            curr_i = i
            swap_v = in_arr[curr_i]
            while swap_v:
                in_arr[curr_i] = curr_i + 1
                if curr_i == swap_v - 1 and in_arr[curr_i] == swap_v:
                    node_to_index_map[swap_v] = curr_i
                    swap_v = None
                    curr_i = None
                else:
                    prev_i = curr_i
                    curr_i = node_to_index_map[curr_i + 1]
                    node_to_index_map[prev_i + 1] = prev_i
                    in_arr[curr_i] = swap_v
                    min_swap += 1
        else:
            i += 1

    return min_swap
