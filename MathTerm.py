from Calculator import MathSegmentClass
from Calculator import math_operator_types, math_operation_dictionary


class MathTermClass(MathSegmentClass):
    def __init__(self, number, operator):
        super(MathTermClass, self).__init__(operator)
        if type(number) is str:
            number = float(number)
        self.number = number

    def __str__(self):
        string = str(self.number)
        if self.operator:
            string += self.operator
        return string

    def CalculateWith(self, right_term) -> 'MathTermClass':
        right_term: MathTermClass
        if right_term is None and self.operator is None:
            return self.number
        if self.operator in math_operator_types:
            result = math_operation_dictionary[self.operator](self.number, right_term.number)
            return MathTermClass(result, right_term.operator)
        else:
            raise Exception("operator '{}' is not customizes to use calculate".format(self.operator))

    @classmethod
    def CreateTermFromText(cls, text) -> 'MathTermClass':
        index = 0
        if text[index] == '-' or text[index] == '+':
            index += 1
        period_used = False
        while index < len(text) and (text[index].isdigit() or (not period_used and text[index] == '.')):
            if text[index] == '.' and not period_used:
                period_used = True
            index += 1

        if index == 0:
            raise Exception("could not find number in text '{}'".format(text))

        if index < len(text) and text[index] in math_operator_types:
            return cls(text[:index], text[index])

        return cls(text[:index], None)
