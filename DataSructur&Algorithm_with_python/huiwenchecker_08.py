from Deque_07 import Deque
flag = 1
expression = input('plz input the string:')
deque = Deque()
for i in expression:
    deque.add_rear(i)

while deque.size() != 1 or 0:
    a = deque.remove_front()
    b = deque.remove_rear()
    if a!=b:
        flag = 0
        break

if flag:
    print('yes, it is huiwen')
else:
    print('nout a huiwen string')

