#! /usr/bin/env python3.7

"""
621. Task scheduler
https://leetcode.com/problems/task-scheduler/description/

"""

import unittest
from typing import List


class TestLeastInterval(unittest.TestCase):
    # def test_oneByOne(self):
    #     tasks: List[str] = ["A", "C", "A", "B", "D", "B"]
    #     n: int = 1
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 6)

    # def test_shortIdle(self):
    #     tasks: List[str] = ["A", "B"]
    #     n: int = 2
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 2)

    # def test_tripleIdle(self):
    #     tasks: List[str] = ["A", "A", "B"]
    #     n: int = 2
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 4)

    # def test_Idle(self):
    #     tasks: List[str] = ["A", "A", "A", "B", "B", "B"]
    #     n: int = 2
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 8)

    # def test_doubleIdle(self):
    #     tasks: List[str] = ["A", "A", "A", "B", "B", "B"]
    #     n: int = 3
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 10)

    # def test_complexOne(self):
    #     tasks: List[str] = ["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"]
    #     n: int = 4
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 10)

    # def test_complexTwo(self):
    #     tasks: List[str] = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    #     n: int = 1
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 12)

    def test_complexThree(self):
        tasks: List[str] = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
        n: int = 2
        print("Tasks: {}, interval: {}".format(tasks, n))
        self.assertEqual(leastInterval(tasks, n), 12)


def findTaskGroupEqualOrLessSize(
    taskQueue: List[str], equalOrLessGrSize: int, prev_stop_i: int
):
    """
    Find max repeat group after another:
        A,A,A,D,A,B,B,C,B,C:

        max group symbol size = 4 (A symbol), then B symbol size = 3...
        So that max group after A symbol group (4) = 3
    """
    if len(taskQueue) == 1:
        return "{}:{}".format(0, 1)
    i = (
        prev_stop_i + 1
        if prev_stop_i > 0 and prev_stop_i + 1 < len(taskQueue)
        else prev_stop_i
    )

    stop_i = i
    curr_size = result_gr_size = 1
    while i + 1 < len(taskQueue):
        if taskQueue[i] == taskQueue[i + 1]:
            curr_size += 1
        if result_gr_size < curr_size and result_gr_size <= equalOrLessGrSize:
            result_gr_size = curr_size
            stop_i = (
                i + 1
                if (taskQueue[i] == taskQueue[i + 1] and i + 1 < len(taskQueue))
                else i
            )
        if taskQueue[i] != taskQueue[i + 1]:
            curr_size = 1
        i += 1

    return "{}:{}".format(stop_i, result_gr_size)


def leastInterval(taskQueue: List[str], n: int) -> int:
    """ """
    if n == 0 or len(taskQueue) == 1:
        return len(taskQueue)
    stop_i = 0
    j = 0
    k = 0
    equal_or_less_gr_size = 65536
    taskQueue.sort()
    resultList = [taskQueue[stop_i]]
    del taskQueue[stop_i]
    while len(taskQueue) > 0:
        stop_i, equal_or_less_gr_size = findTaskGroupEqualOrLessSize(
            taskQueue, equal_or_less_gr_size, stop_i
        ).split(":")
        stop_i = int(stop_i)
        equal_or_less_gr_size = int(equal_or_less_gr_size)
        k = 0
        canSet = True
        while len(resultList) > 0 and canSet and k < n and j - k >= 0:
            if taskQueue[stop_i] == resultList[j - k]:
                canSet = False
            k += 1
        if canSet:
            resultList.append(taskQueue[stop_i])
            del taskQueue[stop_i]
            stop_i = stop_i - 1 if stop_i > 0 else stop_i
        else:
            if stop_i + 1 >= len(taskQueue):
                resultList.append("idle")

        if stop_i + 1 >= len(taskQueue) or canSet:
            j += 1
        if stop_i + 1 >= len(taskQueue):
            equal_or_less_gr_size = 65536
            stop_i = 0
        else:
            if len(taskQueue) == 2 and not canSet and stop_i == 0:
                stop_i = 1
    return len(resultList)


if __name__ == "__main__":
    unittest.main()
