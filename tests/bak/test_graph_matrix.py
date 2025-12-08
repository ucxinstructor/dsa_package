import unittest

from dsa.graph import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph

class TestAdjacencyMatrixGraph(unittest.TestCase):
    def test_create_undirected(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixGraph(directed=False, vertices=vertices)
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')
        self.assertEqual(g["A"], ["B", "C"])

        self.assertTrue(g.has_edge("A", "B"))
        self.assertFalse(g.has_edge("B", "C"))

        g.add_edge("B", 'C')
        self.assertTrue(g.has_edge("B", "C"))
        g.add_edge("B", 'D')
        self.assertEqual(g["B"], ["A", "C", "D"])

        g.add_edge("C", 'D')
        g.add_edge("D", 'E')
        g.add_edge("E", 'F')
        g.add_edge("F", 'G')
        self.assertTrue(g.has_edge("C", "D"))
        self.assertTrue(g.has_edge("D", "C"))

        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("G"), ["G", "F", "E", "D", "B", "A", "C"])
        # self.assertEqual(g.bfs_traverse("G"), ["G", "F", "E", "D", "B", "C", "A"])

        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        g = AdjacencyMatrixGraph(vertices=vertices)
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')

        g.add_edge("B", 'D')
        g.add_edge("B", 'E')

        g.add_edge("C", 'F')
        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F"])

        self.assertEqual(g.vertices(), vertices)
        self.assertEqual(g.edges(), [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'F'), ('D', 'B'), ('E', 'B'), ('F', 'C')])

    def test_create_directed(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixGraph(directed=True, vertices=vertices)
        self.assertEqual(g["A"], [])
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')
        self.assertTrue(g.has_edge("A", "C"))
        self.assertFalse(g.has_edge("C", "A"))

        self.assertEqual(g["A"], ["B", "C"])
        self.assertTrue(g.has_edge("A", "B"))
        self.assertFalse(g.has_edge("B", "C"))

        g.add_edge("B", 'C')
        self.assertTrue(g.has_edge("B", "C"))
        g.add_edge("B", 'D')
        self.assertEqual(g["B"], ["C", "D"])

        g.add_edge("C", 'D')
        g.add_edge("D", 'E')
        g.add_edge("E", 'F')
        g.add_edge("F", 'G')

        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("G"), ["G"])
        # self.assertEqual(g.bfs_traverse("G"), ["G"])

        self.assertEqual(g.vertices(), vertices)
        self.assertEqual(g.edges(), [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])

    def test_delete_directed(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixGraph(directed=True, vertices=vertices)
        g.add_edge('A', 'B')
        g.add_edge('B', 'A')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], ['B'])
        self.assertEqual(g['B'], ['A', 'C'])

        g.delete_edge('A', 'B', directed=True)
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        g.add_edge('A', 'B', directed=True)
        g.delete_edge('B', 'A', directed=True)
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'C'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('A', 'B'))

    def test_delete_undirected(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixGraph(directed=False, vertices=vertices)
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'A')

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

    def test_create_undirected_weighted(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        g = AdjacencyMatrixWeightedGraph(directed=False, vertices=vertices)
        g.add_edge("A", 'B', 1)
        g.add_edge("A", 'C', 2)
        self.assertTrue(g.has_edge("A", "C"))
        self.assertFalse(g.has_edge("B", "E"))
        self.assertEqual(g["A"]["B"], 1)

        g.add_edge("B", 'D', 3)
        g.add_edge("B", 'E', 4)
        self.assertTrue(g.has_edge("B", "E"))
        self.assertEqual(g["B"]["D"], 3)

        g.add_edge("C", 'F', 5)
        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F"])
        self.assertEqual(g.vertices(), vertices)
        self.assertEqual(g.edges(), [('A', 'B', 1), ('A', 'C', 2), ('B', 'A', 1), ('B', 'D', 3), ('B', 'E', 4), ('C', 'A', 2), ('C', 'F', 5), ('D', 'B', 3), ('E', 'B', 4), ('F', 'C', 5)])

        self.assertEqual(g['A']['B'], 1)
        self.assertEqual(g['B']['A'], 1)
        self.assertEqual(g['C']['F'], 5)
        self.assertEqual(g['E']['B'], 4)
        with self.assertRaises(KeyError):
            g['E']['A']

    def test_delete_undirected_weighted(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixWeightedGraph(directed=False, vertices=vertices)
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('C', 'D', 3)
        g.add_edge('D', 'E', 4)
        g.add_edge('E', 'A', 5)

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], {'B': 1, 'E': 5})
        self.assertEqual(g['B'], {'A': 1, 'C': 2})

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

        g.add_edge('B', 'A', 3)
        self.assertEqual(g['A'], {'B': 3, 'E': 5})
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('A', 'B'))

    def test_create_directed_weighted(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixWeightedGraph(directed=True, vertices=vertices)
        g.add_edge("A", 'B', 1)
        g.add_edge("A", 'C', 2)
        self.assertTrue(g.has_edge("A", "C"))
        self.assertFalse(g.has_edge("B", "E"))
        self.assertDictEqual(g["A"], {"B": 1, "C": 2})
        self.assertEqual(g["A"]["B"], 1)
        g.add_edge("B", 'C', 3)
        g.add_edge("B", 'D', 4)
        self.assertEqual(g["B"]["D"], 4)
        self.assertFalse(g.has_edge("B", "E"))

        g.add_edge("C", 'D', 5)
        g.add_edge("D", 'E', 6)
        g.add_edge("E", 'F', 7)
        g.add_edge("F", 'G', 8)

        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.dfs_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        # self.assertEqual(g.bfs_traverse("B"), ["B", "C", "D", "E", "F", "G"])
#        self.assertEqual(g.dfs_traverse("G"), ["G"])
#        self.assertEqual(g.bfs_traverse("G"), ["G"])

        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        g = AdjacencyMatrixWeightedGraph(directed=True, vertices=vertices)
        g.add_edge("A", 'B', 1)

        g.add_edge("B", 'D', 3)
        g.add_edge("B", 'E', 4)

        g.add_edge("C", 'F', 5)
        # self.assertEqual(g.dfs_traverse("A"), ["A", "B", "D", "E"])
        # self.assertEqual(g.bfs_traverse("A"), ["A", "B", "D", "E"])
        self.assertEqual(g.vertices(), vertices)
        self.assertEqual(g.edges(), [('A', 'B', 1),
                                     ('B', 'D', 3), 
                                     ('B', 'E', 4), 
                                     ('C', 'F', 5)])

        self.assertEqual(g['A']['B'], 1)
        with self.assertRaises(KeyError):
            g['B']['A']
        self.assertEqual(g['C']['F'], 5)
        self.assertEqual(g['B']['D'], 3)
        with self.assertRaises(KeyError):
            g['E']['B']

    def test_delete_directed_weighted(self):
        vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixWeightedGraph(directed=True, vertices=vertices)
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('C', 'D', 3)
        g.add_edge('D', 'E', 4)
        g.add_edge('E', 'A', 5)
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        self.assertEqual(g['A'], {'B': 1})
        self.assertEqual(g['B'], {'C': 2})

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

        g.add_edge('B', 'A', 3)
        self.assertEqual(g['A'], {})
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertTrue(g.has_edge('B', 'C'))

        with self.assertRaises(KeyError):
            g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        
    def test_contains(self):
        vertices = ['A', 'B', 'C']
        g = AdjacencyMatrixGraph(vertices=vertices)
        self.assertIn('A', g)
        self.assertIn('B', g)
        self.assertIn('C', g)
        self.assertNotIn('D', g)

        gw = AdjacencyMatrixWeightedGraph(vertices=vertices)
        self.assertIn('A', gw)
        self.assertIn('B', gw)
        self.assertIn('C', gw)
        self.assertNotIn('D', gw)
        
    def test_to_dict(self):
        vertices = ['A', 'B', 'C']
        g = AdjacencyMatrixGraph(vertices=vertices)
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'C')

        expected_dict = {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B']
        }
        self.assertEqual(g.to_dict(), expected_dict)

        gw = AdjacencyMatrixWeightedGraph(vertices=vertices)
        gw.add_edge('A', 'B', 2)
        gw.add_edge('A', 'C', 3)
        gw.add_edge('B', 'C', 4)

        expected_weighted_dict = {
            'A': {'B': 2, 'C': 3},
            'B': {'A': 2, 'C': 4},
            'C': {'A': 3, 'B': 4}
        }
        self.assertEqual(gw.to_dict(), expected_weighted_dict)
        
