# Graph Algorithms Implemented from Scratch
Welcome to this repository, where we delve deep into the intricacies of graph algorithms, implementing them entirely from scratch. This repository stands as a testament to the meticulous work behind each algorithm, showcasing the precision and attention to detail required to create efficient, reliable solutions from the ground up.

# Repository Structure
Our repository is organized into three main directories:

```commandline
├── core
│   └── fibonacci_heap.py
├── src
│   ├── breadth_first_search.py
│   ├── depth_first_search.py
│   ├── dijkstra_fibonacci_heap.py
│   └── page_rank.py
└── test
    ├── bfs_advanced_test.py
    ├── dfs_advanced_test.py
    ├── dijkstra_fibonacci_heap_advanced_test.py
    ├── dijkstra_fibonacci_heap_test.py
    └── page_rank_test.py
```

1. **core** - This is the backbone of our implementations. Here, you'll find foundational data structures that the main algorithms in the `src` directory rely upon. For instance, our `dijkstra_fibonacci_heap.py` algorithm is built upon the Fibonacci heap data structure found here.
    
    - `fibonacci_heap.py`: Implementation of the Fibonacci heap data structure.
2. **src** - This directory houses the core of our work: the graph algorithms themselves. Each file is a standalone implementation of a particular graph algorithm.
    
    - `breadth_first_search.py`: Breadth-first search algorithm.
    - `depth_first_search.py`: Depth-first search algorithm.
    - `dijkstra_fibonacci_heap.py`: Dijkstra's shortest path algorithm using Fibonacci heap.
    - `page_rank.py`: Implementation of the PageRank algorithm.
3. **test** - Ensuring the integrity and efficiency of our implementations is paramount. This directory contains tests that verify the accuracy and performance of our algorithms.
    
    - `bfs_advanced_test.py`: Advanced tests for the breadth-first search algorithm.
    - `dfs_advanced_test.py`: Advanced tests for the depth-first search algorithm.
    - `dijkstra_fibonacci_heap_advanced_test.py`: Advanced tests for Dijkstra's algorithm with Fibonacci heap.
    - `dijkstra_fibonacci_heap_test.py`: Basic tests for Dijkstra's algorithm with Fibonacci heap.
    - `page_rank_test.py`: Tests for the PageRank algorithm.

## Graph Algorithms: A Brief Introduction
Graphs are fundamental structures in computer science, representing a set of objects in which some pairs are connected. The algorithms that operate on graphs, therefore, are crucial in addressing various problems, from shortest path computations to web page ranking.

Implementing these algorithms from scratch not only reinforces the understanding of their underlying principles but also offers an unobstructed view into their mechanics, free from the potential obfuscations of library-specific nuances.

## BFS: An Overview
Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes in the order of their distance from the source node, where distance is measured by the number of edges on the shortest path from the source node. BFS begins at a source vertex and inspects all the neighboring vertices. Subsequently, for each of those nearest vertices, it explores their unexplored neighbor vertices, and so on.
### Mathematical Foundations
Graph Representation: BFS can be applied to both directed and undirected graphs. A graph $G$ can be represented as $G=(V, E)$, where $V$ is a set of vertices and $E$ is a set of edges.
- Adjacency Matrix: $M[i][j]=1$ if there's an edge between vertex $i$ and vertex $j$, else $M[i][j]=0$.
- Adjacency List: For each vertex $v$, its neighbors are stored in a list.
Queue: BFS utilizes a First-In-First-Out (FIFO) data structure called a Queue. Vertices are enqueued and dequeued as BFS progresses.

BFS Tree: BFS produces a BFS tree, which can be represented as $T=\left(V, E_T\right)$, where $E_T \subseteq E$. It shows the connection between vertices as they are explored by BFS.

### Algorithm Complexity
#### Time Complexity:
BFS visits each vertex exactly once and examines each edge once or twice (undirected graphs). Therefore, the time complexity is:
$$O(|V|+|E|)$$
where $|V|$ is the number of vertices and $|E|$ is the number of edges.
#### Space Complexity:
The space complexity depends on the data structures used:
- For the queue used in BFS, in the worst case, all vertices might be in the queue simultaneously. Thus, the queue space complexity is $O(|V|)$.
- For storing the graph, if an adjacency list is used, the space complexity is $O(|V|+|E|)$.
- If an adjacency matrix is used, the space complexity becomes $O\left(|V|^2\right)$.
### Advanced Aspects of BFS
**Bipartite Testing**: BFS can be employed to check if a graph is bipartite. A graph is bipartite if its vertices can be divided into two disjoint sets where no two vertices within the same set are adjacent.

**Shortest Path**: For unweighted graphs, BFS provides the shortest path between the source vertex and any other vertex.

**Layered Approach**: BFS divides the graph into layers. The source vertex is layer 0, its neighbors are layer 1, and so on. This property can be utilized in various applications, such as network broadcasting.
### Use Cases of BFS:
- **Social Networks**: Finding people within a specific degree of connection.
- **Computer Networks**: Broadcasting in a network; BFS can help model this as it ensures minimal redundancy.
- **Pathfinding Algorithms**: BFS can be applied in 2D grids to find the shortest path, often used in games.
- **Web Crawlers**: BFS can help navigate the vast landscape of the web in layers.
- **Recommendation Systems**: By understanding the layers of connection, BFS can assist in making accurate recommendations.

## DFS: An Overview
Depth-First Search (DFS) is a pivotal graph traversal algorithm that explores as far down a branch as possible before backtracking. It starts at a source vertex and ventures deep into the graph following a path until it reaches an end, then retraces its steps and explores alternate routes.
### Mathematical Foundations
Graph Representation: DFS can be applied to both directed and undirected graphs. A graph $G$ is represented as $G=(V, E)$, where $V$ is the set of vertices and $E$ is the set of edges.
- Adjacency Matrix: $M[i][j]=1$ if there's an edge between vertex $i$ and vertex $j$, else $M[i][j]=0$.
- Adjacency List: For every vertex $v$, its neighbors are kept in a list.
Stack: DFS employs a Last-In-First-Out (LIFO) data structure called a Stack. Vertices are pushed onto the stack as DFS progresses and popped when backtracking.

DFS Tree: DFS yields a DFS tree, which is defined as $T=\left(V, E_T\right)$, where $E_T \subseteq E$. This tree illustrates the relationships between vertices as they are traversed by DFS.
### Algorithm Complexity
#### Time Complexity:
Since DFS visits each vertex and examines each edge once, the time complexity is:
$$O(|V|+|E|)$$
where $|V|$ signifies the number of vertices and $|E|$ denotes the number of edges.
#### Space Complexity:
The space efficiency is contingent upon the structures used:
- The stack in DFS, in the worst scenario, might be populated with all vertices. Thus, the space complexity of the stack is $O(|V|)$.
- If an adjacency list represents the graph, space complexity is $O(|V|+|E|)$.
- Using an adjacency matrix results in a space complexity of $O\left(|V|^2\right)$.

### Advanced Aspects of DFS
**Topological Sorting**: On Directed Acyclic Graphs (DAGs), DFS can facilitate topological ordering. This is crucial in scenarios like task scheduling.

**Cycle Detection**: DFS can be employed to discern cycles in a graph, which can be pivotal in numerous applications, such as detecting deadlocks.

**Connected Components**: In an undirected graph, DFS can assist in identifying connected components, which represent discrete clusters within the graph.

**Strongly Connected Components**: In directed graphs, DFS can be employed twice to pinpoint strongly connected components, an essential aspect in various graph applications.

**Path Finding**: DFS can locate a path between two vertices, but unlike BFS, it doesn't guarantee the shortest path in unweighted graphs.

### Use Cases of DFS:
- **Maze Solving Algorithms**: DFS can be used to solve mazes, creating a path from start to finish.
- **Dependency Resolution**: Systems like package managers use DFS for topological sorting to determine the order of installations.
- **Circuit Design**: In electronic circuit design, DFS assists in determining the connectivity of components.
- **Garbage Collection**: Modern garbage collectors employ DFS to detect objects that are no longer in use.
- **Decomposition of Graphs**: DFS aids in decomposing graphs into their constituent parts, simplifying complex graph structures.

## PageRank: An Overview

PageRank is an algorithm developed by Larry Page and Sergey Brin, co-founders of Google, during their time at Stanford University. Originally conceived to rank web pages in search results, it operates on the premise that the importance of a webpage can be determined by the number and quality of links pointing to it.

### Mathematical Foundations
Basic Principle: The PageRank of a page is the sum of a fraction of the PageRank of each page linking to it.

Given a graph $G$ of $N$ web pages with the set $P$ of pages and the set $E$ of links between them, the PageRank $P R\left(p_i\right)$ of page $p_i$ is given by:
$$P R\left(p_i\right)=(1-d)+d \times \sum_{p_j \in M\left(p_i\right)} \frac{P R\left(p_j\right)}{L\left(p_j\right)}$$
Where:
- $M\left(p_i\right)$ is the set of pages linking to $p_i$
- $L\left(p_j\right)$ is the number of outbound links on page $p_j$
- $d$ is the damping factor, typically set to 0.85
This can be represented in matrix form using a transition matrix and solved as an eigenvalue problem.

**Convergence**: The iterative computation of PageRank converges as it represents a Markov chain, especially since the web can be seen as a giant, stochastic graph.

### Algorithm Complexity
#### Time Complexity:
Computing PageRank through iterative methods requires repeated matrix multiplications. If we use simple matrix multiplication, the time complexity would be $O\left(N^3\right)$ for an $N \times N$ transition matrix. However, optimizations using sparse matrices or power iteration methods can reduce this considerably.
#### Space Complexity:
The main storage required is for the transition matrix. For a sparse matrix with $E$ non-zero entries (links), the space complexity is $O(N+E)$.

### Advanced Aspects of PageRank
**Damping Factor**: The introduction of the damping factor �d models the behavior where a surfer occasionally decides to jump to a random page rather than follow links endlessly. It ensures convergence of the algorithm and makes it less susceptible to manipulation.

**Taxation and Personalization**: The PageRank equation can be modified to introduce a tax vector which can be used to introduce personalization based on user preferences.

**Limitations and Tweaks**: Over time, webmasters tried to game the system by creating link farms and other manipulations. Google had to tweak and complement PageRank with other signals to maintain relevant search results.

### Use Cases:
- **Web Search**: The initial and most prominent use of PageRank was for ranking web pages in search results.
- **Academic Citations**: PageRank can be employed to rank scientific papers based on their citations, considering a paper that's widely cited as more influential.
- **Social Networks**: In platforms like Twitter, PageRank can be used to identify influential users or nodes within the network.
- **Recommendation Systems**: PageRank can assist in determining the importance of items within a large dataset, aiding in personalized recommendations.
- **Link Prediction**: In a network, PageRank can be used to predict the emergence of links, offering insights into future connections.

## Dijkstra's Algorithm and Fibonacci Heaps: An Overview
Dijkstra's algorithm is a cornerstone of graph theory, dedicated to finding the shortest path from a source vertex to every other vertex in a weighted graph. While the algorithm can be implemented with various priority queue structures, the Fibonacci Heap stands out as an efficient data structure, especially when the graph has a sparse set of edges.
### Mathematical Foundations
**Dijkstra's Algorithm Principle**: Starting from the source vertex, the algorithm repeatedly selects the vertex with the smallest distance, explores all its neighbors, and updates their distances.

**Fibonacci Heap**: It's a collection of trees satisfying the min-heap property. Key features include:

- Lazy handling of node reductions.
- Allows nodes to have a logarithmic degree.
- Amortized analysis ensures efficient operations.

**Combining Dijkstra and Fibonacci Heaps**: Dijkstra’s algorithm heavily depends on the "decrease key" and "delete" operations of priority queues. Fibonacci Heaps perform these operations in constant and logarithmic time, respectively, thus accelerating Dijkstra's algorithm in sparse graphs.

### Algorithm Complexity
Dijkstra's Standard Complexity: With basic priority queues, Dijkstra's time complexity is $O\left(|V|^2\right)$, but with binary heaps, it's $O((|V|+|E|) \log |V|)$.
Dijkstra with Fibonacci Heaps:
- Extract-Min operation: $O(\log V)$ amortized time.
- Decrease-Key operation: $O(1)$ amortized time.
Considering the above, the time complexity becomes:
$$O(|E|+|V| \log |V|)$$
This makes the Fibonacci Heap variant faster for graphs with fewer edges.

### Advanced Aspects of Dijkstra with Fibonacci Heaps
**Amortized Analysis**: The efficiency of Fibonacci Heaps doesn't always manifest in each operation but becomes evident when operations are considered in aggregate, making the overall process quicker.

**Limitations**:

- While Fibonacci Heaps are theoretically efficient, their constant factors and overhead make them slower in practice for most real-world datasets when compared to simpler structures like binary heaps.
- The structure of Fibonacci Heaps is more intricate, leading to more complex implementations.

**Variations and Optimizations**:

- For graphs with non-negative edge weights, Dijkstra's algorithm with Fibonacci Heaps is optimal. However, for graphs with negative weights, modifications and other algorithms, like Bellman-Ford, are required.
- Bidirectional Dijkstra's can be considered for further optimization in specific scenarios.
### Use Cases
- **Networking**: Employed in IP routing to determine the optimal path for data packet transfers.
- **Geographical Mapping Systems**: Finding the quickest route between two points.
- **Transportation**: Optimizing routes in logistics and cargo delivery.
- **Game Development**: AI pathfinding uses variants of Dijkstra's algorithm to move characters.
- **Telecommunication**: Routing calls and messages through optimal paths in the network.