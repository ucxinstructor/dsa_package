from os import link
import unittest
import random
import dsa.generators

class TestRandomArray(unittest.TestCase):

    def test_random_array_length(self):
        arr = dsa.generators.random_array(10)
        self.assertEqual(len(arr), 10)

    def test_random_array_value_range(self):
        min_val = 5
        max_val = 15
        arr = dsa.generators.random_array(20, min_val=min_val, max_val=max_val)
        for val in arr:
            self.assertGreaterEqual(val, min_val)
            self.assertLessEqual(val, max_val)

        self.assertEqual(arr.count, 20, "array should have 20  elements")

        min_val = -100
        max_val = 100
        arr = dsa.generators.random_array(10_000, min_val=min_val, max_val=max_val)
        for val in arr:
            self.assertGreaterEqual(val, min_val)
            self.assertLessEqual(val, max_val)
        self.assertEqual(arr.count, 10_000, "array should have 10,000 elements")

    def test_random_dynamicarray_value_range(self):
        min_val = 5
        max_val = 15
        arr = dsa.generators.random_dynamicarray(20, min_val=min_val, max_val=max_val)
        for val in arr:
            self.assertGreaterEqual(val, min_val)
            self.assertLessEqual(val, max_val)

        self.assertEqual(arr.count, 20, "Dynamic array should have 20  elements")

        min_val = -100
        max_val = 100
        arr = dsa.generators.random_dynamicarray(10_000, min_val=min_val, max_val=max_val)
        for val in arr:
            self.assertGreaterEqual(val, min_val)
            self.assertLessEqual(val, max_val)

        self.assertEqual(arr.count, 10_000, "Dynamic array should have 10,000 elements")

    def test_random_array_zero_length(self):
        arr = dsa.generators.random_array(0)
        self.assertEqual(len(arr), 0)
        self.assertIsInstance(arr, dsa.array.Array)
        arr = dsa.generators.random_dynamicarray(0)
        self.assertEqual(len(arr), 0)
        self.assertIsInstance(arr, dsa.array.DynamicArray)

    def test_random_stack(self):
        size = 5
        stack = dsa.generators.random_stack(size)
        self.assertEqual(len(stack), size)
        for _ in range(size):
            self.assertIsInstance(stack.pop(), int)

        size = 20_000
        stack = dsa.generators.random_stack(size)
        self.assertEqual(len(stack), size)
        for _ in range(size):
            self.assertIsInstance(stack.pop(), int)

    def test_random_dynamic_stack(self):
        size = 5
        stack = dsa.generators.random_dynamic_stack(size)
        self.assertEqual(len(stack), size)
        for _ in range(size):
            self.assertIsInstance(stack.pop(), int)

        size = 20_000
        stack = dsa.generators.random_dynamic_stack(size)
        self.assertEqual(len(stack), size)
        for _ in range(size):
            self.assertIsInstance(stack.pop(), int)

    def test_random_queue(self):
        size = 5
        queue = dsa.generators.random_queue(size)
        self.assertEqual(len(queue), size)
        for _ in range(size):
            self.assertIsInstance(queue.dequeue(), int)

        size = 20_000
        queue = dsa.generators.random_queue(size)
        self.assertEqual(len(queue), size)
        for _ in range(size):
            self.assertIsInstance(queue.dequeue(), int)

    def test_random_dynamic_queue(self):
        size = 5
        queue = dsa.generators.random_dynamic_queue(size)
        self.assertEqual(len(queue), size)
        for _ in range(size):
            self.assertIsInstance(queue.dequeue(), int)

        size = 20_000
        queue = dsa.generators.random_dynamic_queue(size)
        self.assertEqual(len(queue), size)
        for _ in range(size):
            self.assertIsInstance(queue.dequeue(), int)

    def test_random_deque(self):
        size = 5
        deque = dsa.generators.random_deque(size)
        self.assertEqual(len(deque), size)
        for _ in range(size):
            if random.choice([True, False]):
                self.assertIsInstance(deque.pop_left(), int)
            else:
                self.assertIsInstance(deque.pop_right(), int)
        size = 20_000
        deque = dsa.generators.random_deque(size)
        self.assertEqual(len(deque), size)
        for _ in range(size):
            if random.choice([True, False]):
                self.assertIsInstance(deque.pop_left(), int)
            else:
                self.assertIsInstance(deque.pop_right(), int)

    def test_random_linked_list(self):
        size = 5
        linked_list = dsa.generators.random_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for _ in range(size):
            linked_list.delete(0)
        self.assertEqual(len(linked_list), 0)

        size = 20_000
        linked_list = dsa.generators.random_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for _ in range(size):
            linked_list.delete(0)
        self.assertEqual(len(linked_list), 0)

    def test_random_doubly_linked_list(self):
        size = 5
        linked_list = dsa.generators.random_doubly_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for _ in range(size):
            linked_list.delete(0)
        self.assertEqual(len(linked_list), 0)

        size = 20_000
        linked_list = dsa.generators.random_doubly_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for _ in range(size):
            linked_list.delete(0)
        self.assertEqual(len(linked_list), 0)

    def test_random_binary_tree(self):
        n = 5
        tree = dsa.generators.random_binary_tree(n)
        self.assertIsInstance(tree, dsa.tree.Tree)
        self.assertEqual(len(tree), n)

        n = 20_000
        tree = dsa.generators.random_binary_tree(n)
        self.assertIsInstance(tree, dsa.tree.Tree)
        self.assertEqual(len(tree), n)

    def test_random_heap(self):
        size = 5
        heap = dsa.generators.random_heap(size)
        self.assertEqual(len(heap), size)
        for _ in range(size):
            self.assertIsInstance(heap.pop(), int)

        size = 20_000
        heap = dsa.generators.random_heap(size)
        self.assertEqual(len(heap), size)
        for _ in range(size):
            self.assertIsInstance(heap.pop(), int)


    def test_random_trie(self):
        n = 5
        trie = dsa.generators.random_trie(n)
        self.assertIsInstance(trie, dsa.trie.Trie)
#        self.assertEqual(len(trie), n)

        n = 20_000
        trie = dsa.generators.random_trie(n)
        self.assertIsInstance(trie, dsa.trie.Trie)
 #       self.assertEqual(len(trie), n)

    def test_linear_stack(self):
        size = 5
        stack = dsa.generators.linear_stack(size)
        self.assertEqual(len(stack), size)
        for i in range(size):
            self.assertEqual(stack.pop(), size - i - 1)

        size = 1_000
        stack = dsa.generators.linear_stack(size)
        self.assertEqual(len(stack), size)
        for i in range(size):
            self.assertEqual(stack.pop(), size - i - 1)
    
    def test_linear_dynamic_stack(self):
        size = 5
        stack = dsa.generators.linear_dynamic_stack(size)
        self.assertEqual(len(stack), size)
        for i in range(size):
            self.assertEqual(stack.pop(), size - i - 1)

        size = 1_000
        stack = dsa.generators.linear_dynamic_stack(size)
        self.assertEqual(len(stack), size)
        for i in range(size):
            self.assertEqual(stack.pop(), size - i - 1)
    
    def test_linear_queue(self):
        size = 5
        queue = dsa.generators.linear_queue(size)
        self.assertEqual(len(queue), size)
        for i in range(size):
            self.assertEqual(queue.dequeue(), i)

        size = 1_000
        queue = dsa.generators.linear_queue(size)
        self.assertEqual(len(queue), size)
        for i in range(size):
            self.assertEqual(queue.dequeue(), i)
    
    def test_linear_dynamic_queue(self):
        size = 5
        queue = dsa.generators.linear_dynamic_queue(size)
        self.assertEqual(len(queue), size)
        for i in range(size):
            self.assertEqual(queue.dequeue(), i)

        size = 1_000
        queue = dsa.generators.linear_dynamic_queue(size)
        self.assertEqual(len(queue), size)
        for i in range(size):
            self.assertEqual(queue.dequeue(), i)

    def test_linear_linked_list(self):
        size = 5
        linked_list = dsa.generators.linear_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for i in range(size):
            self.assertEqual(linked_list[i], i)

        size = 1_000
        linked_list = dsa.generators.linear_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for i in range(size):
            self.assertEqual(linked_list[i], i)

    def test_linear_doubly_linked_list(self):
        size = 5
        linked_list = dsa.generators.linear_doubly_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for i in range(size):
            self.assertEqual(linked_list[i], i)

        size = 1_000
        linked_list = dsa.generators.linear_doubly_linked_list(size)
        self.assertEqual(len(linked_list), size)
        for i in range(size):
            self.assertEqual(linked_list[i], i)

    def test_random_adjacency_matrix_graph(self):
        # undirected
        n = 5
        graph = dsa.generators.random_adjacency_matrix_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixGraph)
        graph.print_graph()

        n = 1_000
        graph = dsa.generators.random_adjacency_matrix_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixGraph)
    
        # directed
        n = 5
        graph = dsa.generators.random_adjacency_matrix_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixGraph)
        graph.print_graph()

        n = 1_000
        graph = dsa.generators.random_adjacency_matrix_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixGraph)

    def test_random_adjacency_matrix_weighted_graph(self):
        # undirected
        n = 5
        graph = dsa.generators.random_adjacency_matrix_weighted_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixWeightedGraph)
        graph.print_graph()

        n = 1_000
        graph = dsa.generators.random_adjacency_matrix_weighted_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixWeightedGraph)

        # directed
        n = 5
        graph = dsa.generators.random_adjacency_matrix_weighted_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixWeightedGraph)
        graph.print_graph()

        n = 1_000
        graph = dsa.generators.random_adjacency_matrix_weighted_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyMatrixWeightedGraph)

    def test_random_adjacency_list_graph(self):
        # undirected
        n = 5
        graph = dsa.generators.random_adjacency_list_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListGraph)

        n = 1_000
        graph = dsa.generators.random_adjacency_list_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListGraph)

        # directed
        n = 5
        graph = dsa.generators.random_adjacency_list_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListGraph)

        n = 1_000
        graph = dsa.generators.random_adjacency_list_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListGraph)

    def test_random_adjacency_list_weighted_graph(self):
        # undirected
        n = 5
        graph = dsa.generators.random_adjacency_list_weighted_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListWeightedGraph)

        n = 1_000
        graph = dsa.generators.random_adjacency_list_weighted_graph(n, directed=False)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListWeightedGraph)

        # directed
        n = 5
        graph = dsa.generators.random_adjacency_list_weighted_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListWeightedGraph)

        n = 1_000
        graph = dsa.generators.random_adjacency_list_weighted_graph(n, directed=True)
        self.assertIsInstance(graph, dsa.graph.AdjacencyListWeightedGraph)

if __name__ == '__main__':
    unittest.main()
