#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from arrays.minimum_swaps import minimum_swaps
from array import array


def main():
    in_array = array('i', [4, 3, 1, 2])  # expect 3
    print("Test 003 Input array {}\nMinimum swap: {}"
          .format(in_array, minimum_swaps(in_array)))

    in_array = array('i', [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46,
                           23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20,
                           17, 45, 43, 25, 19])  # expected 46
    print("Test 000 Input array {}\nMinimum swap: {}"
          .format(in_array, minimum_swaps(in_array)))

    in_array = array('i', [7, 1, 3, 2, 4, 5, 6])  # expect 5
    print("Test 004 Input array {}\nMinimum swap: {}"
          .format(in_array, minimum_swaps(in_array)))

    in_array = array('i', [3, 1, 2, 5, 7, 6, 4])
    print("Test 000 Input array {}\nMinimum swap: {}"
          .format(in_array, minimum_swaps(in_array)))

    in_array = array('i', [1, 3, 5, 2, 4, 6, 7])  # expect 3
    print("Test 001 Input array {}\nMinimum swap: {}"
          .format(in_array, minimum_swaps(in_array)))

    in_array = array('i', [2, 3, 4, 1, 5])  # expect 3
    print("Test 002 Input array {}\nMinimum swap: {}"
          .format(in_array, minimum_swaps(in_array)))


if __name__ == "__main__":
    main()
