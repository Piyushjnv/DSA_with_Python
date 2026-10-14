class Graph :
    def __init__(self):
        self.dist = {}

    def add_vertex(self, value):
        if value not in self.dist:
            self.dist[value] = []

    def add_edge(self , sor , dest):
     
        self.add_vertex(sor)
        self.add_vertex(dest)

        self.dist[sor].append(dest)
        self.dist[dest].append(sor)

    def display(self ):
        for x  in self.dist:
            print(x, "-> ",self.dist[x])


gf= Graph()
# gf.add_vertex(1)
gf.add_edge(1,2)
gf.add_edge(1,3)
gf.add_edge(2,3)
gf.display()

