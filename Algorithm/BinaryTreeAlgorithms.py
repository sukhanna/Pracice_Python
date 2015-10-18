__author__ = 'sukhanna'

from DataStructures.Stack import Stack
from DataStructures.BinaryTree import BinaryTree
from Algorithm.StackAlgorithms import StackAlgorithms

class BinaryTreeAlgorithms:

    # evaluate expressions using Binary Tree and stack to keep track of parent
# 3+4*6
    @staticmethod
    def build_expression_tree(expression):
        exp_list = expression.split()
        stack = Stack()
        tree = BinaryTree('')
        stack.push(tree)
        current_tree = tree
        for item in exp_list:
            if item == '(':
                current_tree.insert_left('')
                stack.push(current_tree)
                current_tree = current_tree.get_left()
            elif item not in ['+', '-', '/', '*', ')']:
                current_tree.set_root(item)
                parent = stack.pop()
                current_tree = parent
            elif item in ['+', '-', '/', '*']:
                current_tree.set_root(item)
                current_tree.insert_right('')
                stack.push(current_tree)
                current_tree = current_tree.get_right()
            elif item == ')':
                current_tree = stack.pop()
            else:
                raise ValueError

        return tree

    @staticmethod
    def pre_order(tree):
        if tree:
            print(tree.get_root())
            BinaryTreeAlgorithms.pre_order(tree.get_left())
            BinaryTreeAlgorithms.pre_order(tree.get_right())

    @staticmethod
    def post_order(tree):
        if tree:
            BinaryTreeAlgorithms.post_order(tree.get_left())
            BinaryTreeAlgorithms.post_order(tree.get_right())
            print(tree.get_root())

    @staticmethod
    def post_order_evaluate(tree):
        res1 = None
        res2 = None

        if tree:
            res1 = BinaryTreeAlgorithms.post_order_evaluate(tree.get_left())
            res2 = BinaryTreeAlgorithms.post_order_evaluate(tree.get_right())

            if res1 and res2:
                return StackAlgorithms.evaluate_expression((int)(res1), (int)(res2), tree.get_root())
            else:
                return tree.get_root()

    @staticmethod
    def print_in_order(tree):
        string_value = ""
        if tree:
            res1 = BinaryTreeAlgorithms.print_in_order(tree.get_left())
            if res1:
                string_value = "(" + res1
            string_value = string_value + tree.get_root()
            res2 = BinaryTreeAlgorithms.print_in_order(tree.get_right())
            if res2:
                string_value = string_value + res2 + ")"
        return string_value