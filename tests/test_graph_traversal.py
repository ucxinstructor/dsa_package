import unittest
from dsa.graph_traversal import dfs, bfs, dfs_path, bfs_path
from dsa.graph import Graph

class TestGraphTraversal(unittest.TestCase):
    def test_dfs(self):
        graph_al = Graph.create_adjacency_list(directed=False)
        graph_am = Graph.create_adjacency_matrix(directed=False)
        graph_ald = Graph.create_adjacency_list(directed=True)
        graph_amd = Graph.create_adjacency_matrix(directed=True)

        for graph in (graph_al, graph_am, graph_ald, graph_amd):
            with self.assertRaises(KeyError):
                result = dfs(graph, 'A')
                self.assertEqual(result, [])
        
            graph.add_vertex('A')
            result = dfs(graph, 'A')
            self.assertEqual(result, ['A'])
            
            graph.add_vertex('B')
            result = dfs(graph, 'A')
            self.assertEqual(result, ['A'])
            
            graph.add_edge('A', 'B')
            result = dfs(graph, 'A')
            self.assertEqual(result, ['A', 'B'])        

    def test_bfs(self):
        graph_al = Graph.create_adjacency_list(directed=False)
        graph_am = Graph.create_adjacency_matrix(directed=False)
        graph_ald = Graph.create_adjacency_list(directed=True)
        graph_amd = Graph.create_adjacency_matrix(directed=True)

        for graph in (graph_al, graph_am, graph_ald, graph_amd):
            with self.assertRaises(KeyError):
                result = bfs(graph, 'A')
                self.assertEqual(result, [])
        
            graph.add_vertex('A')
            result = bfs(graph, 'A')
            self.assertEqual(result, ['A'])
            
            graph.add_vertex('B')
            result = bfs(graph, 'A')
            self.assertEqual(result, ['A'])
            
            graph.add_edge('A', 'B')
            result = bfs(graph, 'A')
            self.assertEqual(result, ['A', 'B'])        

    def test_traversal(self):
        gl = Graph.create_adjacency_list(directed=False)
        gl.add_edge('A', 'B')
        gl.add_edge('A', 'C')
        gl.add_edge('B', 'D')
        gl.add_edge('C', 'E')
        gl.add_edge('D', 'F')
        
        gm = Graph.create_adjacency_matrix(directed=False)
        gm.add_edge('A', 'B')
        gm.add_edge('A', 'C')
        gm.add_edge('B', 'D')
        gm.add_edge('C', 'E')
        gm.add_edge('D', 'F')
        
        gld = Graph.create_adjacency_list(directed=True)
        gld.add_edge('A', 'B')
        gld.add_edge('A', 'C')
        gld.add_edge('B', 'D')
        gld.add_edge('C', 'E')
        gld.add_edge('D', 'F')
        gmd = Graph.create_adjacency_matrix(directed=True)
        gmd.add_edge('A', 'B')
        gmd.add_edge('A', 'C')
        gmd.add_edge('B', 'D')
        gmd.add_edge('C', 'E')
        gmd.add_edge('D', 'F')
        
        for graph in (gl, gm, gld, gmd):
            result = dfs(graph, 'A')
            self.assertEqual(result, ['A', 'B', 'D', 'F', 'C', 'E'])
            result = bfs(graph, 'A')
            self.assertEqual(result, ['A', 'B', 'C', 'D', 'E', 'F'])
            
            path = dfs_path(graph, 'A', 'F')
            self.assertEqual(path, ['A', 'B', 'D', 'F'])
            path = bfs_path(graph, 'A', 'F')
            self.assertEqual(path, ['A', 'B', 'D', 'F'])

            path = dfs_path(graph, 'A', 'A')
            self.assertEqual(path, ['A'])
            path = bfs_path(graph, 'A', 'A')
            self.assertEqual(path, ['A'])
            
            path = dfs_path(graph, 'F', 'F')
            self.assertEqual(path, ['F'])
            path = bfs_path(graph, 'F', 'F')
            self.assertEqual(path, ['F'])
            
            path = dfs_path(graph, 'A', 'X')
            self.assertIsNone(path)
            path = bfs_path(graph, 'A', 'X')
            self.assertIsNone(path)

        for graph in (gl, gm):
            result = dfs(graph, 'E')
            self.assertEqual(result, ['E', 'C', 'A', 'B', 'D', 'F'])
            result = bfs(graph, 'E')
            self.assertEqual(result, ['E', 'C', 'A', 'B', 'D', 'F'])

            path = dfs_path(graph, 'E', 'A')    
            self.assertEqual(path, ['E', 'C', 'A'])
            path = bfs_path(graph, 'E', 'A')
            self.assertEqual(path, ['E', 'C', 'A'])
            
        for graph in (gld, gmd):
            result = dfs(graph, 'E')
            self.assertEqual(result, ['E'])
            result = bfs(graph, 'E')
            self.assertEqual(result, ['E'])
            
            path = dfs_path(graph, 'E', 'A')    
            self.assertIsNone(path)
            path = bfs_path(graph, 'E', 'A')
            self.assertIsNone(path)



    def test_weighted_traversal(self):
        gl = Graph.create_adjacency_list(directed=False, weighted=True)
        gl.add_edge('A', 'B', 1)
        gl.add_edge('A', 'C', 2)
        gl.add_edge('B', 'D', 3)
        gl.add_edge('C', 'E', 4)
        gl.add_edge('D', 'F', 5)
        
        gm = Graph.create_adjacency_matrix(directed=False, weighted=True)
        gm.add_edge('A', 'B', 1)
        gm.add_edge('A', 'C', 2)
        gm.add_edge('B', 'D', 3)
        gm.add_edge('C', 'E', 4)
        gm.add_edge('D', 'F', 5)
        
        gld = Graph.create_adjacency_list(directed=True, weighted=True)
        gld.add_edge('A', 'B', 1)
        gld.add_edge('A', 'C', 2)
        gld.add_edge('B', 'D', 3)
        gld.add_edge('C', 'E', 4)
        gld.add_edge('D', 'F', 5)
        gmd = Graph.create_adjacency_matrix(directed=True, weighted=True)
        gmd.add_edge('A', 'B', 1)
        gmd.add_edge('A', 'C', 2)
        gmd.add_edge('B', 'D', 3)
        gmd.add_edge('C', 'E', 4)
        gmd.add_edge('D', 'F', 5)
        
        for graph in (gl, gm, gld, gmd):
            result = dfs(graph, 'A')
            self.assertEqual(result, ['A', 'B', 'D', 'F', 'C', 'E'])
            result = bfs(graph, 'A')
            self.assertEqual(result, ['A', 'B', 'C', 'D', 'E', 'F'])
            
            path = dfs_path(graph, 'A', 'F')
            self.assertEqual(path, ['A', 'B', 'D', 'F'])
            path = bfs_path(graph, 'A', 'F')
            self.assertEqual(path, ['A', 'B', 'D', 'F'])

            path = dfs_path(graph, 'A', 'A')
            self.assertEqual(path, ['A'])
            path = bfs_path(graph, 'A', 'A')
            self.assertEqual(path, ['A'])
            
            path = dfs_path(graph, 'F', 'F')
            self.assertEqual(path, ['F'])
            path = bfs_path(graph, 'F', 'F')
            self.assertEqual(path, ['F'])
            
            path = dfs_path(graph, 'A', 'X')
            self.assertIsNone(path)
            path = bfs_path(graph, 'A', 'X')
            self.assertIsNone(path)

        for graph in (gl, gm):
            result = dfs(graph, 'E')
            self.assertEqual(result, ['E', 'C', 'A', 'B', 'D', 'F'])
            result = bfs(graph, 'E')
            self.assertEqual(result, ['E', 'C', 'A', 'B', 'D', 'F'])

            path = dfs_path(graph, 'E', 'A')    
            self.assertEqual(path, ['E', 'C', 'A'])
            path = bfs_path(graph, 'E', 'A')
            self.assertEqual(path, ['E', 'C', 'A'])
            
        for graph in (gld, gmd):
            result = dfs(graph, 'E')
            self.assertEqual(result, ['E'])
            result = bfs(graph, 'E')
            self.assertEqual(result, ['E'])
            
            path = dfs_path(graph, 'E', 'A')    
            self.assertIsNone(path)
            path = bfs_path(graph, 'E', 'A')
            self.assertIsNone(path)

        
        


