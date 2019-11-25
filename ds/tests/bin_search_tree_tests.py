#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from ds.bin_search_tree import *

if __name__ == '__main__':
    in_array = [7, 5, 6, 4, 2, 3, 14, 10, 9, 11, 15, 16, 13]
    length = len(in_array)

    tree = BinTree(in_array)
    print("Income array: " + " ".join(map(str, in_array)))
    print("Sorted tree: ")
    tree.centered_walk()

    print("Remove [10]")
    tree.remove(10)
    print("Sorted tree: ")
    tree.centered_walk()

    print("Remove [14]")
    tree.remove(14)
    print("Sorted tree: ")
    tree.centered_walk()
