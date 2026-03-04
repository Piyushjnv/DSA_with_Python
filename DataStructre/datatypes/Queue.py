# This is Queue data structure made in python it has 3 methods for add , remove, and veiw data respectvely in Queue

class Queue:
    def __init__(self,x):
        self.queue = []
        self.__x = x
        self.__start =0

    def Add(self,value):
        if self.__x == self.__start:
            print("NO space")
            return
        self.__start += 1
        self.queue.append(value)


    def delete(self):
        if len(self.queue) == 0:
            print("NO DATA FOUND")
            return
        self.queue.pop(0)
        self.__start -= 1
    
    def view(self):
        if len(self.queue) == 0:
            print("NO DATA FOUND")
        for i in self.queue :
            print(i, end="--")



que = Queue(2)
que.Add(1)
que.Add(2)
print(que._Queue__x)
que.delete()
que.Add(3)
# que.delete()
# que.delete()
# que.Add(5)

que.view()

