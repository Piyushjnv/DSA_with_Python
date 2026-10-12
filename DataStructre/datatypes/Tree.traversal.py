class Node:
    def __init__(self, value):
        self.left = None
        self.right = None 
        self.data = value


def preorder(root):
    
    if root != None:
            print(root.data  , end=" ")
    if root.left != None:
        preorder(root.left)
    if root.right != None:
        preorder(root.right)
    return 


def Inorder(root):
    
    
    if root.left != None:
        Inorder(root.left)
    if root != None:
        print(root.data  , end=" ")
    if root.right != None:
        Inorder(root.right)
    

def postorder(root):
    
    
    if root.left != None:
        postorder(root.left)
    if root.right != None:
        postorder(root.right)
    if root != None:
            print(root.data  , end=" ")
 

x = Node(1)
x.right = Node(5)
x.right.left = Node(43)
x.right.right = Node(8)
x.left = Node(3)
x.left.left = Node(2)
x.left.right = Node(4)

preorder(x)
print("\n Inorder")
Inorder(x)
print("\n postorder")
postorder(x)