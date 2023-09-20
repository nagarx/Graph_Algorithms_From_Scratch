import math

# Node class for Fibonacci heap
class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        self.next = self
        self.prev = self

# FibonacciHeap class
class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

# Initialize the heap with a singleton tree containing node x
def insert(heap, x):
    if heap.min_node is None:
        heap.min_node = x
    else:
        x.prev = heap.min_node
        x.next = heap.min_node.next
        heap.min_node.next.prev = x
        heap.min_node.next = x
        if x.key < heap.min_node.key:
            heap.min_node = x
    heap.num_nodes += 1

# Extract the minimum node from the Fibonacci heap
# Implementing the extract_min function for a Fibonacci Heap
def extract_min(heap):
    z = heap.min_node
    if z is not None:
        # Add children of z to the root list
        x = z.child
        if x is not None:
            for _ in range(z.degree):
                y = x.next  # store the next child before modifying x
                # Add x to the root list
                x.prev = heap.min_node
                x.next = heap.min_node.next
                heap.min_node.next.prev = x
                heap.min_node.next = x
                x.parent = None
                x = y  # move to the next child

        # Remove z from the root list
        z.prev.next = z.next
        z.next.prev = z.prev

        # If z is the only node in the root list, set min_node to None
        if heap.min_node == z and z.next == z:
            heap.min_node = None
        else:
            heap.min_node = z.next
            consolidate(heap)  # Reorganize the heap

        heap.num_nodes -= 1  # Decrease the total number of nodes in the heap

    return z

# Union of two Fibonacci heaps
def union(heap1, heap2):
    new_heap = FibonacciHeap()
    new_heap.min_node = heap1.min_node
    if new_heap.min_node is not None and heap2.min_node is not None:
        heap1.min_node.next.prev = heap2.min_node.prev
        heap2.min_node.prev.next = heap1.min_node.next
        heap1.min_node.next = heap2.min_node
        heap2.min_node.prev = heap1.min_node
        if heap2.min_node.key < heap1.min_node.key:
            new_heap.min_node = heap2.min_node
    new_heap.num_nodes = heap1.num_nodes + heap2.num_nodes
    return new_heap

# Decrease the key of a node in the Fibonacci heap
def decrease_key(heap, x, k):
    if k > x.key:
        raise ValueError("New key is greater than the current key")
    x.key = k
    y = x.parent
    if y is not None and x.key < y.key:
        cut(heap, x, y)
        cascading_cut(heap, y)
    if x.key < heap.min_node.key:
        heap.min_node = x

def remove_from_list(x):
    x.prev.next = x.next
    x.next.prev = x.prev


# Cut a node x from its parent y and add it to the root list
def cut(heap, x, y):
    remove_from_list(x)
    y.degree -= 1
    if y.child == x:
        y.child = x.next
    if y.degree == 0:
        y.child = None
    x.prev = heap.min_node
    x.next = heap.min_node.next
    heap.min_node.next.prev = x
    heap.min_node.next = x
    x.parent = None
    x.mark = False

# Cascading cut of a node y in the Fibonacci heap
def cascading_cut(heap, y):
    z = y.parent
    if z is not None:
        if y.mark == False:
            y.mark = True
        else:
            cut(heap, y, z)
            cascading_cut(heap, z)

# Delete a node x from the Fibonacci heap
def delete_node(heap, x):
    decrease_key(heap, x, float('-inf'))
    extract_min(heap)

# Implementing the consolidate function for a Fibonacci Heap
def consolidate(heap):
    D = int(math.log(heap.num_nodes) / math.log(2)) if heap.num_nodes > 0 else 0
    A = [None] * (D + 1)

    w = heap.min_node
    nodes = []
    if w is not None:
        node = w
        while True:
            nodes.append(node)
            node = node.next
            if node == w:
                break

    for w in nodes:
        x = w
        d = x.degree
        while A[d] is not None:
            y = A[d]
            if x.key > y.key:
                x, y = y, x

            # Link y to x
            y.prev.next = y.next
            y.next.prev = y.prev

            y.next = y
            y.prev = y

            if x.child is None:
                x.child = y
            else:
                y.prev = x.child
                y.next = x.child.next
                x.child.next.prev = y
                x.child.next = y

            y.parent = x
            x.degree += 1
            y.mark = False

            A[d] = None
            d += 1

        A[d] = x

    heap.min_node = None
    for i in range(D + 1):
        if A[i]:
            if heap.min_node is None:
                heap.min_node = A[i]
            elif A[i].key < heap.min_node.key:
                heap.min_node = A[i]

# Helper function to link two trees in Fibonacci Heap
def link(heap, y, x):
    # Remove y from root list
    y.prev.next = y.next
    y.next.prev = y.prev
    # Make y a child of x
    y.parent = x
    if x.child is None:
        x.child = y
        y.next = y
        y.prev = y
    else:
        y.prev = x.child
        y.next = x.child.next
        x.child.next.prev = y
        x.child.next = y
    x.degree += 1
    y.mark = False




