class Cercularqueue():
    def __init__(self,size):
        self.size = size
        self.item = [None] * size
        self.front = self.rear = -1
    
    def enqueue(self,value):
        if ((self.rear + 1) % self.size  == self.front ):
            print("data is full")
        elif self.rear == -1 :
            self.rear +=1
            self.front +=1
            self.item[self.rear] = value
        else:
            self.item[(self.rear + 1) % self.size] = value
            self.rear += 1

    def dequeue(self):
        if (self.rear == self.front == -1):
            print("Queue is Empty")
        elif self.rear == self.front :
            print(self.item[self.front])
            self.rear = self.front = -1
        else:
            print(self.item[self.front])
            self.front = (self.front + 1) % self.size

cq = Cercularqueue(5)
cq.enqueue(15)
cq.enqueue(20)
cq.enqueue(43)
cq.enqueue(56)
cq.enqueue(89)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
# cq.enqueue(90)




