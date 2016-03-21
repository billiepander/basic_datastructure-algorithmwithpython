class itemNode:
    def __init__(self,item):
        self.item = item

class subTree(itemNode):
    def __init__(self,Lchild=None,Rchild=None,parent = None):
        super().__init__()
        self.parent = self.item
        self.Lchild = Lchild
        self.Lchild = Rchild


a = itemNode(5)
b = itemNode(8)
c = itemNode(9)
d=subTree(b,c,a)
print(d.item)
