# -*- coding:utf-8 -*-
class Stack:
    def __init__(self,*args):
        self.cstack = []        #c:construct
        for i in args:
            self.cstack.append(i)
    def push(self,x):
        self.cstack.append(x)
    def size(self):
        return len(self.cstack)
    def pop(self):
        if self.size()>0:
            return self.cstack.pop()
        else:
            print('Sorry, this is an empty stack')
    def peek(self):
        if self.size()>0:
            return self.cstack[len(self.cstack)-1]
        else:
            return 'empty stack'

    # def __next__(self):
    #         self.a = self.cstack[self.size()-1]
    #         if self.size() == 0: # 退出循环的条件
    #             raise StopIteration();
    #         return self.a # 返回下一个值
    # def __iter__(self):
    #     return self.cstack

stack = Stack(1,'*','/')
print(stack.pop())
trystack = Stack()
print(trystack.cstack)
stack = Stack(1,2,3,4)
print(stack.pop())
print(stack.cstack)
stack.push('haha')
print(stack.cstack)
stack.pop()
print(stack.cstack)
stack.pop()
stack.pop()
print(stack.peek())
stack.pop()
stack.pop()
stack.pop()
print(stack.size())
print(stack.peek())

# class Stack:
#     def __init__(self,*args):
#         self = []        #c:construct
#         for i in args:
#             self.append(i)
#     def push(self,x):
#         self.append(x)
#     def size(self):
#         return len(self)
#     def pop(self):
#         if self.size()>0:
#             self.pop()
#         else:
#             print('Sorry, this is an empty stack')
#     def peek(self):
#         if self.size()>0:
#             return self[len(self.cstack)-1]
#         else:
#             return 'empty stack'

# stack = Stack(1,2,4,5)