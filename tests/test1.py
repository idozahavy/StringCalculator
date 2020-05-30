from StringCalculator import SolveMathProblem

exp_texts = ["5",
             "1+(1)",
             "2*6",
             "-9+3",
             "+35419.55619-6",
             "5*.25/9-6",
             "-59*-.25/-9-6",
             "5^(2*6)-3V27^3",
             "(1/6)-1^(2*6)"]
i = 0
for text in exp_texts:
    i += 1
    print()
    print()
    print("exp_text{} ---------".format(i))
    print("expression = '{}'".format(exp_texts[i-1]))
    print("result = {}".format(SolveMathProblem(exp_texts[i-1])))
