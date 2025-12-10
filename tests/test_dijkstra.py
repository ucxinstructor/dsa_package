import unittest
from dsa.dijkstra import shortest_path, find_path
from dsa.graph import Graph

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.gl = Graph.create_adjacency_list(directed=True, weighted=True)
        self.gl.add_edge('A', 'B', 1)
        self.gl.add_edge('A', 'C', 4)
        self.gl.add_edge('B', 'C', 2)
        self.gl.add_edge('B', 'D', 5)
        self.gl.add_edge('C', 'D', 1)

        self.gm = Graph.create_adjacency_matrix(directed=True, weighted=True)
        self.gm.add_edge('A', 'B', 1)
        self.gm.add_edge('A', 'C', 4)
        self.gm.add_edge('B', 'C', 2)
        self.gm.add_edge('B', 'D', 5)
        self.gm.add_edge('C', 'D', 1)
        
    def test_shortest_path(self):
        weight_table, previous = shortest_path(self.gl, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)
        self.assertEqual(previous['D'], 'C')
        self.assertEqual(previous['C'], 'B')
        self.assertEqual(previous['B'], 'A')

        weight_table, previous = shortest_path(self.gm, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)
        self.assertEqual(previous['D'], 'C')
        self.assertEqual(previous['C'], 'B')
        self.assertEqual(previous['B'], 'A')

    def test_shortest_path_same_start_end(self):
        weight_table, previous = shortest_path(self.gl, 'A', 'A')
        self.assertEqual(weight_table['A'], 0)
        self.assertEqual(previous['A'], 'A')

        weight_table, previous = shortest_path(self.gm, 'A', 'A')
        self.assertEqual(weight_table['A'], 0)
        self.assertEqual(previous['A'], 'A')

    def test_shortest_path_no_path(self):
        self.gl.add_edge('E', 'E', 0)
        weight_table, previous = shortest_path(self.gl, 'A', 'E')
        self.assertNotIn('E', weight_table)
        self.assertNotIn('E', previous)

        self.gm.add_edge('E', 'E', 0)
        weight_table, previous = shortest_path(self.gm, 'A', 'E')
        self.assertNotIn('E', weight_table)
        self.assertNotIn('E', previous)

    def test_graph_with_cycle(self):
        # Add cycle C → A with big weight
        self.gl.add_edge('C', 'A', 10)
        weight_table, previous = shortest_path(self.gl, 'A', 'D')
        # Should still produce the same shortest path as before
        self.assertEqual(weight_table['D'], 4)

        # Add cycle C → A with big weight
        self.gl.add_edge('C', 'A', 10)
        weight_table, previous = shortest_path(self.gm, 'A', 'D')
        # Should still produce the same shortest path as before
        self.assertEqual(weight_table['D'], 4)

    def test_multiple_equal_paths(self):
        # Add another equally-weighted path A → X → D
        self.gl.add_edge('A', 'X', 2)
        self.gl.add_edge('X', 'D', 2)
        weight_table, previous = shortest_path(self.gl, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)
        # Path may be A-B-C-D or A-X-D; both valid
        self.assertIn(previous['D'], ('C', 'X'))


        # Add another equally-weighted path A → X → D
        self.gm.add_edge('A', 'X', 2)
        self.gm.add_edge('X', 'D', 2)
        weight_table, previous = shortest_path(self.gm, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)
        # Path may be A-B-C-D or A-X-D; both valid
        self.assertIn(previous['D'], ('C', 'X'))


    def test_disconnected_graph(self):
        # Add entirely separate component
        self.gl.add_edge('X', 'Y', 1)
        weight_table, previous = shortest_path(self.gl, 'A', 'Y')
        self.assertNotIn('Y', weight_table)

        self.gm.add_edge('X', 'Y', 1)
        weight_table, previous = shortest_path(self.gm, 'A', 'Y')
        self.assertNotIn('Y', weight_table)


    def test_heavier_direct_edge(self):
        # Add direct but worse path
        self.gl.add_edge('A', 'D', 100)
        weight_table, previous = shortest_path(self.gl, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)

        self.gm.add_edge('A', 'D', 100)
        weight_table, previous = shortest_path(self.gm, 'A', 'D')
        self.assertEqual(weight_table['D'], 4)

    def test_zero_weight_edges(self):
        # Add zero-weight shortcuts
        self.gl.add_edge('A', 'Z', 0)
        self.gl.add_edge('Z', 'D', 0)
        self.assertTrue(self.gl.has_edge('A','Z'))
        self.assertTrue(self.gl.has_edge('Z','D'))
        weight_table, previous = shortest_path(self.gl, 'A', 'D')
        self.assertEqual(weight_table['D'], 0)
        self.assertEqual(previous['D'], 'Z')
        self.assertEqual(previous['Z'], 'A')

        self.assertFalse(self.gm.has_vertex('Z'))
        self.assertTrue(self.gm.has_vertex('D'))
        self.gm.add_edge('A', 'Z', 0)
        self.gm.add_edge('Z', 'D', 0)
        self.assertEqual(self.gm.get_weight('A', 'Z'), 0)
        self.assertTrue(self.gm.has_vertex('Z'))
        self.assertTrue(self.gm.has_vertex('D'))
        self.assertTrue(self.gm.has_edge('A','Z'))
        self.assertTrue(self.gm.has_edge('Z','D'))
        weight_table_gm, previous_gm = shortest_path(self.gm, 'A', 'D')

        self.assertEqual(weight_table, weight_table_gm)
        self.assertEqual(previous, previous_gm)
        self.assertEqual(weight_table_gm['D'], 0)
        self.assertEqual(previous_gm['D'], 'Z')
        self.assertEqual(previous_gm['Z'], 'A')

    def test_large_linear_chain(self):
        # Long path A → B → C → ... → J
        g = Graph.create_adjacency_list(directed=True, weighted=True)
        letters = "ABCDEFGHIJ"
        for i in range(len(letters)-1):
            g.add_edge(letters[i], letters[i+1], 1)
        weight_table, previous = shortest_path(g, 'A', 'J')
        self.assertEqual(weight_table['J'], 9)
        self.assertEqual(previous['J'], 'I')

    def test_end_not_in_graph(self):
        with self.assertRaises(KeyError):
            weight_table, previous = shortest_path(self.gl, 'A', 'ZZZ')
    
        with self.assertRaises(KeyError):
            weight_table, previous = shortest_path(self.gm, 'A', 'ZZZ')

class TestFindPath(unittest.TestCase):
    def setUp(self):
        self.gl = Graph.create_adjacency_list(directed=True, weighted=True)
        self.gl.add_edge('A', 'B', 1)
        self.gl.add_edge('A', 'C', 4)
        self.gl.add_edge('B', 'C', 2)
        self.gl.add_edge('B', 'D', 5)
        self.gl.add_edge('C', 'D', 1)

        self.gm = Graph.create_adjacency_matrix(directed=True, weighted=True)
        self.gm.add_edge('A', 'B', 1)
        self.gm.add_edge('A', 'C', 4)
        self.gm.add_edge('B', 'C', 2)
        self.gm.add_edge('B', 'D', 5)
        self.gm.add_edge('C', 'D', 1)


    def test_find_path_basic(self):
        path = find_path(self.gl, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])

        path = find_path(self.gm, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])

    def test_find_path_same_start_end(self):
        path = find_path(self.gl, 'A', 'A')
        self.assertEqual(path, ['A'])

        path = find_path(self.gm, 'A', 'A')
        self.assertEqual(path, ['A'])

    def test_find_path_no_path(self):
        # Add isolated E
        self.gl.add_edge('E', 'E', 0)
        with self.assertRaises(KeyError):
            # predecessor['E'] will not exist → KeyError expected
            find_path(self.gl, 'A', 'E')

        self.gm.add_edge('E', 'E', 0)
        with self.assertRaises(KeyError):
            # predecessor['E'] will not exist → KeyError expected
            find_path(self.gm, 'A', 'E')

    def test_find_path_intermediate(self):
        path = find_path(self.gl, 'A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])

        path = find_path(self.gm, 'A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])

    def test_find_path_debug_output(self):
        # Just verify it runs; no exception
        path = find_path(self.gl, 'A', 'D', debug=True)
        self.assertEqual(path, ['A', 'B', 'C', 'D'])

        path = find_path(self.gm, 'A', 'D', debug=True)
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
        
if __name__ == '__main__':
    unittest.main()