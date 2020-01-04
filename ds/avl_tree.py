from .tree_node import Node
from .bin_search_tree import BinTree
from .tree import Tree


class AVLNode(Node):

    def __init__(self, in_key_v, parent=None):
        Node.__init__(
            self,
            in_key_v,
            parent
        )
        self.height = 0

    def get_height(self):
        return self.height

    def set_height(self, in_height):
        self.height = in_height

    def increment_height(self):
        self.height += 1

    def get_diff(self):
        if self.get_left() is None and self.get_right() is None:
            return 0
        elif self.get_left() is not None and self.get_right() is None:
            return (-1) * self.get_left().height
        elif self.get_right() is not None and self.get_left() is None:
            return self.get_right().height
        else:
            return self.get_right().height - self.get_left().height


class AVLTree(Tree):

    def __init__(self, root_node):
        self.bin_tree = BinTree(root_node)

    @staticmethod
    def create_node(in_key_v, parent=None):
        return AVLNode(in_key_v, parent)

    def insert(self, new_node):
        new_node = self.bin_tree.insert(new_node)
        self.__increment_height__(new_node)
        new_root = self.__balance__(new_node)
        self.bin_tree.set_root(new_root)

    @staticmethod
    def __increment_height__(new_node):
        parent = new_node.get_parent()
        child = new_node
        while parent is not None:
            if parent.get_height() == child.get_height():
                parent.increment_height()
            child = parent
            parent = parent.get_parent()

    def __balance__(self, new_node):
        parent = new_node.get_parent()
        child = new_node

        while parent is not None:
            # left rotation
            if parent.get_diff() == 2:
                right_child = parent.get_right()
                # big left rotation
                if right_child.get_diff() < 0:
                    parent = self.__right_rotation__(right_child)
                parent = self.__left_rotation__(parent)
            # right rotation
            elif parent.get_diff() == -2:
                left_child = parent.get_left()
                # big right rotation
                if left_child.get_diff() > 0:
                    parent = self.__left_rotation__(left_child)
                parent = self.__right_rotation__(parent)

            child = parent
            parent = child.get_parent()

        return child

    @staticmethod
    def __left_rotation__(parent):
        right_child = parent.get_right()
        grand_pa = parent.get_parent()
        if right_child.get_left() is not None:
            left_right_child = right_child.get_left()
            parent.set_right(left_right_child)
            left_right_child.set_parent(parent)
        else:
            parent.get_right(None)

        if grand_pa is not None:
            right_child.set_parent(grand_pa)
            if grand_pa.get_left() == parent:
                grand_pa.set_left(right_child)
            elif grand_pa.get_right() == parent:
                grand_pa.set_right(right_child)

        right_child.set_left(parent)
        parent.set_parent(right_child)
        right_child.set_parent(grand_pa)
        AVLTree.__update_height__(parent)
        AVLTree.__update_height__(right_child)

        return right_child

    @staticmethod
    def __update_height__(in_node):
        left_height = -1
        if in_node.get_left() is not None:
            left_height = in_node.get_left().get_height()
        right_height = -1
        if in_node.get_right() is not None:
            right_height = in_node.get_right().get_height()

        if left_height > right_height:
            in_node.set_height(left_height + 1)
        else:
            in_node.set_height(right_height + 1)

    @staticmethod
    def __right_rotation__(parent):
        left_child = parent.get_left()
        grand_pa = parent.get_parent()
        if left_child.get_right() is not None:
            right_left_child = left_child.get_right()
            parent.set_left(right_left_child)
            right_left_child.set_parent(parent)
        else:
            parent.set_left(None)

        if grand_pa is not None:
            left_child.set_parent(grand_pa)
            if grand_pa.get_left() == parent:
                grand_pa.set_left(left_child)
            elif grand_pa.get_right() == parent:
                grand_pa.set_right(left_child)

        left_child.set_right(parent)
        parent.set_parent(left_child)
        left_child.set_parent(grand_pa)
        AVLTree.__update_height__(parent)
        AVLTree.__update_height__(left_child)

        return left_child
