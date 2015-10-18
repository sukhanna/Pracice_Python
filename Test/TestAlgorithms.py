__author__ = 'sukhanna'

# test stack algorithms
from Algorithm.StackAlgorithms import StackAlgorithms
from Algorithm.LinkList import List
from Algorithm.Recursion import is_palindrome
from Algorithm.Sort import Sort
from Algorithm.BinaryTreeAlgorithms import BinaryTreeAlgorithms
import time
import random

print("Paranthesis are balanced : ", StackAlgorithms.is_paranthesis_balanced('([{}])'))

# convert decimal number to base
print("Binary Value of 255 of base 2 is : ", StackAlgorithms.convert_to_base(255, 2))
print("Binary Value of 25 of base 16 is : ", StackAlgorithms.convert_to_base(25, 16))
print("Binary Value of 25 of base 8 is : ", StackAlgorithms.convert_to_base(25, 8))

# convert infix to pot fix
print("postfix of (A+B)*(C+D) is", StackAlgorithms.convert_infix_to_postfix("(A+B)*(C+D)"))
print("postfix of (A+B)*(C+D)*(E+F) is", StackAlgorithms.convert_infix_to_postfix("(A+B)*(C+D)*(E+F)"))
print("postfix of (A+B)*C is", StackAlgorithms.convert_infix_to_postfix("(A+B)*C"))
print("postfix of A*B+C is", StackAlgorithms.convert_infix_to_postfix("A*B+C"))
print("postfix of (A+B+C+D)/C is", StackAlgorithms.convert_infix_to_postfix("(A+B+C+D)/C"))
print("postfix of A+B*C is", StackAlgorithms.convert_infix_to_postfix("A+B*C"))

# evaluate post fix expression
print("evaluation result of postfix expression 56*7+ is", StackAlgorithms.evaluate_postfix_expression("56*7+"))
print("evaluation result of postfix expression 56*76++ is", StackAlgorithms.evaluate_postfix_expression("56*76++"))

# testing linked list
l = List()
for item in range(10):
    l.add(item)
l.printList()

# insert new item to the list
l.insert(11, 3)
print('\nlist after insert operation')
l.printList()

# insert new item to the list
l.insert(100, 4)
print('\nlist after insert operation')
l.printList()

# test for palindromes
print(is_palindrome("radar", len("radar")))
print(is_palindrome("heloo", len("heloo")))
print(is_palindrome("abcdefghijkl", len("abcdefghijkl")))

# test for quick sort
random_list = random.sample(range(100), 100)
t1 = time.time()
Sort.quick_sort1(random_list, 0, len(random_list)-1, 0)
t2 = time.time()
print(random_list)
print("time in seconds %d" %(t2-t1))

#test for binary tree : building expression trees
tree = BinaryTreeAlgorithms.build_expression_tree("( ( 10 + 5 ) * 3 )")

print("--------print_in_order tree expression")
print(BinaryTreeAlgorithms.print_in_order(tree))

print("--------Post order evaluation---------------")
print(BinaryTreeAlgorithms.post_order_evaluate(tree))

tree = BinaryTreeAlgorithms.build_expression_tree("( a + ( ( b - c ) * d )")
print("----------------Pre Order---------------------")
BinaryTreeAlgorithms.pre_order(tree)

print("----------------Post Order---------------------")
BinaryTreeAlgorithms.post_order(tree)