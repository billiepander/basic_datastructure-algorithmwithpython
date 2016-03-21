class Queue:                    # right is the front
    def __init__(self,*args):
        self.item = []
        for i in args:
            self.item.insert(0,i)

    def size(self):
        return len(self.item)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def enqueue(self,*arg):
        for i in arg:
            self.item.insert(0,i)

    def dequeue(self):
        if self.size() > 0:
            return self.item.pop()
        else:
            print('empty queue, cannot dequeue anymore')

# que = Queue(1,2,3)
# que.enqueue(4,5)
# print(que.item)
# print(que.dequeue())
# print(que.dequeue())
# print(que.size())