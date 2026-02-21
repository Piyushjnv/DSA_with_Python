class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList :

    def __init__(self,head = None):
        self.head = Node(head)

    def addatbeg(self, value = None):
        tem = self.head
        if self.head.data == None:
            self.head = Node(value)
            return
        head = Node(value)
        head.next = self.head
        self.head = head
    def addatafter(self , x, vlaue= None):
        tem = self.head
        while tem.data != x:
            tem = tem.next
        
        
    def Addatend(self,value = None):
        head = self.head
        if self.head.data == None:
            # print("node is empty and None")
            self.head = Node(value)
            return 
        while head.next != None:
            head  = head.next # shift the value of head to next node
        head.next = Node(value) #add node at the end

    def ptintsll(self):
        tmp= self.head
        while tmp.next != None: # iterate until counter none
            print(tmp.data)
            tmp = tmp.next
        else:
             print(tmp.data) #print last node



obj = singlyLinkedList()
obj.Addatend(20)
# obj.Addatend(30)
# obj.Addatend(40)
# obj.addatbeg(15)
obj.ptintsll()
