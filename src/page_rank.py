import numpy as np


class PageRank:
    def __init__(self, graph_matrix, decay_factor=0.85, epsilon=1e-6):
        self.graph = graph_matrix
        self.decay_factor = decay_factor
        self.epsilon = epsilon
        self.num_nodes = len(graph_matrix)
        self.dangling_nodes = np.where(~graph_matrix.any(axis=1))[0]

    def handle_dangling_nodes(self, rank_vector):
        # Distribute the PageRank of dangling nodes equally across all nodes, considering the decay factor
        rank_vector += (self.decay_factor * np.sum(rank_vector[self.dangling_nodes]) / self.num_nodes)

    def power_iteration(self, rank_vector):
        # Compute new rank vector using the Power Iteration method
        new_rank_vector = np.dot(self.graph.T, rank_vector) * self.decay_factor
        new_rank_vector += (1 - self.decay_factor) / self.num_nodes
        self.handle_dangling_nodes(new_rank_vector)
        return new_rank_vector

    def check_convergence(self, old_ranks, new_ranks):
        # Check if the PageRank values have converged
        return np.linalg.norm(new_ranks - old_ranks, 2) < self.epsilon

    def personalized_pagerank(self, personalization_vector=None):
        # Compute a personalized PageRank vector
        if personalization_vector is None:
            personalization_vector = np.ones(self.num_nodes) / self.num_nodes
        rank_vector = personalization_vector
        while True:
            new_rank_vector = self.power_iteration(rank_vector)
            if self.check_convergence(rank_vector, new_rank_vector):
                break
            rank_vector = new_rank_vector
        return new_rank_vector

    def run(self):
        # Main method to run the PageRank algorithm
        initial_rank_vector = np.ones(self.num_nodes) / self.num_nodes
        final_rank_vector = self.personalized_pagerank(initial_rank_vector)
        return final_rank_vector


# Test the PageRank class
if __name__ == "__main__":
    # Create an example adjacency matrix for a simple graph
    graph_matrix = np.array([
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ], dtype=float)

    # Normalize the adjacency matrix
    out_degree = np.sum(graph_matrix, axis=1)
    graph_matrix = graph_matrix / out_degree[:, np.newaxis]

    # Initialize the PageRank class and run the algorithm
    pr = PageRank(graph_matrix)
    final_rank_vector = pr.run()
    print("Final PageRank Vector:", final_rank_vector)

