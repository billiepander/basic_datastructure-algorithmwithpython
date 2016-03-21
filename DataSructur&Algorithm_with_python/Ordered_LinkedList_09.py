class LinkedList:
    class __Node:
        def __init__(self, item, next = None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def setItem(self, item):
            self.item = item

        def setNext(self,next):
            self.next = next

        def getNext(self):
            return self.next

    def __init__(self,contents=[]):
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0
        contents = sorted(contents)
        for i,e in enumerate(contents):
            self.append(e)
            if i==0:
                self.first=LinkedList.__Node(e)


    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def add(self,item):
        node = LinkedList.__Node(item)
        if item < self.first.getItem():
            node.setNext(self.first)
            self.first = node
        elif item > self.last.getItem():
            self.last.setNext(node)
            self.last = node
        else:
            cursor = self.first.getNext()
            while cursor.getItem < item and cursor != self.last:
                cursor = cursor.getNext()
            cursor.setNext(node)
            node.setNext(cursor.getNext())




linkedlist = LinkedList([4,1,3,2,5])
# linkedlist2 = LinkedList([9,8,7,6])
# print(linkedlist[2])
linkedlist.add(8)
# linkedlist.insert(2,'insert')
# linkedlist += linkedlist2
first = linkedlist.first
while True:
    print(first.getItem())
    first = first.getNext()
