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

             
def Delete(root , value):
        if( root == None) :
            print("root is empty ")
            return root
        if root.data > value:
            root.left = Delete(root.left, value )
        if root.data < value :
            root.right  =  Delete(root.right, value )
        else:
            if root.data == value:
                 if root.left == None :
                      return root.right
                 elif root.right == None:
                      return root.left 
                 else:
                    x  =   root.right
                    while x.left != None and x.left.left != None :
                              x = x.left
                    else:
                             if x.left == None:
                                 x.left = root.left
                                 return x
                             else:
                                  y = x.left.right
                                  root.data = x.left.data
                                  x.left = y
                                #   x.left.left = root.left
                                #   x.left.right = root.right
                                #   x.left = x.left.right

                                #   root = x.left.left
                                #   root = x.left
                                #   x.left = y
                                  return root
                             
        return root


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
Insert(x,12)
Insert(x,15)
Insert(x,14)
Insert(x,20.5)
Insert(x,7)
Insert(x,1)
Insert(x,4)
Insert(x,6)
Insert(x,6.5)
Insert(x,25)

Inorder(x)
Search(x,11)
Delete(x,7)
Inorder(x)