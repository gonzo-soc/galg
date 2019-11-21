#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from arrays.left_rotation import left_rot
from array import array


def main():
    arr = array('i', [431, 397, 149, 275, 556, 362, 852, 789, 601, 357, 516,
                      575, 670, 507, 127, 888, 284, 405, 806, 27, 495, 879,
                      976, 467, 342, 356, 908, 750, 769, 947, 425, 643, 754,
                      396, 653, 595, 108, 75, 347, 394, 935, 252, 683, 966,
                      553, 724, 629, 567, 93, 494, 693, 965, 328, 187, 728,
                      389, 70, 288, 509, 252, 449])
    rot = 9
    print("Debug Test 007\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [33, 47, 70, 37, 8, 53, 13, 93,
                      71, 72, 51, 100, 60, 87, 97])
    rot = 13
    print("Debug Test 000\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5, 6, 7])
    rot = 3

    print("Debug Test 001\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
    rot = 4

    print("Debug Test 002\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
    rot = 5

    print("Debug Test 003\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5])
    rot = 4

    print("Debug Test 004\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2])
    rot = 1

    print("Debug Test 005\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86,
                      58, 26, 10, 86, 51])
    rot = 10

    print("Debug Test 006\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, left_rot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))


if __name__ == "__main__":
    main()
