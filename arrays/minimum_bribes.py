#! /usr/bin/env python3.7

from array import array

'''
Task New Year chaotic

From here: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
Eventually I ve found an efficient solution: complexity < O(n^2)

Solution 02 (function quick_minimum_bribes) is based on building a map of bypassed nodes:

1 2 3 5 10 6 7 8 9

Initialize: { 9 -> 1; 10 -> 0 } where 1 means wasted
Loop 5 on ... 10 6 ... {6 -> 1 7 -> 1 8 -> 1 9 -> 1}
Loop 6 - check ... 10, 6 ... position: from [10 ..6] see built map
'''


def slow_minimum_bribes(in_array):
    length = len(in_array)
    i = length - 1

    is_too_chaotic = False
    # who was bribed: public officer
    po_v = None
    # current kleptocrat bribes
    br_j = 0
    # summary bribes
    br_sum = 0

    while i >= 0 and not is_too_chaotic:

        if po_v and po_v > in_array[i]:
            po_v = None

        if not po_v and i - 1 >= 0 and in_array[i - 1] - in_array[i] > 0:
            po_v = in_array[i]
        elif po_v:
            br_j = 0
            klep_v = in_array[i]
            j = i + 1
            while j < length and not is_too_chaotic:
                if klep_v > in_array[j]:
                    br_j += 1

                if br_j > 2:
                    is_too_chaotic = True

                j += 1

            if not is_too_chaotic:
                br_sum += br_j

        i -= 1

    if is_too_chaotic:
        print("Too chaotic")
    else:
        print(br_sum)


def quick_minimum_bribes(in_array):
    length = len(in_array)
    i = length - 1

    is_too_chaotic = False
    # who was bribed: public officer
    po_v = None
    # current kleptocrat bribes
    br_j = 0
    # summary bribes
    br_sum = 0
    klep_v = None
    kleptocrat_map = {}

    if in_array[length - 1] != length:
        for j in range(in_array[length - 1], length):
            kleptocrat_map[j] = 0

    while i >= 0 and not is_too_chaotic:
        if po_v and po_v > in_array[i]:
            po_v = None
            if i + 1 < length - 1 and in_array[i+1] - in_array[i] >= 0:
                for j in range(in_array[i], in_array[i+1]):
                    kleptocrat_map.setdefault(j, 0)
            kleptocrat_map[in_array[i]] = 1
        if not po_v and i - 1 >= 0:
            if in_array[i - 1] - in_array[i] > 0:
                po_v = in_array[i]
            elif in_array[i] - in_array[i - 1] >= 1:
                for j in range(in_array[i - 1], in_array[i] + 1):
                    kleptocrat_map.setdefault(j, 0)
            kleptocrat_map[in_array[i]] = 1
        elif po_v and in_array[i] > po_v:
            j = in_array[i] - 1
            klep_v = in_array[i]
            br_j = 0
            while j >= po_v and not is_too_chaotic:
                if kleptocrat_map[j] == 1:
                    br_j += 1
                if br_j > 2:
                    is_too_chaotic = True
                j -= 1

            if br_j <= 2:
                br_sum += br_j
            kleptocrat_map[klep_v] = 1
        i -= 1

    if is_too_chaotic:
        print("Too chaotic")
    else:
        print(br_sum)
