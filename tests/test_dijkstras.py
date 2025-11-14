import unittest
from dsa.dijkstras import shortest_path, find_path
from dsa.graph import AdjacencyListWeightedGraph

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = AdjacencyListWeightedGraph()
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('B', 'D', 5)
        self.graph.add_edge('C', 'D', 1)

    def test_shortest_path(self):
        weight_table, previous = shortest_path(self.graph, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)
        self.assertEqual(previous['D'], 'C')
        self.assertEqual(previous['C'], 'B')
        self.assertEqual(previous['B'], 'A')

    def test_shortest_path_same_start_end(self):
        weight_table, previous = shortest_path(self.graph, 'A', 'A')
        self.assertEqual(weight_table['A'], 0)
        self.assertEqual(previous['A'], 'A')

    def test_shortest_path_no_path(self):
        self.graph.add_edge('E', 'E', 0)
        weight_table, previous = shortest_path(self.graph, 'A', 'E')
        self.assertNotIn('E', weight_table)
        self.assertNotIn('E', previous)

    def test_graph_with_cycle(self):
        # Add cycle C → A with big weight
        self.graph.add_edge('C', 'A', 10)
        weight_table, previous = shortest_path(self.graph, 'A', 'D')
        # Should still produce the same shortest path as before
        self.assertEqual(weight_table['D'], 4)

    def test_multiple_equal_paths(self):
        # Add another equally-weighted path A → X → D
        self.graph.add_edge('A', 'X', 2)
        self.graph.add_edge('X', 'D', 2)
        weight_table, previous = shortest_path(self.graph, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)
        # Path may be A-B-C-D or A-X-D; both valid
        self.assertIn(previous['D'], ('C', 'X'))

    def test_disconnected_graph(self):
        # Add entirely separate component
        self.graph.add_edge('X', 'Y', 1)
        weight_table, previous = shortest_path(self.graph, 'A', 'Y')
        self.assertNotIn('Y', weight_table)

    def test_heavier_direct_edge(self):
        # Add direct but worse path
        self.graph.add_edge('A', 'D', 100)
        weight_table, previous = shortest_path(self.graph, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)

    def test_zero_weight_edges(self):
        # Add zero-weight shortcuts
        self.graph.add_edge('A', 'Z', 0)
        self.graph.add_edge('Z', 'D', 0)
        weight_table, previous = shortest_path(self.graph, 'A', 'D')
        self.assertEqual(weight_table['D'], 0)
        self.assertEqual(previous['D'], 'Z')
        self.assertEqual(previous['Z'], 'A')

    def test_large_linear_chain(self):
        # Long path A → B → C → ... → J
        g = AdjacencyListWeightedGraph()
        letters = "ABCDEFGHIJ"
        for i in range(len(letters)-1):
            g.add_edge(letters[i], letters[i+1], 1)
        weight_table, previous = shortest_path(g, 'A', 'J')
        self.assertEqual(weight_table['J'], 9)
        self.assertEqual(previous['J'], 'I')

    def test_end_not_in_graph(self):
        with self.assertRaises(KeyError):
            weight_table, previous = shortest_path(self.graph, 'A', 'ZZZ')
    
class TestFindPath(unittest.TestCase):
    def setUp(self):
        self.graph = AdjacencyListWeightedGraph()
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('B', 'D', 5)
        self.graph.add_edge('C', 'D', 1)

    def test_find_path_basic(self):
        path = find_path(self.graph, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])

    def test_find_path_same_start_end(self):
        path = find_path(self.graph, 'A', 'A')
        self.assertEqual(path, ['A'])

    def test_find_path_no_path(self):
        # Add isolated E
        self.graph.add_edge('E', 'E', 0)
        with self.assertRaises(KeyError):
            # predecessor['E'] will not exist → KeyError expected
            find_path(self.graph, 'A', 'E')

    def test_find_path_intermediate(self):
        path = find_path(self.graph, 'A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])

    def test_find_path_debug_output(self):
        # Just verify it runs; no exception
        path = find_path(self.graph, 'A', 'D', debug=True)
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        
if __name__ == '__main__':
    unittest.main()