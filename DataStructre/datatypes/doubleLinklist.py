class Node:
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkList():
    def __init__(self, value = None):
        self.head = Node(value)

    def addatend(self, value):
        tmp = self.head
        if self.head.data == None:
            self.head = Node(value)
            return
        while tmp.next != None:
            tmp = tmp.next
        newNode = Node(value)
        newNode.prev = tmp
        tmp.next = newNode

    def addAtBeg(self, value):
        tmp = self.head
        if self.head.data == None:
            self.head = Node(value)
            return
        newNode = Node(value)
        tmp.prev  = newNode
        newNode.next = tmp
        self.head = newNode
    
    def Addatmid(self,x, value):
        tmp = self.head
        if self.head.data == None:
            self.head = Node(value)
            return

        if tmp.data == x:
            newNode= Node(value)
            newNode.next = tmp
            newNode.prev = tmp.prev
            tmp.prev = newNode
            return
        
        while tmp.next != None:
            if tmp.data == x:
                newNode= Node(value)
                newNode.next = tmp
                newNode.prev = tmp.prev
                tmp.prev = newNode
                return
            tmp = tmp.next
        newNode = Node(value)


    