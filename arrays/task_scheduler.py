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

    # def test_idle(self):
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

    def test_complexTwo(self):
        tasks: List[str] = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n: int = 1
        print("Tasks: {}, interval: {}".format(tasks, n))
        self.assertEqual(leastInterval(tasks, n), 12)

    # def test_complexThree(self):
    #     tasks: List[str] = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    #     n: int = 2
    #     print("Tasks: {}, interval: {}".format(tasks, n))
    #     self.assertEqual(leastInterval(tasks, n), 12)


def leastInterval(taskQueue: List[str], n: int) -> int:
    """ """
    if n == 0:
        return len(taskQueue)

    resultList = [taskQueue[0]]
    del taskQueue[0]
    
    taskQueue.sort()
    i = 1
    j = 1
    k = 0
    
    while (len(taskQueue) > 0):
        while(taskQueue[i] == resultList[j] and i < len(taskQueue)):
            i+=1
        
        if i == len(taskQueue):
            i = 0
        else: 
            k = 0
            canSet = True
            while canSet and k < n and j - k >= 0:
                if taskQueue[i] == resultList[j - k]:
                    canSet = False
                k+=1
            if (canSet):    
                resultList.append(taskQueue[i])
                del taskQueue[i]
                i+=1
            else:
                resultList.append("idle")
            j+=1
        
    return len(resultList)


if __name__ == "__main__":
    unittest.main()
