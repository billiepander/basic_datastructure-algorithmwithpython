from stackType_01 import Stack

while True:
    stack = Stack()
    str = input('input the arithmetic expression:')
    if len(str) == 0:
        print('input something')
    else:
        for i in str:
            if i in '({[':         #!!!
                stack.push(i)
            elif i in ')}]':
                stack.pop()
        if stack.size()==0:
            print('It is a balanced arithmetic expression')
        else:
            print('not a balanced arithmatic expression')
