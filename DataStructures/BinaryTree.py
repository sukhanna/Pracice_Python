__author__ = 'sukhanna'


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, node):
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def pre_order(self):
        print(self.root)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.root)