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


    ## 4. MUTATION TESTS

    def test_vertex_mutations(self):
        g = AdjacencyMatrixGraph(directed=False)
        g.add_vertex('V1')
        self.assertEqual(g.order(), 1)
        self.assertIn('V1', g)

        # Test adding a duplicate vertex (should raise error)
        with self.assertRaises(ValueError):
            g.add_vertex('V1')
        
        # Test deletion (Implicit test from test_graph_matrix_2.py)
        self.g_directed.delete_vertex('A')
        self.assertEqual(self.g_directed.order(), 4) # B, C, D, E remain
        self.assertNotIn('A', self.g_directed)
        self.assertFalse(self.g_directed.has_edge('E', 'A'))
        self.assertFalse(self.g_directed.has_edge('A', 'B'))

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

    ## 5. WEIGHTED GRAPH TESTS

    def test_weighted_undirected_properties(self):
        g = self.g_wu
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


    def test_weighted_directed_properties(self):
        g = self.g_wd
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

    ## 6. TRAVERSAL TESTS

    def test_traversal_undirected(self):
        g = self.g_undirected
        # DFS starting from 'A'
        self.assertEqual(g.dfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # BFS starting from 'A'
        self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E", "F", "G"])
        # DFS starting from 'G' (reverse path)
        self.assertEqual(g.dfs_traverse("G"), ["G", "F", "E", "D", "B", "A", "C"])
        # BFS starting from 'G'
        self.assertEqual(g.bfs_traverse("G"), ["G", "F", "E", "D", "B", "C", "A"])

    def test_traversal_directed(self):
        g = self.g_directed # Cycle A->B->C->D->E->A
        # DFS should traverse the full cycle
        self.assertEqual(g.dfs_traverse("A"), ["A", "B", "C", "D", "E"])
        # BFS should traverse the full cycle
        self.assertEqual(g.bfs_traverse("A"), ["A", "B", "C", "D", "E"])
        
        # Starting from a vertex with no outgoing edges (if graph was acyclic)
        g_tail = AdjacencyMatrixGraph(directed=True)
        g_tail.add_edge('X', 'Y')
        self.assertEqual(g_tail.dfs_traverse("Y"), ["Y"])
        self.assertEqual(g_tail.bfs_traverse("Y"), ["Y"])