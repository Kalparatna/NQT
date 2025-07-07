class Graph:
    def __init__(self, directed =False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)

        if v2 not in self.graph:
            self.add_vertex(v2)

        self.graph[v1].append(v2)
        if not self.directed:
            self.graph[v2].append(v1)
    

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}->{self.graph[vertex]}")

g1 = Graph(directed = True)
g1.add_edge("A", "B")
g1.add_edge("C", "D")

g1.display()
