from StringCalculator import SolveMathProblem
from StringCalculator.Calculator import MathExpressionClass


exp_texts = [
    # "10^308+10^308",
    # "1+(1)",
    # "2*6",
    # "-9+3",
    # "+35419.55619-6",
    # "5*.25/9-6",
    # "-59*-.25/-9-6",
    # "5^(2*6)-3V27^3",
    ["(1/6)-1^(2*6)",-5/6],
    ["((48*83)+(73*42))/2",3525.0],
    ["1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 1 + 0 + 0 + 1 + 1 + 1 + 2 + 3 + 3 + 2 + 2 +    1",28.0],
]
i = 0
for text in exp_texts:
    i += 1
    print()
    print()
    print("exp_text{} ---------".format(i))
    expRes = exp_texts[i-1]
    exp = expRes[0]
    neededResult = expRes[1]
    print("expression = '{}' expression Class = '{}'".format(exp, MathExpressionClass(exp)))
    result = SolveMathProblem(exp)    
    print("result = {} , neededResult = {}".format(result,neededResult))
    if result != neededResult:
        raise Exception('not working properly')

# input_text = None
# while input_text != "stop":
#     print()
#     print("expression Class = '{}'".format(MathExpressionClass(input_text)))
#     print("result = {}".format(SolveMathProblem(input_text)))
#     print()
#     input_text = input("enter expression_")
