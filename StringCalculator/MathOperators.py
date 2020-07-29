import math


def Add(left_number, right_number):
    return left_number + right_number


def Subtract(left_number, right_number):
    return left_number - right_number


def Divide(left_number, right_number):
    return left_number / right_number


def Multiply(left_number, right_number):
    return left_number * right_number


def Exponent(left_number, right_number):
    try:
        return left_number ** right_number
    except OverflowError:
        return math.inf


def Root(left_number, right_number):
    return Exponent(right_number, 1.0 / left_number)


math_operation_dictionary = {
    '^': Exponent,
    'V': Root,
    'v': Root,
    '*': Multiply,
    'x': Multiply,
    'X': Multiply,
    '/': Divide,
    '\\': Divide,
    '÷': Divide,
    '+': Add,
    '-': Subtract
}
math_operator_types = [operator for operator in math_operation_dictionary.keys()]
math_operator_order = [
    ['^', 'V', 'v'],
    ['*', 'x', 'X', '/', '\\', '÷'],
    ['+', '-']
]
