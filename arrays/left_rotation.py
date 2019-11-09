#! /usr/bin/env python3.7

'''
Task from
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
Left rotation:
1) def rotate(arr, rot) - O(n^rot) => O(n^2)
2) def quick_rotate(arr, rot): O(n)
3) def leftRot(in_arr, in_rot): O(n)
'''
from array import array


def rotate(arr, rot):
    rot = rot % len(arr)
    if rot == 0:
        return arr

    n = 0
    v = arr[0]
    i = 0
    temp = ""
    while n < rot:
        i -= 1
        if i < 0:
            i += len(arr)
            temp = arr[i]
            arr[i] = v
            if i == 0:
                v = arr[0]
            n += 1
        else:
            v = temp


def quickRotate(arr, rot):
    rot = rot % len(arr)
    if rot == 0:
        return arr
    m = len(arr) - rot
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, m - 1)
    if m + 1 < len(arr):
        reverse(arr, m, len(arr) - 1)

    return arr


def reverse(arr, left, right):
    if left == right and left == 0:
        return arr

    i = left
    j = right

    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

    return arr


def leftRot(in_arr, in_rot):
    rot = in_rot % len(in_arr)
    if rot == 0:
        return in_arr

    i = 0
    j = i + rot
    right = len(in_arr) - 1
    l = len(in_arr)

    while True:
        # shift from left to right
        if int(l/rot) >= 2:
            n = 0
            # quantity of rotation in the cut
            rot_q = int((l - rot)/rot)
            while int(n/rot) < rot_q:
                temp = in_arr[i]
                in_arr[i] = in_arr[j]
                in_arr[j] = temp
                i += 1
                j += 1
                n += 1

        # shift from right to left
        l = right - i + 1
        if l % rot != 0:
            rot = right - j + 1
            left = i
            i = right - rot
            j = right
            rot_q = int((l - rot)/rot)
            n = 0
            while int(n/rot) < rot_q:
                temp = in_arr[i]
                in_arr[i] = in_arr[j]
                in_arr[j] = temp
                i -= 1
                j -= 1
                n += 1

                if i + 1 != left:
                    rot = i - left + 1
                    right = j
                    j = i + 1
                    i = left
                    l = right - i + 1
                else:
                    break
        else:
            break

    return in_arr


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
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [33, 47, 70, 37, 8, 53, 13, 93,
                      71, 72, 51, 100, 60, 87, 97])
    rot = 13
    print("Debug Test 000\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5, 6, 7])
    rot = 3

    print("Debug Test 001\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
    rot = 4

    print("Debug Test 002\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
    rot = 5

    print("Debug Test 003\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2, 3, 4, 5])
    rot = 4

    print("Debug Test 004\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [1, 2])
    rot = 1

    print("Debug Test 005\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))

    arr = array('i', [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86,
                      58, 26, 10, 86, 51])
    rot = 10

    print("Debug Test 006\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}, rotation {}".format(input_arr, rot))
    output_arr = ' '.join(map(str, leftRot(arr, rot)))
    print("Rotated array: {}\n".format(output_arr))
