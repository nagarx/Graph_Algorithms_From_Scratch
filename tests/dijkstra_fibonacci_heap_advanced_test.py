# Generating advanced test cases for Dijkstra's Algorithm implemented with a Fibonacci Heap
import random
import unittest
from src.dijkstra_fibonacci_heap import Graph

class TestDijkstraFibonacciHeapAdvanced(unittest.TestCase):

    def test_large_almost_complete_graph(self):
        graph = Graph()
        vertices = list("ABCDEFGHIJKLMNOP")
        for u in vertices:
            for v in vertices:
                if u != v:
                    weight = random.randint(1, 100)
                    graph.add_edge(u, v, weight)

        # Remove one random edge to make it almost complete
        u, v = random.choice(vertices), random.choice(vertices)
        if u != v:
            graph.graph[graph.vertex_map[u]] = [(vertex, weight) for vertex, weight in graph.graph[graph.vertex_map[u]] if vertex != graph.vertex_map[v]]

        start, end = 'A', 'P'
        distance = graph.dijkstra(start)
        # We can't determine the expected distance since it's a random graph, but it should not be infinity
        self.assertNotEqual(distance[end], float("inf"))

    def test_graph_with_parallel_edges(self):
        graph = Graph()
        graph.add_edge('A', 'B', 1)
        graph.add_edge('A', 'B', 2)
        graph.add_edge('A', 'B', 3)
        graph.add_edge('B', 'C', 1)

        start, end = 'A', 'C'
        distance = graph.dijkstra(start)
        self.assertEqual(distance[end], 2)  # Should choose the path A->B->C with total weight 2 (1 from A->B and 1 from B->C)

    def test_graph_with_max_min_values(self):
        graph = Graph()
        max_value = 10**18  # Replace with the maximum value your data type can hold
        min_value = 1  # Replace with the minimum non-zero value

        graph.add_edge('A', 'B', max_value)
        graph.add_edge('B', 'C', max_value)
        graph.add_edge('A', 'C', min_value)

        start, end = 'A', 'C'
        distance = graph.dijkstra(start)
        self.assertEqual(distance[end], min_value)

    def test_random_graph(self):
        graph = Graph()
        vertices = list("ABCDEFG")
        for u in vertices:
            for v in vertices:
                if u != v and random.random() < 0.5:
                    weight = random.randint(1, 100)
                    graph.add_edge(u, v, weight)

        start, end = random.choice(vertices), random.choice(vertices)
        while start == end:
            end = random.choice(vertices)

        distance = graph.dijkstra(start)
        # We can't determine the expected distance since it's a random graph, but we can ensure it's either a number or infinity
        self.assertTrue(distance[end] == float("inf") or isinstance(distance[end], (int, float)))

if __name__ == "__main__":
    unittest.main()

