"""
Heap sort

Complexity: n * log2(n)

"""

from typing import List


def swap(elements: List[int], iLeft: int, iRight: int):
    temp = elements[iLeft]
    elements[iLeft] = elements[iRight]
    elements[iRight] = temp


def getRootIndex(elements: List[int], iChild: int) -> int:
    return int((iChild - 1) / 2)


def iRightChild(elements: List[int], iRoot: int) -> int:
    return int(2 * iRoot + 2)


def iLeftChild(elements: List[int], iRoot: int) -> int:
    return int(2 * iRoot + 1)


def siftDown(elements: List[int], iRoot: int, iEnd: int):
    while iLeftChild(elements, iRoot) < iEnd:
        rightChildIndex = iRightChild(elements, iRoot)
        leftChildIndex = iLeftChild(elements, iRoot)
        iChild = leftChildIndex

        if (
            rightChildIndex < len(elements)
            and elements[rightChildIndex] < elements[leftChildIndex]
        ):
            swap(elements, leftChildIndex, rightChildIndex)

        if rightChildIndex < len(elements) and elements[rightChildIndex] > elements[iRoot]:
            swap(elements, iRoot, rightChildIndex)
        else:
            if elements[leftChildIndex] > elements[iRoot]:
                swap(elements, iRoot, leftChildIndex)
            else:
                return

        iRoot = getRootIndex(elements, iChild)


def heapify(elements: List[int]):
    start = getRootIndex(elements, len(elements) - 1)

    while start >= 0:
        siftDown(elements, start, len(elements))
        start = start - 1


def heapSort(elements: List[int]):
    heapify(elements)

    end = len(elements) - 1
    while end >= 1:
        swap(elements, 0, end)
        end = end - 1
        siftDown(elements, 0, end)


if __name__ == "__main__":
    elements: List[int] = [5, 2, 3, 7, 8, 0]
    heapSort(elements)
