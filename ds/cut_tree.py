#! /usr/bin/env python3.7


'''
Build a tree of cuts based on input length: can be useful for non-recursion version of merge sort.

Example 001.
Length = 4
    0, 4
    /   |
 0, 1  2, 3
'''

def init_tree(length):
    out_tree = {}

    medium_v = int(1 + length/2)
    out_tree['cut'] = "{},{}".format(1, length)
    out_tree['medium_v'] = medium_v
    out_tree['left'] = None
    out_tree['right'] = None

    return out_tree


def create_tree(left, right, curr_node):
    medium = int((left + right)/2)

    if left == right or (left == medium and left == 0):
        return curr_node
    elif right - medium == 1 and left == medium:
        return curr_node
    else:
        left_node = {}
        left_node['cut'] = "{}, {}".format(left + 1, medium + 1)
        left_node['left'] = None
        left_node['right'] = None
        curr_node['medium_v'] = medium + 1
        curr_node['left'] = left_node

    create_tree(left, medium, left_node)

    right_node = {}
    if left >= 0 and right - medium == 1:
        right_node['cut'] = "{}".format(right + 1)
    else:
        right_node['cut'] = "{}, {}".format(medium + 2, right + 1)

    right_node['left'] = None
    right_node['right'] = None
    curr_node['medium_v'] = medium + 1
    curr_node['right'] = right_node

    create_tree(medium + 1, right, right_node)
    return curr_node


def preorder_walk_tree(tree_root):
    print(tree_root['cut'])

    if tree_root['left'] is not None:
        preorder_walk_tree(tree_root['left'])

    if tree_root['right'] is not None:
        preorder_walk_tree(tree_root['right'])
    else:
        return None