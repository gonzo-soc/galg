#! /usr/bin/env python3.7

from os import environ
from sys import path

path.append(environ['HOME'] + '/Workspace/Sys/pycharm_projs/galg/')
path.append('.')
path.append('..')

from ds.cut_tree import *
from array import array

if __name__ == '__main__':
    in_array = array('i', [1, 2, 3, 4, 5, 6])
    length = len(in_array)
    TREE_ROOT = init_tree(length)
    curr_root = create_tree(0, length - 1, TREE_ROOT)

    preorder_walk_tree(TREE_ROOT)

    in_array = array('i', [1, 2, 3])
    length = len(in_array)
    TREE_ROOT = init_tree(length)
    curr_root = create_tree(0, length - 1, TREE_ROOT)

    preorder_walk_tree(TREE_ROOT)

    in_array = array('i', [1, 2, 3, 4, 5, 6, 7])
    length = len(in_array)
    TREE_ROOT = init_tree(length)
    curr_root = create_tree(0, length - 1, TREE_ROOT)
