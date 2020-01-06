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

    def find_min_after(self, less_than_key):
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
                rem_node.right.parent = parent_node
        else:
            min_after_key = self.bin_tree.find_min_after(key_v)
            if min_after_key.parent != rem_node:
                if min_after_key.right is not None:
                    min_after_key.parent.left = min_after_key.right
                    min_after_key.right.parent = min_after_key.parent
                else:
                    min_after_key.parent.left = None
                min_after_key.right = rem_node.right
                rem_node.right.parent = min_after_key

            if parent_node.left == rem_node:
                parent_node.left = min_after_key
            else:
                parent_node.right = min_after_key

            min_after_key.parent = rem_node.parent
            if rem_node.left is not None:
                min_after_key.left = rem_node.left
                rem_node.left.parent = min_after_key

        return parent_node


