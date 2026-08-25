import unittest
from dsa.prim import prim, reconstruct_mst, get_mst, prim_simple, get_total_weight
from dsa.graph import Graph

class TestPrim(unittest.TestCase):

    def setUp(self):
        self.graph = Graph.create_adjacency_list(directed=False, weighted=True)
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('B', 'D', 5)
        self.graph.add_edge('C', 'D', 3)

        # create a graph with a cycle
        self.graph_with_cycle = Graph.create_adjacency_list(directed=False, weighted=True)
        self.graph_with_cycle.add_edge('A', 'B', 1)
        self.graph_with_cycle.add_edge('B', 'C', 2)
        self.graph_with_cycle.add_edge('C', 'A', 3)  # This creates a cycle A -> B -> C -> A
        self.graph_with_cycle.add_edge('C', 'D', 4)

    def test_get_mst(self):
        mst = get_mst(self.graph, 'A')
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

        mst_with_cycle = get_mst(self.graph_with_cycle, 'A')
        mst_with_cycle_edges = mst_with_cycle.undirected_edges()
        expected_edges_with_cycle = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 4)]
        self.assertEqual(sorted(mst_with_cycle_edges), sorted(expected_edges_with_cycle))

    def test_prim(self):
        weight_table, predecessor_table = prim(self.graph, 'A')
        self.assertEqual(weight_table, {'A': 0, 'B': 1, 'C': 2, 'D': 3})
        self.assertEqual(predecessor_table, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'})

        weight_table_with_cycle, predecessor_table_with_cycle = prim(self.graph_with_cycle, 'A')
        self.assertEqual(weight_table_with_cycle, {'A': 0, 'B': 1, 'C': 2, 'D': 4})
        self.assertEqual(predecessor_table_with_cycle, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'})

    def test_reconstruct_mst(self):
        weight_table, predecessor_table = prim(self.graph, 'A')
        mst = reconstruct_mst(weight_table, predecessor_table)
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

        weight_table_with_cycle, predecessor_table_with_cycle = prim(self.graph_with_cycle, 'A')
        mst_with_cycle = reconstruct_mst(weight_table_with_cycle, predecessor_table_with_cycle)
        mst_with_cycle_edges = mst_with_cycle.undirected_edges()
        expected_edges_with_cycle = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 4)]
        self.assertEqual(sorted(mst_with_cycle_edges), sorted(expected_edges_with_cycle))

    def test_prim_simple(self):
        mst = prim_simple(self.graph, 'A')
        mst_edges = mst.undirected_edges()
        expected_edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3)]
        self.assertEqual(sorted(mst_edges), sorted(expected_edges))

        mst_with_cycle = prim_simple(self.graph_with_cycle, 'A')
        mst_with_cycle_edges = mst_with_cycle.undirected_edges()
        expected_edges_with_cycle = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 4)]
        self.assertEqual(sorted(mst_with_cycle_edges), sorted(expected_edges_with_cycle))

    def test_mst_weight(self):
        mst = get_mst(self.graph, 'A')
        total_weight = get_total_weight(mst)
        self.assertEqual(total_weight, 6)

        mst_with_cycle = get_mst(self.graph_with_cycle, 'A')
        total_weight_with_cycle = get_total_weight(mst_with_cycle)
        self.assertEqual(total_weight_with_cycle, 7) 

if __name__ == '__main__':
    unittest.main()