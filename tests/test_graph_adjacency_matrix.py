import unittest
from dsa.graph import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph

# Assume that the graph implementation properly handles vertex keys (mapping them to indices)

class TestAdjacencyMatrixGraph(unittest.TestCase):
    
    # 1. SETUP: Define a consistent set of vertices for all tests
    def setUp(self):
        # Full set of vertices for structure tests
        self.VERTICES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        
        # Unweighted Graph structure (Cyclic, connected)
        self.g_undirected = AdjacencyMatrixGraph(directed=False)
        self.g_undirected.add_edge('A', 'B')
        self.g_undirected.add_edge('A', 'C')
        self.g_undirected.add_edge('B', 'C')
        self.g_undirected.add_edge('B', 'D')
        self.g_undirected.add_edge('C', 'D')
        self.g_undirected.add_edge('D', 'E')
        self.g_undirected.add_edge('E', 'F')
        self.g_undirected.add_edge('F', 'G')
        
        # Directed Graph structure (Cycle A-B-C-D-E-A)
        self.g_directed = AdjacencyMatrixGraph(directed=True)
        self.g_directed.add_edge('A', 'B')
        self.g_directed.add_edge('B', 'C')
        self.g_directed.add_edge('C', 'D')
        self.g_directed.add_edge('D', 'E')
        self.g_directed.add_edge('E', 'A')

        # Weighted Undirected Graph structure
        self.g_wu = AdjacencyMatrixWeightedGraph(directed=False)
        self.g_wu.add_edge('A', 'B', 1)
        self.g_wu.add_edge('B', 'C', 2)
        self.g_wu.add_edge('C', 'D', 3)
        self.g_wu.add_edge('D', 'E', 4)
        self.g_wu.add_edge('E', 'A', 5)

        # Weighted Directed Graph structure
        self.g_wd = AdjacencyMatrixWeightedGraph(directed=True)
        self.g_wd.add_edge('A', 'B', 1)
        self.g_wd.add_edge('B', 'C', 2)
        self.g_wd.add_edge('C', 'D', 3)
        self.g_wd.add_edge('D', 'E', 4)
        self.g_wd.add_edge('E', 'A', 5)


    ## 2. CORE PROPERTY TESTS (Undirected Unweighted)

    def test_undirected_properties(self):
        g = self.g_undirected
        # Initial Vertex/Edge Counts
        self.assertEqual(g.order(), 7)  # A-G = 7 vertices
        self.assertEqual(len(g), 7)
        self.assertEqual(g.size(), 8)   # A-B, A-C, B-C, B-D, C-D, D-E, E-F, F-G = 8 unique edges
        self.assertIn('A', g)
        self.assertNotIn('Z', g)
        self.assertSetEqual(set(g.vertices()), set(self.VERTICES))

        # Adjacency and Edge Existence
        self.assertEqual(g['A'], ['B', 'C'])
        self.assertEqual(g['D'], ['B', 'C', 'E'])
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertTrue(g.has_edge('B', 'A'))
        self.assertFalse(g.has_edge('A', 'D'))
        
        # Edge List
        # Note: Must contain both directions for undirected graph implementation
        expected_edges_partial = {('A', 'B'), ('B', 'A'), ('C', 'D'), ('D', 'C'), ('F', 'G'), ('G', 'F')}
        self.assertTrue(expected_edges_partial.issubset(set(g.edges())))


    ## 3. CORE PROPERTY TESTS (Directed Unweighted)

    def test_directed_properties(self):
        g = self.g_directed
        # Counts and Size
        self.assertEqual(g.order(), 5) # A-E = 5 vertices
        self.assertEqual(g.size(), 5)  # 5 directed edges

        # Adjacency and Edge Existence
        self.assertEqual(g['A'], ['B'])
        self.assertEqual(g['E'], ['A'])
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A')) # Crucial directional check
        self.assertFalse(g.has_edge('E', 'B'))

        # Edge List
        self.assertSetEqual(set(g.edges()), {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')})

    def test_from_dict(self):
        # Unweighted
        data = {
            'A': ['B', 'C'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B', 'D'],
            'D': ['B', 'C', 'E'],
            'E': ['D', 'F'],
            'F': ['E', 'G'],
            'G': ['F']
        }
        g = AdjacencyMatrixGraph.from_dict(data, directed=False)
        self.assertEqual(g.to_dict(), data)
        self.assertEqual(g.order(), 7)
        self.assertEqual(g.size(), 8)

        # Weighted
        data_weighted = {
            'A': {'B': 1, 'C': 2},
            'B': {'A': 1, 'C': 3},
            'C': {'A': 2, 'B': 3}
        }
        g_weighted = AdjacencyMatrixWeightedGraph.from_dict(data_weighted, directed=False)
        self.assertEqual(g_weighted.to_dict(), data_weighted)
        self.assertEqual(g_weighted.order(), 3)
        self.assertEqual(g_weighted.size(), 3)

    ## 4. MUTATION TESTS

    def test_vertex_mutations(self):
        g = AdjacencyMatrixGraph(directed=False)
        g.add_vertex('V1')
        self.assertEqual(g.order(), 1)
        self.assertIn('V1', g)

        # Test adding a duplicate vertex (should raise error)
        with self.assertRaises(ValueError):
            g.add_vertex('V1')
        
        # Test deletion
        self.g_directed.delete_vertex('A')
        self.assertEqual(self.g_directed.order(), 4) # B, C, D, E remain
        self.assertNotIn('A', self.g_directed)

        with self.assertRaises(KeyError):
            self.g_directed.has_edge('E', 'A')
        with self.assertRaises(KeyError):
            self.g_directed.has_edge('A', 'B')

    def test_delete_edge_undirected(self):
        g = self.g_undirected
        self.assertTrue(g.has_edge('A', 'B'))
        
        g.delete_edge('A', 'B')
        
        # Deleting (A, B) must delete (B, A) in adjacency matrix
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertEqual(g.size(), 7) # Size decreased by 1

        # Deleting a non-existent edge should raise KeyError (or similar)
        with self.assertRaises(KeyError):
            g.delete_edge('A', 'B')
            
    def test_delete_edge_directed(self):
        g = self.g_directed
        self.assertTrue(g.has_vertex('A'))
        self.assertTrue(g.has_vertex('B'))
        self.assertFalse(g.has_vertex('X'))

        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))

        g.delete_edge('A', 'B')

        # Deleting (A, B) must NOT affect (B, A)
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A')) # Still false
        self.assertEqual(g.size(), 4) # Size decreased by 1

        # Attempt to delete non-existent edge (B, A)
        with self.assertRaises(KeyError):
             g.delete_edge('B', 'A')
        self.assertTrue(g.has_vertex('A'))
        self.assertTrue(g.has_vertex('B'))
        self.assertFalse(g.has_vertex('X'))

    ## 5. WEIGHTED GRAPH TESTS

    def test_weighted_undirected_properties(self):
        g = self.g_wu
        self.assertTrue(g.has_vertex('A'))
        self.assertTrue(g.has_vertex('B'))
        self.assertFalse(g.has_vertex('X'))
        self.assertEqual(g.order(), 5)
        self.assertEqual(g.size(), 5)

        # Check weight access (assuming __getitem__ handles weights)
        self.assertDictEqual(g['A'], {'B': 1, 'E': 5})
        self.assertEqual(g['B']['A'], 1)
        
        # Check edge list format
        expected_edges_partial = {('A', 'B', 1), ('B', 'A', 1), ('D', 'E', 4), ('E', 'D', 4)}
        self.assertTrue(expected_edges_partial.issubset(set(g.edges())))
        
        # Test deletion
        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        self.assertEqual(g.size(), 4)
        self.assertTrue(g.has_vertex('A'))
        self.assertTrue(g.has_vertex('B'))
        self.assertFalse(g.has_vertex('X'))

    def test_weighted_directed_properties(self):
        g = self.g_wd
        self.assertTrue(g.has_vertex('A'))
        self.assertTrue(g.has_vertex('B'))
        self.assertFalse(g.has_vertex('X'))
        self.assertEqual(g.order(), 5)
        self.assertEqual(g.size(), 5)

        # Check weight access
        self.assertDictEqual(g['A'], {'B': 1})
        self.assertDictEqual(g['E'], {'A': 5})
        self.assertEqual(g['A']['B'], 1)
        
        self.assertTrue(g.has_edge('A', 'B'))
        self.assertFalse(g.has_edge('B', 'A'))
        
        # Check edge list format
        self.assertSetEqual(set(g.edges()), {('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 3), ('D', 'E', 4), ('E', 'A', 5)})

        # Test deletion
        g.delete_edge('A', 'B')
        self.assertFalse(g.has_edge('A', 'B'))
        self.assertEqual(g.size(), 4)
        self.assertTrue(g.has_vertex('A'))
        self.assertTrue(g.has_vertex('B'))
        self.assertFalse(g.has_vertex('X'))
        
    def test_weighted_edge_deletion_errors(self):
        g = self.g_wu
        self.assertTrue(g.has_edge('A', 'B'))
        
        g.delete_edge('A', 'B')
        
        # Deleting a non-existent edge should raise KeyError (or similar)
        with self.assertRaises(KeyError):
            g.delete_edge('A', 'B')

