#! /usr/bin/env python3.7

"""
621. Task scheduler
https://leetcode.com/problems/task-scheduler/description/

"""

import unittest
from typing import List


class TestLeastInterval(unittest.TestCase):
    def test_idle(self):
        tasks: List[str] = ["A", "A", "A", "B", "B", "B"]
        n: int = 2
        print("Tasks: {}, interval: {}".format(tasks, n))
        self.assertEqual(leastInterval(tasks, n), 8)

def leastInterval(tasks: List[str], n: int) -> int:
    '''
    '''
    resultList = [tasks[0]]
    tasksCopy = tasks.copy()
    tasksCopy[0] = -1

    j = 1
    i = 1
    processed = 1
    canSet = True

    while processed != len(tasks):
        while tasksCopy[i] == -1:
            i += 1

        k = 1
        idle = False
        canSet = True
        while k < n and j - k >= 0:
            if resultList[j - k] == tasks[i]:
                canSet = False
            k += 1
        if canSet:
            resultList.append(tasks[i])
            tasksCopy[i] = -1
            processed += 1

        i += 1
        if i == len(tasks):
            i = 0
            if not canSet:
                idle = True
                resultList.append("idle")
        if idle or canSet:
            j += 1

    return len(resultList)


if __name__ == "__main__":
    unittest.main()
