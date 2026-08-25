import unittest
from dsa.prim import prim, reconstruct_mst, get_mst, prim_simple, mst_weight
from dsa.graph import Graph

class TestPrim(unittest.TestCase):

    def setUp(self):
        self.graph = Graph.create_adjacency_list(directed=False, weighted=True)
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('B', 'D', 5)
        self.graph.add_edge('C', 'D', 3)

    def test_get_mst(self):
        mst = get_mst(self.graph, 'A')
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

    def test_prim(self):
        weight_table, predecessor_table = prim(self.graph, 'A')
        self.assertEqual(weight_table, {'A': 0, 'B': 1, 'C': 3, 'D': 6})
        self.assertEqual(predecessor_table, {'A': 'A', 'B': 'A', 'C': 'B', 'D': 'C'})

    def test_reconstruct_mst(self):
        weight_table, predecessor_table = prim(self.graph, 'A')
        mst = reconstruct_mst(predecessor_table, weight_table)
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

    def test_prim_simple(self):
        mst = prim_simple(self.graph, 'A')
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

    def test_mst_weight(self):
        mst = get_mst(self.graph, 'A')
        total_weight = mst_weight(mst)
        self.assertEqual(total_weight, 6)

if __name__ == '__main__':
    unittest.main()