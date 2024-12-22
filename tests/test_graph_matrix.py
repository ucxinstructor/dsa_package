import unittest

from dsa.graph import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph

class TestAdjacencyMatrixGraph(unittest.TestCase):
    def test_create_undirected(self):
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixGraph(labels)
        self.assertEqual(g["A"], [])
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')
        self.assertEqual(g["A"], ["A", "B", "C"])

        self.assertTrue(g.is_edge("A", "B"))
        self.assertFalse(g.is_edge("B", "C"))

        g.add_adjacent_vertex("B", 'C')
        self.assertTrue(g.is_edge("B", "C"))
        g.add_adjacent_vertex("B", 'D')
        self.assertEqual(g["B"], ["A", "B", "C", "D"])

        g.add_edge("C", 'D')
        g.add_edge("D", 'E')
        g.add_edge("E", 'F')
        g.add_edge("F", 'G')
        self.assertTrue(g.is_edge("C", "D"))
        self.assertTrue(g.is_edge("D", "C"))

        self.assertEqual(g.df_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("G"), ["G", "F", "E", "D", "B", "A", "C"])
        self.assertEqual(g.bf_traverse("G"), ["G", "F", "E", "D", "B", "C", "A"])

        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        g = AdjacencyMatrixGraph(labels)
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')

        g.add_edge("B", 'D')
        g.add_edge("B", 'E')

        g.add_edge("C", 'F')
        self.assertEqual(g.df_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F"])

        self.assertEqual(g.vertices(), labels)
        self.assertEqual(g.edges(), [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'F'), ('D', 'B'), ('E', 'B'), ('F', 'C')])

    def test_create_directed(self):
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixGraph(labels)
        self.assertEqual(g["A"], [])
        g.add_directed_edge("A", 'B')
        g.add_directed_edge("A", 'C')
        self.assertTrue(g.is_edge("A", "C"))
        self.assertFalse(g.is_edge("C", "A"))

        self.assertEqual(g["A"], ["A", "B", "C"])
        self.assertTrue(g.is_edge("A", "B"))
        self.assertFalse(g.is_edge("B", "C"))

        g.add_adjacent_directed_vertex("B", 'C')
        self.assertTrue(g.is_edge("B", "C"))
        g.add_adjacent_directed_vertex("B", 'D')
        self.assertEqual(g["B"], ["B", "C", "D"])

        g.add_directed_edge("C", 'D')
        g.add_directed_edge("D", 'E')
        g.add_directed_edge("E", 'F')
        g.add_directed_edge("F", 'G')

        self.assertEqual(g.df_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("G"), ["G"])
        self.assertEqual(g.bf_traverse("G"), ["G"])

        self.assertEqual(g.vertices(), labels)
        self.assertEqual(g.edges(), [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])

    
    def test_create_undirected_weighted(self):
        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        g = AdjacencyMatrixWeightedGraph(labels)
        g.add_edge("A", 'B', 1)
        g.add_edge("A", 'C', 2)
        self.assertTrue(g.is_edge("A", "C"))
        self.assertFalse(g.is_edge("B", "E"))
        self.assertEqual(g["A"]["B"], 1)

        g.add_edge("B", 'D', 3)
        g.add_edge("B", 'E', 4)
        self.assertTrue(g.is_edge("B", "E"))
        self.assertEqual(g["B"]["D"], 3)

        g.add_edge("C", 'F', 5)
        self.assertEqual(g.df_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F"])
        self.assertEqual(g.vertices(), labels)
        self.assertEqual(g.edges(), [('A', 'B', 1), ('A', 'C', 2), ('B', 'A', 1), ('B', 'D', 3), ('B', 'E', 4), ('C', 'A', 2), ('C', 'F', 5), ('D', 'B', 3), ('E', 'B', 4), ('F', 'C', 5)])

        self.assertEqual(g['A']['B'], 1)
        self.assertEqual(g['B']['A'], 1)
        self.assertEqual(g['C']['F'], 5)
        self.assertEqual(g['E']['B'], 4)
        with self.assertRaises(KeyError):
            g['E']['A']


    def test_create_directed_weighted(self):
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        g = AdjacencyMatrixWeightedGraph(labels)
        g.add_directed_edge("A", 'B', 1)
        g.add_directed_edge("A", 'C', 2)
        self.assertTrue(g.is_edge("A", "C"))
        self.assertFalse(g.is_edge("B", "E"))
        print(g["A"])
        self.assertEqual(g["A"]["B"], 1)
        g.add_adjacent_directed_vertex("B", 'C', 3)
        g.add_adjacent_directed_vertex("B", 'D', 4)
        self.assertEqual(g["B"]["D"], 4)
        self.assertFalse(g.is_edge("B", "E"))

        g.add_directed_edge("C", 'D', 5)
        g.add_directed_edge("D", 'E', 6)
        g.add_directed_edge("E", 'F', 7)
        g.add_directed_edge("F", 'G', 8)

        self.assertEqual(g.df_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("B"), ["B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("G"), ["G"])
        self.assertEqual(g.bf_traverse("G"), ["G"])

        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        g = AdjacencyMatrixWeightedGraph(labels)
        g.add_directed_edge("A", 'B', 1)
        g.add_directed_edge("A", 'C', 2)

        g.add_directed_edge("B", 'D', 3)
        g.add_directed_edge("B", 'E', 4)

        g.add_directed_edge("C", 'F', 5)
        self.assertEqual(g.df_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F"])
        self.assertEqual(g.vertices(), labels)
        self.assertEqual(g.edges(), [('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 3), ('B', 'E', 4), ('C', 'F', 5)])

        self.assertEqual(g['A']['B'], 1)
        with self.assertRaises(KeyError):
            g['B']['A']
        self.assertEqual(g['C']['F'], 5)
        self.assertEqual(g['B']['D'], 3)
        with self.assertRaises(KeyError):
            g['E']['B']
