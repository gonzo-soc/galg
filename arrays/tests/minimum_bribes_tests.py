#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')

from array import array
from arrays.minimum_bribes import quick_minimum_bribes


def main():
    with open("test_minimum_bribes_001.txt", 'r') as f:
        arr = [int(x) for x in f.read().rstrip().split(', ')]

    print("Debug Test 002\n" + "-" * 30)
    print("Input array: {}".format(arr))
    quick_minimum_bribes(arr)

    arr = array('i', [2, 3, 1, 4, 5, 7, 8, 6, 9, 11, 10])  # expect 5

    print("Debug Test 002\n" + "-" * 30)
    print("Input array: {}".format(arr))
    quick_minimum_bribes(arr)

    arr = array('i', [5, 1, 2, 3, 7, 8, 6, 4])  # Too chaotic

    print("Debug Test 002\n" + "-" * 30)
    print("Input array: {}".format(arr))
    quick_minimum_bribes(arr)

    arr = array('i', [1, 2, 5, 3, 7, 8, 6, 4])  # except 7

    print("Debug Test 003\n" + "-" * 30)
    print("Input array: {}".format(arr))
    quick_minimum_bribes(arr)

    arr = array('i', [2, 1, 5, 3, 4])  # expect 3

    print("Debug Test 001\n" + "-" * 30)
    print("Input array: {}".format(arr))
    quick_minimum_bribes(arr)


if __name__ == "__main__":
    main()
