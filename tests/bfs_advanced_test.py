
import unittest
from src.Search_Algorithms.Breadth_First_Search import GraphBFS

class TestBFSAdvanced(unittest.TestCase):

    def test_large_graph(self):
        graph = GraphBFS()
        vertices = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for u in vertices:
            for v in vertices:
                if u != v:
                    graph.add_edge(u, v)
        start = 'A'
        result = graph.traverse(start)
        self.assertEqual(result, vertices)  # Should visit all vertices

    def test_disconnected_graph(self):
        graph = GraphBFS()
        graph.add_edge('A', 'B')
        graph.add_edge('C', 'D')
        start = 'A'
        result = graph.traverse(start)
        self.assertEqual(result, ['A', 'B'])  # Should only visit A and B

    def test_graph_with_loops(self):
        graph = GraphBFS()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'A')
        graph.add_edge('B', 'C')
        start = 'A'
        result = graph.traverse(start)
        self.assertEqual(result, ['A', 'B', 'C'])  # Should not go into an infinite loop

    def test_graph_with_multiple_starting_points(self):
        graph = GraphBFS()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('D', 'E')
        start1, start2 = 'A', 'D'
        result1 = graph.traverse(start1)
        result2 = graph.traverse(start2)
        self.assertEqual(result1, ['A', 'B', 'C'])
        self.assertEqual(result2, ['D', 'E'])

if __name__ == "__main__":
    unittest.main()
