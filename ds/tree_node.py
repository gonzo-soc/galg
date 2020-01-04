class Node:

    def __init__(self, in_key_v, parent=None):
        self.key_v = in_key_v
        self.parent = parent
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def set_left(self, left_node):
        self.left = left_node

    def get_right(self):
        return self.right

    def set_right(self, right_node):
        self.right = right_node

    def get_parent(self):
        return self.parent

    def set_parent(self, parent_node):
        self.parent = parent_node

    def get_key(self):
        return self.key_v

    def set_key(self, key_v):
        self.key_v = key_v