from collections import deque, defaultdict


class GraphBFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        visited = set()
        traversal_order = []
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                queue.extend(self.graph[vertex])

        return traversal_order

    # Adding the missing "traverse" method that just calls your "bfs" method.
    def traverse(self, start_vertex):
        return self.bfs(start_vertex)


# Test the implementation
graph = GraphBFS()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')

traversal_order = graph.bfs('A')
print(traversal_order)  # Output should be ['A', 'B', 'C', 'D', 'E', 'F']