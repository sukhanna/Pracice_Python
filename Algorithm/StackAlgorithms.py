__author__ = 'sukhanna'

from DataStructures.Stack import Stack

class StackAlgorithms:

    # check balanced paranthesis
    @staticmethod
    def is_paranthesis_balanced(symbol_string):
        s = Stack()
        index = 0
        balanced = True
        length = len(symbol_string)
        while index < length and balanced:
            symbol = symbol_string[index]
            if symbol in "({[":
                s.push(symbol)
            else:
                if s.is_empty():
                    balanced = False
                else:
                    start = s.pop()
                    if not StackAlgorithms.matches(start, symbol):
                        balanced = False


            index += 1

        if s.is_empty() and balanced:
            return True
        else:
            return False

    @staticmethod
    def matches(start, end):
        try:
            starts = "([{"
            ends = ")]}"
            return starts.index(start) == ends.index(end)
        except:
            print("Exception")


# convert decimal to binary

    # convert number to it base
    @staticmethod
    def convert_to_base(dividend, base):
        s = Stack()
        hexadecimal = "0123456789ABCDEF"
        while dividend > 0:
            s.push(dividend % base)
            dividend //= base;

        length = s.size()
        binary = ""
        while length > 0:
            binary += str(hexadecimal[s.pop()])
            length -= 1

        return binary


    # convert infix to postfix
    @staticmethod
    def convert_infix_to_postfix(infix_expression):
        operator_dictionary = {"+":2, "-":2, "/":3, "*":3, "(":1}
        operator_stack = Stack()
        postfix_list = []
        index = 0

        while index < len(infix_expression):
            token = infix_expression[index];
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
            token in "0123456789":
                postfix_list.append(token)
            elif token == '(':
                operator_stack.push('(')
            elif token == ")":
                top_token = operator_stack.pop()
                while top_token != "(":
                    postfix_list.append(top_token)
                    top_token = operator_stack.pop()
            else:
                while not operator_stack.is_empty() and \
                operator_dictionary[operator_stack.peek()] >= operator_dictionary[token]:
                    postfix_list.append(operator_stack.pop())
                operator_stack.push(token)

            index += 1

        #return postfix expression
        while not operator_stack.is_empty():
            postfix_list.append(operator_stack.pop())
        return "".join(postfix_list)

    # evaluate postfix expression
    @staticmethod
    def evaluate_postfix_expression(postfix_expression):
        expression_stack = Stack()
        index = 0
        while index < len(postfix_expression):
            token = postfix_expression[index]
            if token in "0123456789":
                expression_stack.push(int(token))
            else:
                second = expression_stack.pop()
                first = expression_stack.pop()
                result = StackAlgorithms.evaluate_expression(first, second, token)
                expression_stack.push(result)

            index += 1

        return expression_stack.pop()

    @staticmethod
    def evaluate_expression(first, second, operator):
        if second > first:
            first = second - first
            second = second - first
            first = second + first

        if operator == "*":
            return first * second
        elif operator == "/":
            return first / second
        elif operator == "+":
            return first + second
        else:
            first - second










