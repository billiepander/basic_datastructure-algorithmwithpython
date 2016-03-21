from Queue_05 import Queue
names = input('plz input the names(with blank betwwwn them):')
juge = int(input('plz input the judge number:'))
flag = 1
# queue = Queue(names.split(" "))   #[['pd', 'bill', 'billie', 'joe']]
queue = Queue()
for i in names.split(" "):
    queue.enqueue(i)

while queue.size() != 1:
    if flag != juge:
        queue.enqueue(queue.dequeue())
        flag+=1
    else:
        queue.dequeue()
        flag=1

print(queue.item)

