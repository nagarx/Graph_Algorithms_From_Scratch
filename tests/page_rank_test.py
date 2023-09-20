import unittest
import numpy as np
from src.page_rank import PageRank

class TestPageRank(unittest.TestCase):
    def normalize_matrix(self, graph_matrix):
        out_degree = np.sum(graph_matrix, axis=1)
        for i in range(len(out_degree)):
            if out_degree[i] != 0:
                graph_matrix[i] = graph_matrix[i] / out_degree[i]
        return graph_matrix

    def test_basic_graph(self):
        print("Running test_basic_graph...")
        graph_matrix = np.array([
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0]
        ], dtype=float)
        graph_matrix = self.normalize_matrix(graph_matrix)
        pr = PageRank(graph_matrix)
        final_rank_vector = pr.run()
        print("Final PageRank Vector:", final_rank_vector)
        expected_rank_vector = np.array([0.27665873, 0.15507966, 0.28689782, 0.28136378])  # Updated expected values
        print("Expected PageRank Vector:", expected_rank_vector)
        np.testing.assert_almost_equal(final_rank_vector, expected_rank_vector, decimal=4)

    # ... (other tests can be similar)

if __name__ == "__main__":
    unittest.main()