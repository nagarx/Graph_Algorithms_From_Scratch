class GraphDFS:
    def __init__(self):
        self.graph = {}  # {vertex: [list of neighbors]}
        self.visited = set()  # To keep track of visited vertices
        self.traversal = []  # To keep track of traversal order

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph

    def dfs(self, start_vertex):
        self.visited.add(start_vertex)
        self.traversal.append(start_vertex)
        for neighbor in self.graph[start_vertex]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

    def traverse(self, start_vertex):
        self.visited = set()  # Clear the visited set
        self.traversal = []  # Clear the traversal list
        self.dfs(start_vertex)
        return self.traversal


# Sample Usage
g = GraphDFS()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
traversal_result = g.traverse('A')

print(traversal_result)