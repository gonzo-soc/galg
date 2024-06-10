"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=mvejza05

Given condition
n  - pairs of parantheses

Idea:
Calculate Nth solution based on the n - 1 one: n = n - 1 + "(" + ")"
"""

import unittest
from typing import List


class TestSolution(unittest.TestCase):
    # @unittest.skip
    def test_simpleOne(self):
        result: List[str] = Solution().generateParenthesis(3)
        print("Check result")
        validResult: List[str] = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(result, validResult)

    # @unittest.skip
    def test_4Parantheses(self):
        """
        There is No
        "()(())()","((())())", "(()(()))"
        """
        result: List[str] = Solution().generateParenthesis(4)
        validResult = [
            "(((())))",
            "((()()))",
            "((())())",  # -
            "((()))()",
            "(()(()))",  # -
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",  # -
            "()()(())",
            "()()()()",
        ]
        print("Check result")
        self.assertCountEqual(result, validResult)

    def test_6Parantheses(self):
        validResult = [
            "(((((())))))",
            "((((()()))))",
            "((((())())))",
            "((((()))()))",
            "((((())))())",
            "((((()))))()",
            "(((()(()))))",
            "(((()()())))",
            "(((()())()))",
            "(((()()))())",
            "(((()())))()",
            "(((())(())))",
            "(((())()()))",
            "(((())())())",
            "(((())()))()",
            "(((()))(()))",
            "(((()))()())",
            "(((()))())()",
            "(((())))(())",
            "(((())))()()",
            "((()((()))))",
            "((()(()())))",
            "((()(())()))",
            "((()(()))())",
            "((()(())))()",
            "((()()(())))",
            "((()()()()))",
            "((()()())())",
            "((()()()))()",
            "((()())(()))",
            "((()())()())",
            "((()())())()",
            "((()()))(())",
            "((()()))()()",
            "((())((())))",
            "((())(()()))",
            "((())(())())",
            "((())(()))()",
            "((())()(()))",
            "((())()()())",
            "((())()())()",
            "((())())(())",
            "((())())()()",
            "((()))((()))",
            "((()))(()())",
            "((()))(())()",
            "((()))()(())",
            "((()))()()()",
            "(()(((()))))",
            "(()((()())))",
            "(()((())()))",
            "(()((()))())",
            "(()((())))()",
            "(()(()(())))",
            "(()(()()()))",
            "(()(()())())",
            "(()(()()))()",
            "(()(())(()))",
            "(()(())()())",
            "(()(())())()",
            "(()(()))(())",
            "(()(()))()()",
            "(()()((())))",
            "(()()(()()))",
            "(()()(())())",
            "(()()(()))()",
            "(()()()(()))",
            "(()()()()())",
            "(()()()())()",
            "(()()())(())",
            "(()()())()()",
            "(()())((()))",
            "(()())(()())",
            "(()())(())()",
            "(()())()(())",
            "(()())()()()",
            "(())(((())))",
            "(())((()()))",
            "(())((())())",
            "(())((()))()",
            "(())(()(()))",
            "(())(()()())",
            "(())(()())()",
            "(())(())(())",
            "(())(())()()",
            "(())()((()))",
            "(())()(()())",
            "(())()(())()",
            "(())()()(())",
            "(())()()()()",
            "()((((()))))",
            "()(((()())))",
            "()(((())()))",
            "()(((()))())",
            "()(((())))()",
            "()((()(())))",
            "()((()()()))",
            "()((()())())",
            "()((()()))()",
            "()((())(()))",
            "()((())()())",
            "()((())())()",
            "()((()))(())",
            "()((()))()()",
            "()(()((())))",
            "()(()(()()))",
            "()(()(())())",
            "()(()(()))()",
            "()(()()(()))",
            "()(()()()())",
            "()(()()())()",
            "()(()())(())",
            "()(()())()()",
            "()(())((()))",
            "()(())(()())",
            "()(())(())()",
            "()(())()(())",
            "()(())()()()",
            "()()(((())))",
            "()()((()()))",
            "()()((())())",
            "()()((()))()",
            "()()(()(()))",
            "()()(()()())",
            "()()(()())()",
            "()()(())(())",
            "()()(())()()",
            "()()()((()))",
            "()()()(()())",
            "()()()(())()",
            "()()()()(())",
            "()()()()()()",
        ]
        result: List[str] = Solution().generateParenthesis(6)
        print("Check result")
        self.assertCountEqual(result, validResult)
        # i = 0
        # j = 1
        # sortedResult = sorted(result)
        # while i < len(sortedResult):
        #     if i + 1 < len(sortedResult) and sortedResult[i] == sortedResult[i + 1]:
        #         print(
        #             "The string is duplicate: orig = "
        #             + sortedResult[i]
        #             + " duplicate: "
        #             + sortedResult[i + 1]
        #         )
        #     i += 1


class ParanthesesGenerator:
    def __init__(self, n: int):
        self.paranthesesMap: dict = {
            0: ["()"],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
        }
        for k in range(n):
            self.__calcFirstNthParentheses(k)

    def __isMirroredParentheses(parentheses: str) -> bool:
        """
        Mirror the list of parantheses
        :param parentheses: string of '(' or ')'
        :returns: if mirrored list
        """
        if len(parentheses) % 2 != 0:
            return False
        i: int = 0
        j: int = len(parentheses) - 1

        while i - 1 != j:
            if parentheses[i] == parentheses[j]:
                return False
            i += 1
            j -= 1

        return True

    def __mirrorParentheses(parentheses: List[str]) -> List[str]:
        """
        Mirror the list of parantheses
        :param parentheses: List of parantheses '(' or ')'
        :returns: mirrored list
        """
        i: int = len(parentheses) - 1
        reversedResult: str = ""
        while i >= 0:
            reversedResult += "(" if parentheses[i] == ")" else ")"
            i -= 1
        return reversedResult

    def __getNthParentheses(self, n: int) -> None:
        if n < 0 or n > 7:
            raise RuntimeError("Invalid n=[{!d}]".format(n))
        if n == 0:
            return self.paranthesesMap[n]
        n_minus_1_Parantheses: List[str] = self.paranthesesMap[n - 1]
        n_Parantheses: List[str] = []
        i: int = 0

        for s in n_minus_1_Parantheses:
            sList: List[str] = list(s)
            sList.insert(0, "(")
            i: int = 0
            while i < len(sList):
                if sList[i] == ")" or i == 0:
                    newSample = sList.copy()
                    newSample.insert(i + 1, ")")
                    newSample_str: str = "".join(newSample)
                    if newSample_str not in n_Parantheses:
                        n_Parantheses.append("".join(newSample))
                        if not ParanthesesGenerator.__isMirroredParentheses(newSample):
                            n_Parantheses.append(
                                ParanthesesGenerator.__mirrorParentheses(newSample)
                            )
                i += 1

        self.paranthesesMap[n] = n_Parantheses

    def __calcFirstNthParentheses(self, n: int) -> None:
        self.paranthesesMap.setdefault(n, self.__getNthParentheses(n))


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        generator: ParanthesesGenerator = ParanthesesGenerator(n)
        return generator.paranthesesMap[n - 1]


if __name__ == "__main__":
    unittest.main()
