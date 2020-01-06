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
        parent = new_node.get_parent()
        self.__balance__(parent)

    def remove(self, key_v):
        rem_node = self.get_root()
        while rem_node and rem_node.key_v != key_v:
            if key_v < rem_node.key_v:
                rem_node = rem_node.left
            elif key_v > rem_node.key_v:
                rem_node = rem_node.right

        parent_node = rem_node.parent
        start_balance_node = parent_node
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
                start_balance_node = min_after_key.parent
            else:
                start_balance_node = min_after_key

            if parent_node.left == rem_node:
                parent_node.left = min_after_key
            else:
                parent_node.right = min_after_key

            min_after_key.parent = rem_node.parent
            if rem_node.left is not None:
                min_after_key.left = rem_node.left
                rem_node.left.parent = min_after_key

        self.__balance__(start_balance_node)

    def __balance__(self, parent):
        child = parent
        is_root_rotation = False
        while parent is not None and AVLTree.__update_height__(parent):
            if (parent.get_diff() == -2 or parent.get_diff() == 2) and parent == self.get_root():
                is_root_rotation = True

            # left rotation
            if parent.get_diff() == 2:
                right_child = parent.get_right()
                # big left rotation
                if right_child.get_diff() < 0:
                    self.__right_rotation__(right_child)
                    AVLTree.__update_height__(right_child)
                    AVLTree.__update_height__(right_child.get_parent())

                self.__left_rotation__(parent)
            # right rotation
            elif parent.get_diff() == -2:
                left_child = parent.get_left()
                # big right rotation
                if left_child.get_diff() > 0:
                    self.__left_rotation__(left_child)
                    AVLTree.__update_height__(left_child)
                    AVLTree.__update_height__(left_child.get_parent())

                self.__right_rotation__(parent)
            else:
                child = parent
                parent = parent.get_parent()

        if is_root_rotation:
            if parent is not None:
                self.bin_tree.set_root(parent)
            else:
                self.bin_tree.set_root(child)

    @staticmethod
    def __left_rotation__(parent):
        right_child = parent.get_right()
        grand_pa = parent.get_parent()
        if right_child.get_left() is not None:
            left_right_child = right_child.get_left()
            parent.set_right(left_right_child)
            left_right_child.set_parent(parent)
        else:
            parent.set_right(None)

        if grand_pa is not None:
            right_child.set_parent(grand_pa)
            if grand_pa.get_left() == parent:
                grand_pa.set_left(right_child)
            elif grand_pa.get_right() == parent:
                grand_pa.set_right(right_child)

        right_child.set_left(parent)
        parent.set_parent(right_child)
        right_child.set_parent(grand_pa)

        return right_child

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

        return left_child

    @staticmethod
    def __update_height__(in_node):
        old_height = in_node.get_height()
        left_height = -1
        if in_node.get_left() is not None:
            left_height = in_node.get_left().get_height()
        right_height = -1
        if in_node.get_right() is not None:
            right_height = in_node.get_right().get_height()

        if left_height > right_height:
            in_node.set_height(left_height + 1)
        elif right_height >= left_height:
            in_node.set_height(right_height + 1)

        return old_height != in_node.get_height()

    def get_root(self):
        return self.bin_tree.get_root()
