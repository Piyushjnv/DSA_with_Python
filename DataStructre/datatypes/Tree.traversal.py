class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
def Preoder(root):
    if root != None :
        print(root.data ,end = " ")
        Preoder(root.left)
        Preoder(root.right)

def InOrder(root):
    if root != None :
        InOrder(root.left)
        print(root.data ,end = " ")
        InOrder(root.right)

def  PostOrder(root):
    if root != None :
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data ,end = " ")


root = Node(5)
root.left= Node(15)
root.right = Node(3)
# root.left.left = Node(20)
# root.left.right = Node(178)
# root.right.right = Node(89)
# root.left= Node(15)

Preoder(root )
print(" ")
InOrder(root)
print(" ")
PostOrder(root)