from array import array

'''
Task New Year chaotic
from here:
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
By now managed with O(n^2) complexity, but there is more efficient way (in searching...)
'''


def minimumBribes(in_array):
    length = len(in_array)
    i = length - 1

    isTooChaotic = False
    # who was bribed: public officer
    po_v = None
    # current kleptocrat bribes
    br_j = 0
    # summary bribes
    br_sum = 0
    klep_v = None

    while i >= 0 and not isTooChaotic:

        if po_v and po_v > in_array[i]:
            po_v = None

        if not po_v and i - 1 >= 0 and in_array[i - 1] - in_array[i] > 0:
            po_v = in_array[i]
        elif po_v:
            br_j = 0
            klep_v = in_array[i]
            j = i + 1
            while j < length and not isTooChaotic:
                if klep_v > in_array[j]:
                    br_j += 1

                if br_j > 2:
                    isTooChaotic = True

                j += 1

            if not isTooChaotic:
                br_sum += br_j

        i -= 1

    if isTooChaotic:
        print("Too chaotic")
    else:
        print(br_sum)


if __name__ == '__main__':

    arr = array('i', [2, 1, 5, 3, 4])  # expect 3

    print("Debug Test 001\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}".format(arr))
    minimumBribes(arr)

    arr = array('i', [1, 2, 3, 4, 5, 7, 8, 6, 9, 11, 10])

    print("Debug Test 002\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}".format(arr))
    minimumBribes(arr)

    arr = array('i', [1, 2, 5, 3, 7, 8, 6, 4])  # except 7

    print("Debug Test 003\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}".format(arr))
    minimumBribes(arr)

    arr = array('i', [5, 1, 2, 3, 7, 8, 6, 4])  # Too chaotic

    print("Debug Test 002\n" + "-" * 30)
    input_arr = ' '.join(map(str, arr))
    print("Input array: {}".format(arr))
    minimumBribes(arr)
