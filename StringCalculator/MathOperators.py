def Add(left_number, right_number):
    return left_number + right_number


def Subtract(left_number, right_number):
    return left_number - right_number


def Divide(left_number, right_number):
    return left_number / right_number


def Multiply(left_number, right_number):
    return left_number * right_number


def Exponent(left_number, right_number):
    return left_number ** right_number


def Root(left_number, right_number):
    return Exponent(right_number, 1.0 / left_number)


math_operation_dictionary = {
    '^': Exponent,
    'V': Root,
    '*': Multiply,
    '/': Divide,
    '+': Add,
    '-': Subtract
}
math_operator_types = [operator for operator in math_operation_dictionary.keys()]
math_operator_order = [
    ['^', 'V'],
    ['*', '/'],
    ['+', '-']
]
