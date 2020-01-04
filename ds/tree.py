import abc
from .tree_node import Node


class Tree(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def create_node(in_key_v, parent=None):
        pass


class TreeWalker:

    @staticmethod
    def centered_walk(root):
        if not isinstance(root, Node):
            raise TypeError("Passed argument is not Node type")

        if root.left is not None:
            TreeWalker.centered_walk(root.get_left())
        print(root.key_v, end=" ")
        if root.right is not None:
            TreeWalker.centered_walk(root.get_right())
