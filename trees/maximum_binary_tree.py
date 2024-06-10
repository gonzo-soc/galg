#! /usr/bin/env python3.7

"""
654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/description

"""

import unittest
from typing import List, Optional


class TestSolution(unittest.TestCase):
    @unittest.skip
    def test_simpleOne(self):
        aNums: List[int] = [1, 0, 3]
        mbt_root: Optional[TreeNode] = Solution().constructMaximumBinaryTree(aNums)
        self.assertEqual(True, True)

    # @unittest.skip
    def test_simpleTwo(self):
        aNums: List[int] = [2, 0, 1, 5, 6]
        mbt_root: TreeNode = Solution().constructMaximumBinaryTree(aNums)
        self.assertEqual(True, True)


class TreeNode:
    def __init__(self, val: int = -1, index: int = -1, left=None, right=None):
        self.val = val
        self.index = index
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def __findMaximumValueIndex(nums: List[int], start_i: int, end_i: int) -> int:
        if start_i == end_i:
            return end_i
        i: int = start_i
        max_v: int = -1
        max_value_i: int = -1
        while i <= end_i and i < len(nums):
            if nums[i] > max_v:
                max_v = nums[i]
                max_value_i = i
            i += 1
        return max_value_i

    def __buildMaximumBinaryTree(
        last_added: TreeNode, nums: List[int], start_i: int, end_i: int
    ) -> None:
        max_value_i: int = Solution.__findMaximumValueIndex(nums, start_i, end_i)

        if last_added.val < 0:  # root
            last_added.val = nums[max_value_i]
            last_added.index = max_value_i
        else:
            if max_value_i < last_added.index:
                last_added.left = TreeNode(nums[max_value_i], max_value_i)
                last_added = last_added.left
            else:
                last_added.right = TreeNode(nums[max_value_i], max_value_i)
                last_added = last_added.right

        if start_i == end_i:
            return

        if start_i != max_value_i:
            Solution.__buildMaximumBinaryTree(last_added, nums, start_i, max_value_i - 1)

        if max_value_i != end_i:
            Solution.__buildMaximumBinaryTree(last_added, nums, max_value_i + 1, end_i)

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        root:TreeNode = TreeNode()
        Solution.__buildMaximumBinaryTree(root, nums, 0, len(nums) - 1)
        return root


if __name__ == "__main__":
    unittest.main()
