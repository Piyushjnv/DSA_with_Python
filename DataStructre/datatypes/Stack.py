class stack:
    def __init__(self):
        self.data = []
    
    def push(self,value):
        self.data.append(value)
    
    def pop(self):
        self.data.pop()
    
    def Showstack(self):
        for i in self.data:
            print(i, end="<--->")


hello = stack( )
hello.push(10)
hello.push(1545)
hello.pop()
hello.push(1540)
hello.push(10654)
hello.Showstack()




