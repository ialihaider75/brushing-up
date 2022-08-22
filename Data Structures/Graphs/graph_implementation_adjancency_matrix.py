class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for j in range(self.v)] for i in range(self.v)]
    
    def make_an_edge(self,vertex1,vertex2):
        if (vertex1 <= (self.v)) and (vertex2 <= (self.v)):
            self.graph[vertex1-1][vertex2-1] = 1
        else:
            print("Sorry vertex1: " + str(vertex1) + " or vertex2: " + str(vertex2) + " not exists")
    
    def remove_edge(self,vertex1,vertex2):
        if vertex1 <= (self.v) and vertex2 <= (self.v):
            self.graph[vertex1-1][vertex2-1] = 0
        else:
            print("Sorry vertex1: " + str(vertex1) + " or vertex2: " + str(vertex2) + " not exists")
    
    def print_graph(self):
        for i in range(0,self.v):
            for j in range(0,self.v):
                if self.graph[i][j] == 1:
                    print(str(i+1) + " => " + str(j+1))
    
    
graph = Graph(5)
graph.make_an_edge(1,2)
graph.make_an_edge(1,5)
graph.make_an_edge(1,4)
graph.make_an_edge(2,3)
graph.make_an_edge(3,1)
graph.make_an_edge(4,3)
graph.make_an_edge(4,5)
graph.remove_edge(1,4)
graph.make_an_edge(4,1)
graph.print_graph()