#-*- coding:utf-8 -*-
# 1): __add__(self,y)       x+y

class A:
    def __init__(self,x):
        self.x = x
    def __add__(self, other):
        if type(other.x) == 'str':
            return str(self.x) + str(other.x)
        elif type(other.x) == 'int':
            return int(self.x)+int(other.x)

a=A(2)
b=A(4)
print(a.x+b.x)
a=A('A')
b=A('B')
print(a.x+b.x)