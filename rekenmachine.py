# https://dodona.be/nl/courses/4195/series/46774/activities/1458138173

def evalueer_postfix(expressie):
    stack = []
    for s in expressie:
        if s.isnumeric():
            stack.append(s)
        else: #operator
            operator = s
            getal2 = stack.pop()
            getal1 = stack.pop()
            resultaat = voerBewerkingUit(int(getal1), int(getal2), operator)
            stack.append(resultaat)
    return stack.pop()    

def voerBewerkingUit(getal1, getal2, operator):
    if operator == "+":
        return float(getal1 + getal2)
    if operator == "-":
        return float(getal1 - getal2)
    if operator == "*":
        return float(getal1 * getal2)
    return float(getal1 / getal2)
    

def infix_naar_postfix(expressie):
    out = []
    stack = []
    for s in expressie:
        if s.isnumeric():
            out.append(s)
        else:
            if len(stack) == 0 or s == "(" or priority(s) > priority(stack[-1]):
                stack.append(s)
            else:
                if s == ")":
                    bovensteOperator = stack.pop()
                    while bovensteOperator != "(":
                        out.append(bovensteOperator)
                        bovensteOperator = stack.pop()
                else:
                    while len(stack) > 0 and priority(s) <= priority(stack[-1]):
                        bovensteOperator = stack.pop()
                        out.append(bovensteOperator)
                    stack.append(s)
    
    while not len(stack) == 0:
        out.append(stack.pop())
    
    return out

def priority(operator):
    if operator == "(" or operator == ")":
        return 0
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2

def rekenmachine(s):
    infix_tokens = s.split()
    postfix = infix_naar_postfix(infix_tokens)
    resultaat = evalueer_postfix(postfix)
    return resultaat

# def is_operand(o):
#     return 

# def evalueer_postfix(postfix):
#     s = []
#     for o in postfix:
#         if is_operand(o) :
#             s.append(o)

# def infix_naar_postfix(expressie):
#     s=[]
#     for token in infix:
#         if is_operand(token):
#             uitvoer.append(token)
#         elif is_operator(token) or token =="(":
#             if len(s) == 0 or prioriteit(token)> prioriteit(s(-1)):
#                 s.append(token)
#         else
#             while len(s) >0 and prioriteit(token) <= prioriteit(s[-1]):
#                 uitvoer.append(s.pop())


# def rekenmachine(s):
#     pass
