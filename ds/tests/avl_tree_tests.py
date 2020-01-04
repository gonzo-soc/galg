#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from ds.avl_tree import *
from ds.tree import TreeWalker

if __name__ == '__main__':
    in_array = [8, 9, 6, 5, 4, 7]
    length = len(in_array)

    tree = AVLTree(AVLTree.create_node(in_array[0]))
    for i in range(1, len(in_array)):
        tree.insert(tree.create_node(in_array[i]))

    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree)

    print("Remove [10]")
    tree.remove(10)
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree)

    print("Remove [14]")
    tree.remove(14)
    print("Sorted tree: ")
    TreeWalker.centered_walk(tree)
