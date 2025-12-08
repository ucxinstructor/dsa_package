from dsa.graph import Graph, AdjacencyListGraph, AdjacencyMatrixGraph, AdjacencyListWeightedGraph, AdjacencyMatrixWeightedGraph

import unittest

class TestGraphMatrix(unittest.TestCase):
    def test_create_undirected(self):
        g = AdjacencyMatrixGraph(directed=False)
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_vertex('D')
        self.assertEqual(g['A'], ['B', 'C'])
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('A', 'D'))
        self.assertEqual(g.order(), 4)
        self.assertEqual(len(g), 4)
        self.assertEqual(g.size(), 2)
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
        
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixWeightedGraph(directed=True, vertices=vertices)
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('C', 'D', 3)
        g.add_edge('D', 'E', 4)
        g.add_edge('E', 'A', 5)
        self.assertTrue(g.has_edge('A', 'B'))
        print("Edge? ", g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('B', 'A'))


        
    def test_create_directed(self):
        g = AdjacencyMatrixGraph(directed=True)
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
        
    def test_no_edge_undirected_graph(self):
        g = AdjacencyMatrixGraph(directed=False, vertices=['A', 'B', 'C', 'D'])
        self.assertEqual(g.order(), 4)
        self.assertEqual(len(g), 4)
        g.add_vertex('E') 
        g.print_graph()
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
        
    def test_no_edge_directed_graph(self):
        g = AdjacencyMatrixGraph(directed=True, vertices=['A', 'B', 'C', 'D'])
        g.add_vertex('E') 
        g.print_graph()
        self.assertEqual(g.order(), 5)
        self.assertEqual(len(g), 5)
        self.assertEqual(g.size(), 0)

        with self.assertRaises(ValueError):
            g.add_vertex('C')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertEqual(g['A'], [])
        self.assertEqual(g['B'], [])
        self.assertEqual(g['E'], [])
        self.assertEqual(g.edges(), [])
        
    def test_delete_edge_undirected(self):
        g = AdjacencyMatrixGraph(directed=False)
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')
        
        self.assertTrue(g.size(), 5)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)

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
        
        self.assertTrue(g.size(), 4)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)


    def test_delete_edge_directed(self):
        g = AdjacencyMatrixGraph(directed=True)
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')

        self.assertTrue(g.size(), 5)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], ['B'])
        self.assertEqual(g['B'], ['C'])

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'C'))

        self.assertFalse(g.has_edge('A', 'B'))

        with self.assertRaises(KeyError):
            g.delete_edge('B', 'A')
        self.assertFalse(g.has_edge('A', 'B'))

        g.add_edge('B', 'A')
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        g.delete_edge('B', 'A')
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        self.assertTrue(g.size(), 4)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)
        
    def test_delete_edge_weighted_undirected(self):
        g = AdjacencyMatrixWeightedGraph(directed=False)
        print("Vertices: ", g.vertices())
        g.add_edge('A', 'B', 1)
        print("Vertices: ", g.vertices())
        g.add_edge('B', 'C', 2)
        print("Vertices: ", g.vertices())
        g.add_edge('C', 'D', 3)
        g.add_edge('D', 'E', 4)
        g.add_edge('E', 'A', 5)
        
        self.assertTrue(g.size(), 5)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))

        self.assertEqual(g['A']['B'], 1)
        self.assertEqual(g['B']['C'], 2)

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

        g.add_edge('B', 'A', 1)
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('A', 'B'))

        self.assertTrue(g.size(), 4)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)  
        
    def test_delete_edge_weighted_directed(self):
        g = AdjacencyMatrixWeightedGraph(directed=True)
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('C', 'D', 3)
        g.add_edge('D', 'E', 4)
        g.add_edge('E', 'A', 5)

        self.assertTrue(g.size(), 5)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        self.assertEqual(g['A']['B'], 1)
        self.assertEqual(g['B']['C'], 2)

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'C'))

        self.assertFalse(g.has_edge('A', 'B'))

        with self.assertRaises(KeyError):
            g.delete_edge('B', 'A')
        self.assertFalse(g.has_edge('A', 'B'))

        g.add_edge('B', 'A', 1)
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        g.delete_edge('B', 'A')
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        self.assertTrue(g.size(), 4)
        self.assertTrue(g.order(), 5)
        self.assertTrue(len(g), 5)