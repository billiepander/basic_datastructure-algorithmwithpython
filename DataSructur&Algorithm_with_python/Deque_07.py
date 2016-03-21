class Deque:                    # right is the front
    def __init__(self,*args):
        self.item = []
        for i in args:
            self.item.insert(0,i)

    def __len__(self):
        return len(self.item)
    def size(self):
        return len(self.item)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def add_front(self,*arg):
        for i in arg:
            self.item.append(i)

    def add_rear(self,*arg):
        for i in arg:
            self.item.insert(0,i)

    def remove_front(self):
        if self.size() > 0:
            return self.item.pop()
        else:
            print('empty deque, cannot dequeue anymore')

    def remove_rear(self):
        if self.size() > 0:
            return self.item.pop(0)
        else:
            print('empty deque, cannot dequeue anymore')

# deque = Deque(1,2,3,4)
# print(deque.size())
# print(len(deque))
# print(deque.item)
# deque.add_front('front')
# print(deque.item)
# deque.add_rear('rear')
# print(deque.item)
# print(deque.remove_front())
# print(deque.remove_rear())