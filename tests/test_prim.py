import unittest
from dsa.prim import is_equal_set, prims_mst, mst_weight
from dsa.graph import AdjacencyListWeightedGraph

class TestPrim(unittest.TestCase):

    def setUp(self):
        self.graph = AdjacencyListWeightedGraph()
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('B', 'D', 5)
        self.graph.add_edge('C', 'D', 3)

    def test_is_equal_set(self):
        visited = {'A', 'B', 'C'}
        edges = [('A', 'B'), ('B', 'C')]
        self.assertTrue(is_equal_set(visited, edges))

        visited = {'A', 'B'}
        edges = [('A', 'B'), ('B', 'C')]
        self.assertFalse(is_equal_set(visited, edges))

    def test_prims_mst(self):
        mst = prims_mst(self.graph, 'A')
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

    def test_mst_weight(self):
        mst = prims_mst(self.graph, 'A')
        total_weight = mst_weight(mst)
        self.assertEqual(total_weight, 6)

if __name__ == '__main__':
    unittest.main()