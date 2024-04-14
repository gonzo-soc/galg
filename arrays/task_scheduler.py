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


def findMaxGroupAfter(taskQueue: List[str], max_repeat: int, start_i: int):
    """
    Find max repeat group after another:
        A,A,A,D,A,B,B,C,B,C:

        max group symbol size = 4 (A symbol), then B symbol size = 3...
        So that max group after A symbol group (4) = 3
    """
    if len(taskQueue) == 1:
        return "{}:{}".format(0, 1)
    i = start_i + 1 if start_i > 0 and start_i + 1 < len(taskQueue) else start_i

    stop_i = i
    curr_repeat = 1
    max_repeat_after = 0
    while i + 1 < len(taskQueue):
        if taskQueue[i] == taskQueue[i + 1]:
            curr_repeat += 1
        if max_repeat_after < curr_repeat and max_repeat_after <= max_repeat:
            max_repeat_after = curr_repeat
            stop_i = (
                i + 1
                if (taskQueue[i] == taskQueue[i + 1] and i + 1 < len(taskQueue))
                else i
            )
        if taskQueue[i] != taskQueue[i + 1]:
            curr_repeat = 1
        i += 1

    return "{}:{}".format(stop_i, max_repeat_after)


def leastInterval(taskQueue: List[str], n: int) -> int:
    """ """
    if n == 0 or len(taskQueue) == 1:
        return len(taskQueue)
    i = 0
    j = 0
    k = 0
    max_r = 65536
    taskQueue.sort()
    resultList = [taskQueue[i]]
    del taskQueue[i]
    while len(taskQueue) > 0:
        i, max_r = findMaxGroupAfter(taskQueue, max_r, i).split(":")
        i = int(i)
        max_r = int(max_r)
        k = 0
        canSet = True
        while len(resultList) > 0 and canSet and k < n and j - k >= 0:
            if taskQueue[i] == resultList[j - k]:
                canSet = False
            k += 1
        if canSet:
            resultList.append(taskQueue[i])
            del taskQueue[i]
            i = i - 1 if i > 0 else i
        else:
            if i + 1 >= len(taskQueue):
                resultList.append("idle")

        if i + 1 >= len(taskQueue) or canSet:
            j += 1
        if i + 1 >= len(taskQueue):
            max_r = 65536
            i = 0
        else:
            if len(taskQueue) == 2 and not canSet and i == 0:
                i = 1
    return len(resultList)


if __name__ == "__main__":
    unittest.main()
