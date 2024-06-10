#! /usr/bin/env python3.7

'''
Task from
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''


def pattern_conv_2d_array(in_array, u_pattern):
    max_sum = None
    # res = []
    for i in range(len(in_array)):
        isExit = False
        if (i + len(u_pattern) - 1 >= len(in_array)):
            break
        # res.append(list())
        for j in range(len(in_array[i])):
            ij_sum = 0
            for u_i in range(len(u_pattern)):
                if (j + len(u_pattern[u_i]) - 1 >= len(in_array[i])):
                    isExit = True
                    break
                else:
                    for u_j in range(len(u_pattern[u_i])):
                        ij_sum += u_pattern[u_i][u_j] * in_array[i + u_i][j + u_j]

            if not isExit:
                if max_sum is None:
                    max_sum = ij_sum
                elif max_sum < ij_sum:
                    max_sum = ij_sum
                # res[i].append(ij_sum)
            else:
                break

    return max_sum


def main():
    # expect -19
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
