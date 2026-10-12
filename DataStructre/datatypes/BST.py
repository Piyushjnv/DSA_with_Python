class Node:
    def __init__(self, value):
        self.left = None
        self.right =  None
        self.data  = value


def Insert(root, value):
        if (root == None or root.data == None):
            return Node(value)
        elif (root.data == value):
            return root
        elif (root.data > value) :
            root.left = Insert(root.left ,value)
        else :
            root.right = Insert(root.right, value)
        return root

def  Search(root, value):
        if (root == None or root.data == None):
            print("\n not found ", value)
            return Node(value)
        elif (root.data == value):
            print("\nfind value = ", value)
            return root
        elif (root.data > value) :
             Search(root.left ,value)
        else :
             Search(root.right, value)

def Inorder(root):
    
    
    if root.left != None:
        Inorder(root.left)
    if root != None:
        print(root.data  , end=" ")
    if root.right != None:
        Inorder(root.right)
    
x = Node(10)
Insert(x,2)
Insert(x,5)
Insert(x,8)
Insert(x,11)
Insert(x,12)
Insert(x,20.5)

Inorder(x)
Search(x,11)