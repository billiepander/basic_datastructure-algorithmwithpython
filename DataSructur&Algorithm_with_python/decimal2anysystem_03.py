from stackType_01 import Stack
deci = int(input('input the number:'))
base = int(input('input the system you want to transfer to:'))

def trans(deci,base):
    flag = '0123456789ABCDEF'
    stack = Stack()
    while deci//base > 0:
        stack.push(flag[deci%base])
        deci //= base
    stack.push(flag[deci])
    print(stack.cstack)

trans(deci,base)