class DobleQueue:
    def __init__(self):
        self.queue = []

    def Addatend(self,value):
        self.queue.append(value)

    def Addatbeg(self,value):
        self.queue.insert(0,value)

    def deleteatbeg(self):
        if len(self.queue) == 0:
            print("NO DATA FOUND")
            return
        self.queue.pop(0)
    
    def deleteATend(self):
        if len(self.queue) == 0:
            print("NO DATA FOUND")
            return
        self.queue.pop()

    def view(self):
        if len(self.queue) == 0:
            print("NO DATA FOUND")
        for i in self.queue :
            print(i, end="--")
        print(" ")


dque = DobleQueue()
dque.Addatbeg(2)
dque.Addatend(5)
dque.Addatbeg(3)
dque.Addatbeg(4)
dque.Addatbeg(5)
dque.view()
dque.deleteatbeg()
dque.view()



