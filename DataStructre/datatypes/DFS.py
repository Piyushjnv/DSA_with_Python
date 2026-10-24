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

    def DFS(self, src):
        visited_arr = [False]*self.size
        stack = []
        if 0 <= src < self.size:
          print(src , end="->")
          stack.append(src)
          visited_arr[src] = True
          while True:
           
            for x in range(len(self.mat[stack[-1]])):
                if self.mat[src][x]  == 1:
                    # if visited_arr[x] != True:
                    #     print(x)
                    #     visited_arr[x] = True
                    if visited_arr[x] != True:
                        stack.append(x)
                        src = x
                        print(x , end="->")
                        visited_arr[x] = True
                        continue
                    
            else:
                
               
                x = stack.pop()
                # print('\npop run ',x)  
                if len(stack) > 0: 
                    src = stack[-1]    

            if len(stack) <= 0:
                                 break 
                    # visited_arr[]
       
x= Bi_directed_Graph(7)

x.add_edge(0,3)
x.add_edge(0,1)
# x.add_edge(3,2)
x.add_edge(1,2)
x.add_edge(2,4)
x.add_edge(2,5)
x.add_edge(4,6)
# x.add_edge(5,6)
# x.display()
x.DFS(0)



