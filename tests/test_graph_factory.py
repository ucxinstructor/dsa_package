from re import A
import unittest

from dsa.graph import Graph, AdjacencyListGraph, AdjacencyMatrixGraph, AdjacencyListWeightedGraph, AdjacencyMatrixWeightedGraph

class TestGraphFactory(unittest.TestCase):
    def test_graph_factory(self):
        g1 = Graph.create(graph_type='adjacency_list', directed=False, weighted=False)
        self.assertIsInstance(g1, AdjacencyListGraph)
        self.assertFalse(g1.is_directed)
        self.assertFalse(g1.is_weighted)
        
        g1 = Graph.create_adjacency_list()
        self.assertIsInstance(g1, AdjacencyListGraph)
        self.assertFalse(g1.is_directed)
        self.assertFalse(g1.is_weighted)


        g2 = Graph.create(graph_type='adjacency_matrix', directed=True, weighted=False)
        self.assertIsInstance(g2, AdjacencyMatrixGraph)
        self.assertTrue(g2.is_directed)
        self.assertFalse(g2.is_weighted)

        g2 = Graph.create_adjacency_matrix()
        self.assertIsInstance(g2, AdjacencyMatrixGraph)
        self.assertFalse(g2.is_directed)
        self.assertFalse(g2.is_weighted)
        
        g3 = Graph.create(graph_type='adjacency_list', directed=False, weighted=True)
        self.assertIsInstance(g3, AdjacencyListWeightedGraph)
        self.assertFalse(g3.is_directed)
        self.assertTrue(g3.is_weighted)
        
        g3 = Graph.create_adjacency_list(weighted=True)
        self.assertIsInstance(g3, AdjacencyListWeightedGraph)
        self.assertFalse(g3.is_directed)
        self.assertTrue(g3.is_weighted)
        
        g4 = Graph.create(graph_type='adjacency_matrix', directed=True, weighted=True)
        self.assertIsInstance(g4, AdjacencyMatrixWeightedGraph)
        self.assertTrue(g4.is_directed)
        self.assertTrue(g4.is_weighted)
        
        g4 = Graph.create_adjacency_matrix(directed=True, weighted=True)
        self.assertIsInstance(g4, AdjacencyMatrixWeightedGraph)
        self.assertTrue(g4.is_directed)
        self.assertTrue(g4.is_weighted)
        
        with self.assertRaises(ValueError):
            Graph.create(graph_type='unknown_type')

    def test_graph_from_dict(self):
        # adjacency list graphs
        dict_tests = [
            {'A': ['B'], 'B': ['A']},
            {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']},
            {'1': ['2', '3'], '2': ['1'], '3': ['1']},
            {'X': ['Y'], 'Y': ['X', 'Z'], 'Z': ['Y']},
            {}
        ]           

        for data in dict_tests:
            g = Graph.from_dict(data, graph_type='adjacency_list', directed=False, weighted=False)
            self.assertIsInstance(g, AdjacencyListGraph)
            self.assertEqual(g.to_dict(), data)

            g = Graph.from_dict(data, graph_type='adjacency_list', directed=True, weighted=False)
            self.assertIsInstance(g, AdjacencyListGraph)
            self.assertEqual(g.to_dict(), data)

        dict_weighted_tests = [
            {'A': {'B': 1}, 'B': {'A': 1}},
            {'A': {'B': 2, 'C': 3}, 'B': {'A': 2, 'C': 4}, 'C': {'A': 3, 'B': 4}},
            {'1': {'2': 5, '3': 10}, '2': {'1': 5}, '3': {'1': 10}},
            {'X': {'Y': 1}, 'Y': {'X': 1, 'Z': 2}, 'Z': {'Y': 2}},
            {}
        ]

        for data_weighted in dict_weighted_tests:
            g_weighted = Graph.from_dict(data_weighted, graph_type='adjacency_list', directed=False, weighted=True)
            self.assertIsInstance(g_weighted, AdjacencyListWeightedGraph)
            self.assertEqual(g_weighted.to_dict(), data_weighted)

            g_weighted = Graph.from_dict(data_weighted, graph_type='adjacency_list', directed=True, weighted=True)
            self.assertIsInstance(g_weighted, AdjacencyListWeightedGraph)
            self.assertEqual(g_weighted.to_dict(), data_weighted)

        # adjacency matrix graphs
        for data in dict_tests:
            g = Graph.from_dict(data, graph_type='adjacency_matrix', directed=False, weighted=False)
            self.assertIsInstance(g, AdjacencyMatrixGraph)
            self.assertEqual(g.to_dict(), data)

            g = Graph.from_dict(data, graph_type='adjacency_matrix', directed=True, weighted=False)
            self.assertIsInstance(g, AdjacencyMatrixGraph)
            self.assertEqual(g.to_dict(), data)

        for data_weighted in dict_weighted_tests:
            g_weighted = Graph.from_dict(data_weighted, graph_type='adjacency_matrix', directed=False, weighted=True)
            self.assertIsInstance(g_weighted, AdjacencyMatrixWeightedGraph)
            self.assertEqual(g_weighted.to_dict(), data_weighted)

            g_weighted = Graph.from_dict(data_weighted, graph_type='adjacency_matrix', directed=True, weighted=True)
            self.assertIsInstance(g_weighted, AdjacencyMatrixWeightedGraph)
            self.assertEqual(g_weighted.to_dict(), data_weighted)


        
        
            
class TestAdjacencyListGraph(unittest.TestCase):
    def test_create_undirected(self):
        g = AdjacencyListGraph(directed=False)
        self.assertEqual(g.order(), 0)
        self.assertEqual(len(g), 0)
        self.assertEqual(g.size(), 0)

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_vertex('D')
        self.assertEqual(g.order(), 4)
        self.assertEqual(len(g), 4)
        self.assertEqual(g.size(), 2)
        
        self.assertEqual(g['A'], ['B', 'C'])
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('A', 'D'))
        
        self.assertSetEqual(set(g.vertices()), {'A', 'B', 'C', 'D'})

        g.add_edge('B', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'F')
        g.add_edge('F', 'G')
        
        self.assertEqual(g.order(), 7)
        self.assertEqual(len(g), 7)
        self.assertEqual(g.size(), 8)

        self.assertEqual(g['A'], ['B', 'C'])
        self.assertEqual(g['E'], ['D', 'F'])
        self.assertSetEqual(set(g.edges()), 
                            {('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'B'), ('D', 'C'), ('D', 'E'), ('E', 'D'), ('E', 'F'), ('F', 'E'), ('F', 'G'), ('G', 'F')})

        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("G"), ["G", "F", "E", "D", "B", "A", "C"])
        # self.assertEqual(g.bfs_traverse("G"), ["G", "F", "E", "D", "B", "C", "A"])

        g = AdjacencyListGraph(directed=False)
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)
        self.assertEqual(g.size(), 2)

        g.add_edge("B", 'D')
        g.add_edge("B", 'E')
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)
        self.assertEqual(g.size(), 4)

        g.add_edge("C", 'F')
        
        self.assertEqual(g.order(), 6)
        self.assertEqual(len(g), 6)
        self.assertEqual(g.size(), 5)
        
        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F"])
        
        
    def test_create_directed(self):
        g = AdjacencyListGraph(directed=True)
        self.assertEqual(g.order(), 0)
        self.assertEqual(len(g), 0)
        self.assertEqual(g.size(), 0)

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)
        self.assertEqual(g.size(), 5)
        
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], ['B'])
        self.assertEqual(g['E'], ['A'])
        self.assertSetEqual(set(g.edges()), {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')})
        
    def test_weighted_graph(self):
        g = AdjacencyListWeightedGraph(directed=False)
        self.assertEqual(g.order(), 0)
        self.assertEqual(len(g), 0)
        self.assertEqual(g.size(), 0)
        
        g.add_edge('A', 'B', weight=5)
        g.add_edge('A', 'C', weight=10)
        g.add_edge('B', 'C', weight=2)
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)
        self.assertEqual(g.size(), 3)
        
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('A', 'C'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertTrue(g.has_edge('C', 'A'))
        self.assertTrue(g.has_edge('C', 'B'))

        self.assertListEqual(list(g['A'].keys()), ['B', 'C'])
        self.assertListEqual(list(g['B'].keys()), ['A', 'C'])
        self.assertListEqual(list(g['C'].keys()), ['A', 'B'])

        self.assertEqual(g.get_weight('A', 'B'), 5)
        self.assertEqual(g.get_weight('A', 'C'), 10)
        self.assertEqual(g.get_weight('B', 'C'), 2)
        
    def test_weighted_directed_graph(self):
        g = AdjacencyListWeightedGraph(directed=True)
        self.assertEqual(g.order(), 0)
        self.assertEqual(len(g), 0)
        self.assertEqual(g.size(), 0)
        
        g.add_edge('A', 'B', weight=3)
        g.add_edge('B', 'C', weight=4)
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)
        self.assertEqual(g.size(), 2)
        
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertFalse(g.has_edge('C', 'B'))

        self.assertListEqual(list(g['A'].keys()), ['B'])
        self.assertListEqual(list(g['B'].keys()), ['C'])
        self.assertListEqual(list(g['C'].keys()), [])

        self.assertEqual(g.get_weight('A', 'B'), 3)
        self.assertEqual(g.get_weight('B', 'C'), 4)
    
    def test_no_edge_undirected_graph(self):
        g = AdjacencyListGraph(directed=False, vertices=['A', 'B', 'C', 'D'])
        self.assertEqual(g.order(), 4)
        self.assertEqual(len(g), 4)
        self.assertEqual(g.size(), 0)   
        g.add_vertex('E') 
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)
        self.assertEqual(g.size(), 0)
        with self.assertRaises(ValueError):
            g.add_vertex('B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertEqual(g['A'], [])
        self.assertEqual(g['B'], [])
        self.assertEqual(g['E'], [])
        self.assertEqual(g.edges(), [])

    def test_delete_edge_directed(self):
        g = AdjacencyListGraph(directed=True)
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], ['B'])
        self.assertEqual(g['B'], ['C'])

        self.assertEqual(g.size(), 5)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'C'))

        self.assertFalse(g.has_edge('A', 'B'))
        self.assertEqual(g.size(), 4)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)

        with self.assertRaises(KeyError):
            g.delete_edge('B', 'A')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertEqual(g.size(), 4)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)

        g.add_edge('A', 'B')
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertEqual(g.size(), 5)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertEqual(g.size(), 4)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)

    def test_delete_edge_undirected(self):
        g = AdjacencyListGraph(directed=False)
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')
        self.assertEqual(g.size(), 5)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], ['B', 'E'])
        self.assertEqual(g['B'], ['A', 'C'])

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        with self.assertRaises(KeyError):
            g.delete_edge('B', 'A')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        g.add_edge('B', 'A')
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertEqual(g.size(), 4)
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)
        
    def test_weighted_undirected_graph_delete_edge(self):
        g = AdjacencyListWeightedGraph(directed=False)
        g.add_edge('A', 'B', weight=5)
        g.add_edge('A', 'C', weight=10)
        g.add_edge('B', 'C', weight=2)
        self.assertEqual(g.size(), 3)
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('A', 'C'))
        self.assertTrue(g.has_edge('C', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertTrue(g.has_edge('C', 'B'))
        self.assertEqual(g.size(), 2)
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)
        
    def test_weighted_directed_graph_delete_edge(self):
        g = AdjacencyListWeightedGraph(directed=True)
        g.add_edge('A', 'B', weight=3)
        g.add_edge('B', 'C', weight=4)
        self.assertEqual(g.size(), 2)
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertFalse(g.has_edge('C', 'B'))
        self.assertEqual(g.size(), 1)
        self.assertEqual(g.order(), 3)
        self.assertEqual(len(g), 3)
