#! /usr/bin/env python3.7

"""
687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/description/

"""

import unittest


class TestReorginzeString(unittest.TestCase):
    def test_simpleOne(self):
        aLine: str = "aaaab"
        self.assertEqual(aLine, "aaaab")


class Node:
    def __init__(self, aSymbol: str, aFrequent: int):
        self.__symbol = aSymbol
        self.__frequent = aFrequent
        self.__left: Node = None
        self.__right: Node = None
        self.__sibling: Node = None

    def getFrequent(self) -> int:
        return self.__frequent

    def getSymbol(self) -> str:
        return self.__symbol

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def getSibling(self):
        return self.__sibling

    def setLeft(self, aNode):
        self.__left = aNode

    def setRight(self, aNode):
        self.__right = aNode

    def setSibling(self, aNode):
        self.__sibling = aNode

    def setFrequent(self, aFrequent):
        self.__frequent = aFrequent


class FrequentTree:
    reorganizeString: str = ""

    def __init__(self, line: str):
        self.__root: Node = None
        sortedLine: str = sorted(line)
        currFrequent = 1
        i = 0
        while i < len(sortedLine):
            currSymbol = sortedLine[i]
            if i + 1 < len(sortedLine) and currSymbol == sortedLine[i + 1]:
                currFrequent = currFrequent + 1
            else:
                if self.__root is None:
                    self.__root = Node(currSymbol, currFrequent)
                else:
                    FrequentTree.addNode(self.__root, currSymbol, currFrequent)
                currFrequent = 1
            i = i + 1

    def addNode(aNode: Node, aSymbol: str, aFrequent: int) -> bool:
        if aNode is None:
            return True
        if aNode.getFrequent() > aFrequent:
            if FrequentTree.addNode(aNode.getLeft(), aSymbol, aFrequent):
                aNode.setLeft(Node(aSymbol, aFrequent))
        else:
            if aNode.getFrequent() < aFrequent:
                if FrequentTree.addNode(aNode.getRight(), aSymbol, aFrequent):
                    aNode.setRight(Node(aSymbol, aFrequent))
            else:
                if aNode.getFrequent() == aFrequent and aNode.getSymbol() != aSymbol:
                    curr = aNode
                    aSibling = Node(aSymbol, aFrequent)
                    while curr.getSibling() is not None:
                        curr = curr.getSibling()
                        if curr.getSymbol() == aSymbol:
                            # already exists in siblings
                            break
                    curr.setSibling(aSibling)
                    return False

    def removeNode(self, aNode: Node):
        # if root
        if aNode == self.__root:
            leftChild = self.__root.getLeft()
            rightChild = self.__root.getRight()
            if rightChild is not None:
                if rightChild.getRight() is not None:
                    rightLeftChild = rightChild.getRight().getLeft()
                    if rightLeftChild is not None and rightChild.getLeft() is not None:
                        curr = rightLeftChild
                        while curr.getLeft() is not None:
                            curr = curr.getLeft()
                        curr.setLeft(rightLeftChild)
                    if leftChild is not None:
                        rightChild.setLeft(leftChild)

                self.__root = rightChild
            else:
                if leftChild is not None:
                    self.__root = leftChild
        else:
            # if it is not a leaf
            if aNode.getLeft() is not None or aNode.getRight() is not None:
                raise Exception("Unpredictable behavior")
            else:
                # if leaf
                parent = aNode.getParent()
                if parent.getLeft() == aNode:
                    parent.setLeft(None)
                else:
                    parent.setLeft(None)

    def print(aNode: Node):
        resultString: str = aNode.getSymbol()
        frequent = aNode.getFrequent() - 1
        aNode.setFrequent(frequent)
        curr: Node = aNode.getSibling()
        while curr is not None:
            resultString = resultString + curr.getSymbol()
            frequent = curr.getFrequent() - 1
            curr.setFrequent(frequent)
            curr = curr.getSibling()
        return resultString
