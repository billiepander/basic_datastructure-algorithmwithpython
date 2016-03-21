# -*- coding:utf-8 -*-
# from stackType_01 import Stack
import stackType_01
def ToPostfix(expression):
    L = []
    stack = stackType_01.Stack()
    for i in expression:
        if i in '(+-*/':
            stack.push(i)
        elif i == ')':
            while stack.peek() != '(':
                L.append(stack.pop())
            stack.pop()
        else:
            L.append(i)
    print('postfix:',''.join(L))
    return L

def calpostfix(stt):
    stack = stackType_01.Stack()
    for i in stt:
        if i in '+-*/':
            pop1 = stack.pop()
            pop2 = stack.pop()
            temp = pop2+i+pop1
            stack.push(str(eval(temp)))
        else:
            stack.push(i)
    print('calresult:',stack.peek())

expression = list(input('plz input the expression with balanced parentheses:'))
calpostfix(ToPostfix(expression))