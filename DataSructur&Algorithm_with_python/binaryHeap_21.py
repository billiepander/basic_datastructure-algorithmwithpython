#coding:utf-8
class BinaryHeap:
    def __init__(self):
        self.List = [0]
        self.num = 0

    def build_heap(self, a_list):       #从一个list组建为binary heap
        for i in a_list:
            self.insert(i)

    def insert(self,item):
        self.List.append(item)
        i = len(self.List)-1
        while i//2 > 0:
            if self.List[i] < self.List[i//2]:
                self.List[i],self.List[i//2] = self.List[i//2],self.List[i]
            i = i//2
        self.num += 1

    def minchild(self,i):
        if 2*i+1 > self.num:
            return 2*i
        else:
            if self.List[2*i] > self.List[2*i+1]:
                return 2*i+1
            else:
                return 2*i

    def kill_min(self):
        self.List.pop(1)
        self.List.insert(1,self.List.pop())
        self.num -= 1
        i = 1
        while i*2 < self.num:
            if self.List[i] > self.List[self.minchild(i)]:
                self.List[i],self.List[self.minchild(i)] = self.List[self.minchild(i)],self.List[i]
            i *= 2

bh = BinaryHeap()
bh.build_heap([5,2,6,8,9,10,1])
print(bh.List)
bh.kill_min()
print(bh.List)