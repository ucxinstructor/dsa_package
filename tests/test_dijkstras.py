import unittest
from dsa.dijkstras import shortest_path
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

if __name__ == '__main__':
    unittest.main()