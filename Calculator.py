from Calculator.MathTerm import MathTermClass
from Calculator import MathSegmentClass
from Calculator import math_operator_order, math_operator_types


class MathExpressionClass(MathSegmentClass):
    def __init__(self, text: str):
        super().__init__(None)
        self.segments = []
        i = 0
        while i < len(text):

            if text[i] == ')':
                return
            if text[i] == '(':
                new_expression = MathExpressionClass(text[i + 1:])
                par_count = 1 + new_expression._countNestedExpressions()
                for _ in range(par_count):
                    i = text.find(')', i + 1) + 1
                if i < 0:
                    raise Exception("no closing parentheses in text '{}'".format(text))
                if i < len(text) and text[i] in math_operator_types:
                    new_expression.operator = text[i]
                    i += 1
                self.segments.append(new_expression)
                continue

            new_term = MathTermClass.CreateTermFromText(text[i:])
            self.segments.append(new_term)
            if new_term.operator is None:
                return
            else:
                i = text.find(new_term.operator, i + 1) + 1

        if self.segments[-1].operator is not None:
            raise Exception("no number or expression found after operator - '{}' in text '{}'"
                            .format(self.segments[-1].operator, text))

    def __str__(self):
        string = ""
        for seg in self.segments:
            if type(seg) is MathExpressionClass:
                string += '(' + str(seg) + ')'
                if seg.operator:
                    string += seg.operator
            else:
                string += str(seg)
        return string

    def Solve(self) -> float:
        if len(self.segments) == 0:
            return 0

        index = 0
        while index < len(self.segments):
            if type(self.segments[index]) is MathExpressionClass:
                result_number = self.segments[index].Solve()
                self.segments[index] = MathTermClass(result_number, self.segments[index].operator)
            index += 1

        for highest_order_operators in math_operator_order:
            index = 0
            while index < len(self.segments):
                if self.segments[index].operator in highest_order_operators:
                    self.CalculateTermAtIndex(index)
                    index -= 1
                index += 1

        if len(self.segments) == 1:
            return self.segments[0].number
        else:
            raise Exception("missing operator in expression '{}'".format(self))

    def CalculateTermAtIndex(self, index: int) -> None:
        if index >= len(self.segments):
            raise Exception("index out of bounds index={} in expression '{}'".format(index, self))
        if index + 1 == len(self.segments):
            raise Exception("no term after '{}' in segments '{}'".format(self.segments[index], self.segments))

        left_seg = self.segments[index]
        right_seg = self.segments[index + 1]
        result = left_seg.CalculateWith(right_seg)
        self.segments[index] = result
        del self.segments[index + 1]

    def _countNestedExpressions(self) -> int:
        times = 0
        for seg in self.segments:
            if type(seg) is MathExpressionClass:
                seg: MathExpressionClass
                times += seg._countNestedExpressions() + 1
        return times
