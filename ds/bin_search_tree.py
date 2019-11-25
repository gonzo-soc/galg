class Node:

    def __init__(self, in_key_v, parent=None):
        self.key_v = in_key_v
        self.parent = parent
        self.left = None
        self.right = None


class BinTree:

    def __init__(self, in_array):
        self.root = Node(in_array[0])

        for i in range(1, len(in_array)):
            self.insert(in_array[i])

    def insert(self, in_key_v):
        curr_node = self.root
        new_node = Node(in_key_v)
        while curr_node:
            if in_key_v < curr_node.key_v:
                if curr_node.left is None:
                    curr_node.left = new_node
                    break
                else:
                    curr_node = curr_node.left
            elif in_key_v > curr_node.key_v:
                if curr_node.right is None:
                    curr_node.right = new_node
                    break
                else:
                    curr_node = curr_node.right

        new_node.parent = curr_node

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

    @staticmethod
    def __centered_walk(root):
        if root.left is not None:
            BinTree.__centered_walk(root.left)
        print(root.key_v, end=" ")
        if root.right is not None:
            BinTree.__centered_walk(root.right)

    def centered_walk(self):
        root_node = self.root
        BinTree.__centered_walk(root_node)

