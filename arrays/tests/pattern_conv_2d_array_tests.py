#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from arrays.pattern_conv_2d_array import pattern_conv_2d_array

'''
Task from
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''


def main():
    in_array = [
        [0, -4, -6, 0, -7, -6],
        [-1, -2, -6, -8, -3, -1],
        [-8, -4, -2, -8, -8, -6],
        [-3, -1, -2, -5, -7, -4],
        [-3, -5, -3, -6, -6, -6],
        [-3, -6, 0, -8, -6, -7]
    ]

    u_pattern = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print("Input pattern matrix: \n")
    for line in u_pattern:
        print(line)

    print("\nInput matrix: \n")
    for line in in_array:
        print(line)

    print("\nResult maximum summary:")
    print(f"\nMaximal sum: {pattern_conv_2d_array(in_array, u_pattern)}")


if __name__ == '__main__':
    main()
