#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from ds.avl_tree import *
from ds.tree import TreeWalker

if __name__ == '__main__':
    # Test 001: RR
    in_array = [7, 6, 9, 8, 10]
    length = len(in_array)

    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("\nTest #1 Right rotation")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Tree: ")
    TreeWalker.centered_walk(tree.get_root())

    # Test 002: BRR
    in_array = [7, 10, 3, 5, 4, 6]
    length = len(in_array)

    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("\nTest #2 Big Right rotation")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Tree: ")
    TreeWalker.centered_walk(tree.get_root())

    # Test #003 Left rotation
    in_array = [4, 3, 10, 7, 8]
    length = len(in_array)
    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("\nTest #3 Left rotation")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())

    # Test #004 Big Left rotation
    in_array = [5, 3, 2, 10, 6, 4, 11, 8, 7, 9]
    length = len(in_array)
    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("\nTest #4 Big Left rotation")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())

    # Test #005 Left-Leaf deletion
    in_array = [5, 3, 2, 10, 6, 4, 11, 8, 7, 9]
    length = len(in_array)
    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))
    print("\nTest #5 Left-leaf deletion: 2")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())
    tree.remove(2)
    TreeWalker.centered_walk(tree.get_root())

    # Test #006 Right-Leaf deletion
    in_array = [5, 3, 2, 10, 6, 4, 11, 8, 7, 9]
    length = len(in_array)
    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))
    print("\nTest #6 Right-leaf deletion: 4")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())
    tree.remove(4)
    TreeWalker.centered_walk(tree.get_root())

    # Test #007 Complex node deletion
    in_array = [5, 3, 2, 10, 6, 4, 11, 8, 7, 9]
    length = len(in_array)
    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))
    print("\nTest #7 Complex node deletion: 8")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())
    tree.remove(8)
    TreeWalker.centered_walk(tree.get_root())

    # Test #008 Complex root-node deletion
    in_array = [5, 3, 2, 10, 6, 4, 11, 8, 7, 9]
    length = len(in_array)
    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))
    print("\nTest #8 Complex root-node deletion: 5")
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())
    tree.remove(5)
    TreeWalker.centered_walk(tree.get_root())
