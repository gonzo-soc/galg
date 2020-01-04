from .tree_node import Node
from .tree import Tree


class BinTree(Tree):

    def __init__(self, root_node):
        self.root = root_node

    @staticmethod
    def create_node(in_key_v, parent=None):
        return Node(in_key_v, parent)

    def insert(self, new_node):
        curr_node = self.root
        new_key_v = new_node.get_key()
        while curr_node:
            if new_key_v < curr_node.key_v:
                if curr_node.left is None:
                    curr_node.left = new_node
                    break
                else:
                    curr_node = curr_node.left
            elif new_key_v > curr_node.key_v:
                if curr_node.right is None:
                    curr_node.right = new_node
                    break
                else:
                    curr_node = curr_node.right

        new_node.set_parent(curr_node)
        return new_node

    def get_root(self):
        return self.root

    def set_root(self, new_root):
        self.root = new_root

    def __after_that(self, less_than_key):
        successor = None
        current = self.root
        while current:
            if current.key_v <= less_than_key:
                current = current.right
            elif current.key_v > less_than_key:
                successor = current
                current = current.left
        return successor

    def remove(self, key_v):
        rem_node = self.root
        while rem_node and rem_node.key_v != key_v:
            if key_v < rem_node.key_v:
                rem_node = rem_node.left
            elif key_v > rem_node.key_v:
                rem_node = rem_node.right

        parent_node = rem_node.parent
        if rem_node.left is None and rem_node.right is None:
            if parent_node.left == rem_node:
                parent_node.left = None
            else:
                parent_node.right = None
        elif rem_node.left and rem_node.right is None:
            if parent_node.left == rem_node:
                parent_node.left = rem_node.left
                rem_node.left.parent = parent_node
            else:
                parent_node.right = rem_node.left
                rem_node.left.parent = parent_node
        elif rem_node.right and rem_node.left is None:
            if parent_node.left == rem_node:
                parent_node.left = rem_node.right
                rem_node.right.parent = parent_node
            else:
                parent_node.right = rem_node.right
                rem_node.left.parent = parent_node
        else:
            after_rem_node = self.__after_that(key_v)
            rem_node.key_v = after_rem_node.key_v
            if after_rem_node.parent != rem_node:
                if after_rem_node.right is not None:
                    after_rem_node.parent.left = after_rem_node.right
                    after_rem_node.right = after_rem_node.parent
                else:
                    after_rem_node.parent.left = None
            else:
                rem_node.right = after_rem_node.right
                after_rem_node.right.parent = rem_node

        return parent_node


