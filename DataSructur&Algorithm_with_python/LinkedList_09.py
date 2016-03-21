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
        for e in contents:
            self.append(e)

    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + str(type(self)) + " + " + str(type(other)))
        result = LinkedList()
        cursor = self.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        cursor = other.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
        return result

    def insert(self,index,item):
        cursor = self.first
        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()

            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)

linkedlist = LinkedList([1,2,3,4,5])
linkedlist2 = LinkedList([9,8,7,6])
print(linkedlist[2])
linkedlist.append('append')
linkedlist.insert(2,'insert')
linkedlist += linkedlist2
for i in linkedlist:
    print(i)
