import unittest
from src.Graph_Algorithms.dijkstra_fibonacci_heap import Graph

class TestDijkstraFibonacciHeap(unittest.TestCase):

    def test_simple_graph(self):
        graph = Graph()
        graph.add_edge('A', 'B', 1)
        graph.add_edge('A', 'C', 4)
        graph.add_edge('B', 'C', 2)
        graph.add_edge('B', 'D', 5)
        graph.add_edge('C', 'D', 1)

        start, end = 'A', 'D'
        distance = graph.dijkstra(start)
        self.assertEqual(distance[end], 4)

    def test_graph_with_no_path(self):
        graph = Graph()
        graph.add_edge('A', 'B', 1)
        graph.add_edge('A', 'C', 4)
        graph.add_edge('C', 'D', 1)

        start, end = 'B', 'D'
        distance = graph.dijkstra(start)
        self.assertEqual(distance.get(end, float('inf')), float('inf'))

    def test_graph_with_single_node(self):
        graph = Graph()
        graph.add_edge('A', 'A', 0)

        start, end = 'A', 'A'
        distance = graph.dijkstra(start)
        self.assertEqual(distance[end], 0)

if __name__ == "__main__":
    unittest.main()
