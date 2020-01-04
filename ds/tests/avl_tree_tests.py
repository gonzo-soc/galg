#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from ds.avl_tree import *
from ds.tree import TreeWalker

if __name__ == '__main__':
    # big right rotation
    in_array = [7, 8, 1, 5, 4]
    length = len(in_array)

    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())

    # right rotation
    in_array = [8, 9, 6, 5, 4, 7]
    length = len(in_array)

    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree.get_root())
