#! /usr/bin/env python3.7

"""
767. Reorganize String
https://leetcode.com/problems/reorganize-string/

"""

import unittest
from typing import List


class TestReorginzeString(unittest.TestCase):
    @unittest.skip
    def test_simpleOne(self):
        # aLine: str = "aabbccdeeeeffffffff"
        aLine: str = "aaaab"
        solution = Solution()
        self.assertEqual(solution.reorganizeString(aLine), "")

    # @unittest.skip
    def test_simpleTwo(self):
        # aLine: str = "aabbccdeeeeffffffff"
        aLine: str = "abcdef"
        solution = Solution()
        self.assertEqual(solution.reorganizeString(aLine), "abcdef")

    @unittest.skip
    def test_strongOne(self):
        aLine: str = "dababcceeeefffff"
        solution = Solution()
        self.assertEqual(solution.reorganizeString(aLine), "feabcdfeabcfefef")

    @unittest.skip
    def test_simpleThree(self):
        aLine: str = "aab"
        solution = Solution()
        self.assertEqual(solution.reorganizeString(aLine), "aba")

    # @unittest.skip
    def test_simpleFourth(self):
        aLine: str = "lovmvmmvvvv"
        solution = Solution()
        self.assertEqual(solution.reorganizeString(aLine), "vlvov")

class Solution:

    def __buildMostFrequentSymbolList(sortedLine: str) -> List[str]:
        """
        build list: list[i] = <symbol:frequent>
        """
        if len(sortedLine) == 1:
            return ["{}:{}".format(sortedLine[0], 1)]

        stopIndex = i = 0
        currSz = maxGr = 1
        mostFrequentSymbolList: List[str] = []
        while len(sortedLine) > 0:
            if i + 1 < len(sortedLine):
                if sortedLine[i] == sortedLine[i + 1]:
                    currSz += 1
                else:
                    currSz = 1
                if maxGr < currSz:
                    maxGr = currSz
                    stopIndex = i
                i += 1
            else:
                lastSingleItem: bool = i + 1 == len(sortedLine) and len(sortedLine) == 1
                if lastSingleItem:
                    stopIndex = 0
                i = 0
                mostFrequentSymbolList.append(
                    ":".join([sortedLine[stopIndex], str(maxGr)])
                )
                sortedLine = sortedLine.replace(sortedLine[stopIndex], "")
                currSz = maxGr = 1
                stopIndex = 0

        return mostFrequentSymbolList

    def checkAndDemoteKey(frequentSymbolList: List[str], pos: int, actingFrequent: int):
        j = pos + 1
        newPos = -1
        while j < len(frequentSymbolList):
            currFrequent = int(frequentSymbolList[j].split(":")[1])
            if currFrequent > actingFrequent:
                newPos = j
                j += 1
            else:
                break

        if newPos >= 0:
            # swap keys
            temp = frequentSymbolList[newPos]
            frequentSymbolList[newPos] = frequentSymbolList[pos]
            frequentSymbolList[pos] = temp

    def reorganizeString(self, s: str) -> str:
        if len(s) < 3:
            return s

        reorganizeString: str = ""
        mostFrequentSymbolList: List[str] = Solution.__buildMostFrequentSymbolList(
            "".join(sorted(s))
        )

        while len(mostFrequentSymbolList) > 1:
            topSymbol = mostFrequentSymbolList[0].split(":")[0]
            topFrequent = int(mostFrequentSymbolList[0].split(":")[1])
            topFrequent -= 1
            nextAfterTopSymbol = mostFrequentSymbolList[1].split(":")[0]
            nextAfterTopFrequent = int(mostFrequentSymbolList[1].split(":")[1])
            nextAfterTopFrequent -= 1

            reorganizeString = reorganizeString + topSymbol + nextAfterTopSymbol
            mostFrequentSymbolList[0] = ":".join([topSymbol, str(topFrequent)])
            mostFrequentSymbolList[1] = ":".join(
                [nextAfterTopSymbol, str(nextAfterTopFrequent)]
            )
            if nextAfterTopFrequent != 0:
                Solution.checkAndDemoteKey(
                    mostFrequentSymbolList, 1, nextAfterTopFrequent
                )
            else:
                del mostFrequentSymbolList[1]
            if topFrequent != 0:
                Solution.checkAndDemoteKey(mostFrequentSymbolList, 0, topFrequent)
            else:
                del mostFrequentSymbolList[0]

        if len(mostFrequentSymbolList) == 1:
            balance = mostFrequentSymbolList[0].split(":")
            if int(balance[1]) > 1:
                return ""
            else:
                return reorganizeString + balance[0]
        return reorganizeString


if __name__ == "__main__":
    unittest.main()
