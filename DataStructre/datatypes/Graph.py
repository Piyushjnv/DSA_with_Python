class Bi_directed_Graph:
    
    def __init__(self, vertexs : int):
        self.mat = [[0]*vertexs for _ in range(vertexs)]
        self.size = vertexs

    def add_edge(self, sor: int, dest: int  , value = 1):
        if sor <= self.size- 1 and sor >= 0 and  dest <= self.size - 1 and dest >= 0 :
            self.mat[sor][dest] = value
            self.mat[dest][sor] = value

    def display(self):
        for x in self.mat:
         print( " ".join(map(str, x)))


x= Bi_directed_Graph(5)

x.add_edge(1,2)
x.add_edge(4,2 , 3)
x.add_edge(1,4)
x.add_edge(3,2 , 5)
x.add_edge(4,3)
x.add_edge(0,3, 4)
x.display()