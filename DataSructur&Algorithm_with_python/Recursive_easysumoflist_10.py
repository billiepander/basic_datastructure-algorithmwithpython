#-*- coding:utf-8 -*-
#total = (1 + (3 + (5 + (7 + 9))))
def sum(seq=[]):
    if len(seq)==1:
        return seq[0]
    return seq[0]+sum(seq[1:])

print('sum of the list:',sum([1,2,3,4,5,6,7,8,9]))

#factorial of a number:阶乘
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print('10!=',factorial(10))

#Converting an Integer to a String in Any Base
#review:decimal2anysystem_03.py, use stack to achieve the same thing, while this is much easier
convert_string = "0123456789ABCDEF"
def to_str(n, base):
    global convert_string
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]
print(to_str(769, 2))

#reverse a string
def reverse(string):
    if len(string)==1:
        return str(string)
    return str(string[len(string)-1])+reverse(string[:len(string)-1])

print(reverse('string'))