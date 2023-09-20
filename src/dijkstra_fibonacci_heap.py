from core.fibonacci_heap import FibonacciHeap, Node, extract_min, insert, decrease_key
from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = 0  # Number of vertices
        self.graph = defaultdict(list)
        self.vertex_map = {}
        self.reverse_vertex_map = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertex_map:
            self.vertex_map[vertex] = self.V
            self.reverse_vertex_map[self.V] = vertex
            self.V += 1

    def add_edge(self, u, v, w):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[self.vertex_map[u]].append((self.vertex_map[v], w))

    def get_vertex_name(self, vertex_idx):
        return self.reverse_vertex_map.get(vertex_idx, None)

    def dijkstra(self, src):
        src_idx = self.vertex_map.get(src, None)
        if src_idx is None:
            return None

        dist = {i: float("inf") for i in range(self.V)}
        dist[src_idx] = 0

        heap = FibonacciHeap()
        heap_nodes = [None] * self.V

        for i in range(self.V):
            heap_nodes[i] = Node(dist[i])
            insert(heap, heap_nodes[i])

        heap.min_node = heap_nodes[src_idx]

        while heap.num_nodes > 0:
            u = extract_min(heap)
            if u is None:
                print("Warning: Extracted min node is None.")
                break

            u_idx = heap_nodes.index(u)

            if u_idx not in self.graph:
                continue

            for v, w in self.graph[u_idx]:
                if dist[u_idx] + w < dist[v]:
                    if heap_nodes[v] is None:
                        print(f"Warning: heap_nodes[{v}] is None.")
                        continue

                    dist[v] = dist[u_idx] + w
                    if heap.min_node is not None:  # Added check
                        decrease_key(heap, heap_nodes[v], dist[v])
                    else:
                        print("Warning: heap.min_node is None.")

        named_dist = {self.get_vertex_name(i): d for i, d in dist.items()}
        return named_dist


# Test code
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    print(g.graph)
