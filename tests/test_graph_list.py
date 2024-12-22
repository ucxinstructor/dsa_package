import unittest
from dsa.graph import AdjacencyListGraph, AdjacencyListWeightedGraph

class TestAdjacencyListGraph(unittest.TestCase):
    def test_create_undirected(self):
        g = AdjacencyListGraph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        self.assertEqual(g['A'], ['B', 'C'])
        self.assertTrue(g.is_edge('A', 'B'))
        self.assertTrue(g.is_edge('B', 'A'))
        g.add_adjacent_vertex('B', 'C')
        g.add_adjacent_vertex('B', 'D')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'F')
        g.add_edge('F', 'G')

        self.assertEqual(g['A'], ['B', 'C'])
        self.assertEqual(g['E'], ['D', 'F'])

        self.assertEqual(g.df_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        self.assertEqual(g.bf_traverse("B"), ["B", "A", "C", "D", "E", "F", "G"])
        self.assertEqual(g.df_traverse("G"), ["G", "F", "E", "D", "B", "A", "C"])
        self.assertEqual(g.bf_traverse("G"), ["G", "F", "E", "D", "B", "C", "A"])

        g = AdjacencyListGraph()
        g.add_edge("A", 'B')
        g.add_edge("A", 'C')

        g.add_edge("B", 'D')
        g.add_edge("B", 'E')

        g.add_edge("C", 'F')
        self.assertEqual(g.df_traverse("A"), ["A", "B", "D", "E", "C", "F"])
        self.assertEqual(g.bf_traverse("A"), ["A", "B", "C", "D", "E", "F"])
        self.assertEqual(g.edges(), [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'F'), ('D', 'B'), ('E', 'B'), ('F', 'C')])

        self.assertEqual(g.dfs('A', 'B'), 'B')
        self.assertEqual(g.dfs('A', 'E'), 'E')
        self.assertEqual(g.dfs('C', 'F'), 'F')

        self.assertEqual(g.bfs('A', 'B'), 'B')
        self.assertEqual(g.bfs('A', 'E'), 'E')
        self.assertEqual(g.bfs('C', 'F'), 'F')

    def test_create_directed(self):
        g = AdjacencyListGraph()
        g.add_directed_edge('A', 'B')
        g.add_directed_edge('B', 'C')
        g.add_directed_edge('C', 'D')
        g.add_directed_edge('D', 'E')
        g.add_directed_edge('E', 'A')

        self.assertTrue(g.is_edge('A', 'B'))
        self.assertFalse(g.is_edge('B', 'A'))

        self.assertEqual(g['A'], ['B'])
        self.assertEqual(g['E'], ['A'])
        self.assertEqual(g.edges(), [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')])
        self.assertTrue(g.is_edge('A', 'B'))
        self.assertFalse(g.is_edge('B', 'A'))

        self.assertEqual(g.dfs('A', 'B'), 'B')
        self.assertEqual(g.dfs('A', 'E'), 'E')
        self.assertEqual(g.dfs('C', 'E'), 'E')

        self.assertEqual(g.bfs('A', 'B'), 'B')
        self.assertEqual(g.bfs('A', 'E'), 'E')
        self.assertEqual(g.bfs('C', 'E'), 'E')


    def test_create_undirected_weighted(self):
        g = AdjacencyListWeightedGraph()
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('C', 'D', 3)
        g.add_edge('D', 'E', 4)
        g.add_edge('E', 'A', 5)

        self.assertTrue(g.is_edge('A', 'B'))
        self.assertTrue(g.is_edge('B', 'A'))


        self.assertEqual(g['A'], {'B': 1, 'E': 5})
        self.assertEqual(g.edges(), [('A', 'B', 1), ('A', 'E', 5), ('B', 'A', 1), ('B', 'C', 2), ('C', 'B', 2), ('C', 'D', 3), ('D', 'C', 3), ('D', 'E', 4), ('E', 'D', 4), ('E', 'A', 5)])

        self.assertEqual(g['A']['B'], 1)
        self.assertEqual(g['B']['A'], 1)
        self.assertEqual(g['C']['D'], 3)
        self.assertEqual(g['E']['A'], 5)
        with self.assertRaises(KeyError):
            g['A']['C']
        self.assertEqual(g.dfs('A', 'B'), 'B')
        self.assertEqual(g.dfs('A', 'E'), 'E')
        self.assertEqual(g.dfs('C', 'E'), 'E')

        self.assertEqual(g.bfs('A', 'B'), 'B')
        self.assertEqual(g.bfs('A', 'E'), 'E')
        self.assertEqual(g.bfs('C', 'E'), 'E')


    def test_create_directed_weighted(self):
        g = AdjacencyListWeightedGraph()
        g.add_directed_edge('A', 'B', 1)
        g.add_directed_edge('B', 'C', 2)
        g.add_directed_edge('C', 'D', 3)
        g.add_directed_edge('D', 'E', 4)
        g.add_directed_edge('E', 'A', 5)

        self.assertTrue(g.is_edge('A', 'B'))
        self.assertFalse(g.is_edge('B', 'A'))

        self.assertEqual(g['A'], {'B': 1})
        self.assertEqual(g.edges(), [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'E', 4), ('E', 'A', 5)])

        self.assertEqual(g['A']['B'], 1)
        with self.assertRaises(KeyError):
            g['B']['A']
        self.assertEqual(g['C']['D'], 3)
        self.assertEqual(g['E']['A'], 5)
        with self.assertRaises(KeyError):
            g['A']['C']

        self.assertEqual(g.dfs('A', 'B'), 'B')
        self.assertEqual(g.dfs('A', 'E'), 'E')
        self.assertEqual(g.dfs('C', 'E'), 'E')

        self.assertEqual(g.bfs('A', 'B'), 'B')
        self.assertEqual(g.bfs('A', 'E'), 'E')
        self.assertEqual(g.bfs('C', 'E'), 'E')

