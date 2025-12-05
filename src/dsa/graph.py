""" Module containing graph classes. """

from tkinter import N
from turtle import st
from venv import create
from dsa.queue import Queue

class Graph:
    """
    Graph Factory
    
    """
    @staticmethod
    def create(graph_type: str, directed: bool=False, weighted: bool=False, vertices=None) -> object:
        """ 
        Return a graph object based on the specified parameters.

        Args:
            graph_type: The type of graph ('adjacency_matrix' or 'adjacency_list').
            directed: Whether the graph is directed.
            weighted: Whether the graph is weighted.
            labels (list[str], optional): List of vertex labels for adjacency matrix graphs. Defaults to [].
        """
        if graph_type == 'adjacency_matrix':
            if vertices is None:
                vertices = []
            return Graph.create_adjacency_matrix(directed=directed, weighted=weighted, vertices=vertices)
        elif graph_type == 'adjacency_list':
            return Graph.create_adjacency_list(directed=directed, weighted=weighted, vertices=vertices)
        else:
            raise ValueError("Invalid graph type. Use 'adjacency_matrix' or 'adjacency_list'.")
    
    @staticmethod
    def create_adjacency_matrix(directed: bool=False, weighted: bool=False, vertices=None) -> object:
        """ 
        Return an adjacency matrix graph object.

        Args:
            directed: Whether the graph is directed.
            weighted: Whether the graph is weighted.
            labels (list[str], optional): List of vertex labels for adjacency matrix graphs. Defaults to [].
        """
        if vertices is None:
            vertices = []
        if weighted:
            return AdjacencyMatrixWeightedGraph(directed=directed, vertices=vertices)
        else:
            return AdjacencyMatrixGraph(directed=directed, vertices=vertices)
    
    @staticmethod
    def create_adjacency_list(directed: bool=False, weighted: bool=False, vertices=None) -> object:
        """ 
        Return an adjacency list graph object.

        Args:
            directed: Whether the graph is directed.
            weighted: Whether the graph is weighted.
            labels (list[str], optional): List of vertex labels for adjacency matrix graphs. Defaults to [].
        """
        if weighted:
            return AdjacencyListWeightedGraph(directed=directed, vertices=vertices)
        else:
            return AdjacencyListGraph(directed=directed, vertices=vertices)

class AdjacencyMatrixGraph:
    """ 
    An unweighted adjacency matrix graph implementation.
    
    This class allows either directed or undirected representation of a graph.
    Vertex labels are string types.
    """
    def __init__(self, directed=False, weighted=False, vertices=None):
        """
        Initialize the graph with optional vertex labels.
        
        Args:
            directed (bool): Whether the graph is directed.
            vertices (list[str]): List of labels for each vertex.

        """
        if vertices is None:
            vertices = []

        self.labels = list(vertices)

        # Prevent duplicates
        if len(self.labels) != len(set(self.labels)):
            raise ValueError("Duplicate vertex labels are not allowed.")

        self.is_directed = directed
        self.is_weighted = weighted

        # Map labels to indices
        self.label_index = {label: i for i, label in enumerate(self.labels)}

        # Initialize matrix
        n = len(self.labels)
        self._matrix = [[None for _ in range(n)] for _ in range(n)]


    def add_edge(self, start_label: str, end_label: str, directed=None):
        """ 
        Add an edge in the graph.
        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
            directed (bool): Whether the edge is directed.
        """
        if start_label not in self.label_index:
            self.add_vertex(start_label)
        if end_label not in self.label_index:
            self.add_vertex(end_label)
        
        a = self.label_index[start_label]
        b = self.label_index[end_label]
        self._matrix[a][b] = True

        if directed is None:            
            directed = self.is_directed
        
        if not directed:
            self._matrix[b][a] = True

    def add_vertex(self, label: str):
        """ 
        Add a vertex to the graph.
        
        Args:
            label (str): The vertex label to add.
        
        Raises:
            ValueError: If the vertex label already exists.
        """
        if label in self.label_index:
            raise ValueError(f"Vertex {label} already exists")
        self.labels.append(label)
        self.label_index[label] = len(self.labels) - 1
        for row in self._matrix:
            row.append(None)
        self._matrix.append([None for i in range(len(self.labels))])

    def delete_vertex(self, label: str):
        """ 
        Delete a vertex from the graph.
        
        Args:
            label (str): The vertex label to delete.
        """
        index = self.label_index[label]
        self.labels.pop(index)
        self.label_index = { label: index for index, label in enumerate(self.labels) }
        self._matrix.pop(index)
        for row in self._matrix:
            row.pop(index)

    def delete_edge(self, start_label: str, end_label: str, directed=None):
        """ 
        Delete an edge in the graph.
        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
            directed (bool): Whether the edge is directed.
        """
        a = self.label_index[start_label]
        b = self.label_index[end_label]
        if self._matrix[a][b] is None:
            raise KeyError(f"Edge {start_label} to {end_label} does not exist")

        self._matrix[a][b] = None
        
        if directed is None:
            directed = self.is_directed
        
        if not directed:
            if self._matrix[b][a] is None:
                raise KeyError(f"Edge {end_label} to {start_label} does not exist")
            self._matrix[b][a] = None

    def dfs_traverse(self, start_label: str):
        """ 
        Perform depth first traversal in an adjacency matrix
 
        Args:
            start_label (str): Starting vertex label.
        
        Returns:
            Array with depth first order traversal.
        """
        return self._df_rec_traverse(start_label, set(), [])
        
    def _df_rec_traverse(self, start_label: str, visited, dfs):
        """ 
        Helper method for depth first recursive traversal
        """
        start_index = self.label_index[start_label]
        visited.add(start_label)
        dfs.append(self.labels[start_index])

        for adj_index, is_connected in enumerate(self._matrix[start_index]):
            adj_label = self.labels[adj_index]
            if is_connected and adj_label not in visited:
                self._df_rec_traverse(adj_label, visited, dfs)

        return dfs

    def bfs_traverse(self, start_label: str):
        """ 
        Perform breadth first traversal in an adjacency matrix.
 
        Args:
            start_label (str): Starting vertex label.
        
        Returns:
            Array with breadth first order traversal.
        """
        bfs = []
        q = Queue()
        visited = set()

        start_index = self.label_index[start_label]
        q.enqueue(start_index)
        bfs.append(self.labels[start_index])
        while not q.is_empty():
            current = q.dequeue()
            for i in range(len(self._matrix)):
                if start_index != i and self._matrix[current][i] and (i not in visited):
                    visited.add(i)
                    q.enqueue(i)
                    bfs.append(self.labels[i])
        return bfs
    
    def vertices(self) -> list:
        """
        Return a list of vertex labels of the graph
        """
        return self.labels
    
    def edges(self) -> list:
        """ 
        Return a list of edges in the graph. Each edge is represented by a tuple (start, end)
        """
        edges = []
        vertex_count = len(self.labels)
        for i in range(vertex_count):
            for j in range(vertex_count):
                if self._matrix[i][j] and i != j:  
                    edges.append((self.labels[i], self.labels[j]))
    
        return edges

    def undirected_edges(self) -> list:
        """ 
        Return a list of undirected edges in the graph. Each edge is represented by a tuple (start, end)
        """
        edges = []
        vertex_count = len(self.labels)
        for i in range(vertex_count):
            for j in range(vertex_count):
                if self._matrix[i][j] and i != j and (self.labels[j], self.labels[i]) not in edges:  
                    edges.append((self.labels[i], self.labels[j]))
    
        return edges

    def has_edge(self, start_label: str, end_label: str) -> bool:
        """ 
        Return boolean if an edge exists.

        Args:
            start_label (str): starting vertex label
            end_label (str): starting vertex label
        
        Returns:0
            A boolean of whether there is an edge from start to end.
        """
        start_index = self.label_index[start_label]
        end_index = self.label_index[end_label]

        return self._matrix[start_index][end_index] is not None

    def __getitem__(self, vertex: str) -> list:
        """ 
        Args:
            vertex (str): The vertex label.
        Returns:
            A list of adjacent vertex labels.
        """
        index = self.label_index[vertex]
        return [self.labels[i] for i in range(len(self._matrix[index])) if self._matrix[index][i]]
    
    def __contains__(self, label: str) -> bool:
        """ 
        Args:
            label (str): The vertex label.
        Returns:
            A boolean indicating if the vertex is in the graph.
        """
        return label in self.label_index
    
    def print_graph(self):
        """ 
        Print the contents of the graph.
        """
        print("   |", end="")
        for label in self.labels:
            print(f"{label:^3}", end=" ")
        print()
        print("----" * (len(self._matrix) + 1))
        for r, row in enumerate(self._matrix):
            label = self.labels[r]
            print(f"{label:^3}|", end="")
            for col in row:
                b = " T " if col else "   "
                print(b, end=" ")
            print()
            
    def order(self) -> int:
        """
        Return the number of nodes in the graph.
        Returns:
            int: The number of nodes in the graph.
        """
        return len(self.labels)
    
    def __len__(self):
        """
        Return the number of nodes in the graph.
        """
        return len(self.labels)
            
    def size(self) -> int:
        """
        Return the number of edges in the graph.
        Returns:
            int: The number of edges in the graph.
        """
        edge_count = 0
        for start in self.labels:
            edge_count += len(self[start])
        if not self.is_directed:
            edge_count = edge_count // 2
        return edge_count
    
    def to_dict(self) -> dict:
        """ 
        Return the adjacency matrix as a dictionary.
        
        For unweighted graphs, returns a dictionary of lists.
        For weighted graphs, returns a dictionary of dictionaries.
        
        Returns:
            A dictionary representing the adjacency matrix of the graph.
            - Unweighted: {vertex: [neighbor1, neighbor2, ...]}
            - Weighted: {vertex: {neighbor1: weight1, neighbor2: weight2, ...}}
        """
        matrix_dict = {}
        
        for i, row in enumerate(self._matrix):
            if self.is_weighted:
                matrix_dict[self.labels[i]] = {}
            else:
                matrix_dict[self.labels[i]] = []
            
            for j, val in enumerate(row):
                if val is not None:
                    if self.is_weighted:
                        matrix_dict[self.labels[i]][self.labels[j]] = val
                    else:
                        matrix_dict[self.labels[i]].append(self.labels[j])
        
        return matrix_dict

class AdjacencyMatrixWeightedGraph(AdjacencyMatrixGraph):
    """ 
    A weighted adjacency matrix graph implementation
    (allows either directed or undirected representation)
    vertex labels are string types
    """
    def __init__(self, directed=False, vertices=None):
        """ 
        Args:
            vertices: list of labels for each vertex (string types)
        """
        super().__init__(directed=directed, vertices=vertices)
        self.is_weighted=True

    def add_edge(self, start_label: str, end_label: str, weight, directed=None):
        """ 
        Add an edge to the graph.

        Args:
            start_label (str): The starting vertex label.
            end_label (str): The ending vertex label.
            weight: The weight of the vertex.
            directed: Whether the edge is directed.
        """
        if start_label not in self.label_index:
            self.add_vertex(start_label)
        if end_label not in self.label_index:
            self.add_vertex(end_label)

        a = self.label_index[start_label]
        b = self.label_index[end_label]

        self._matrix[a][b] = weight
        self._matrix[a][a] = None # prevent self-loop
        self._matrix[b][b] = None

        if directed is None:
            directed = self.is_directed

        if not directed:
            self._matrix[b][a] = weight
        
    def print_graph(self):
        """ 
        Print the contents of the graph.
        """
        print("   |", end="")
        for label in self.labels:
            print(f"{label:>3}", end=" ")
        print()
        print("----" * (len(self._matrix) + 1))
        for r, row in enumerate(self._matrix):
            label = self.labels[r]
            print(f"{label:^3}|", end="")
            for col in row:
                w = f"{col:3}" if col is not None else "   "
                print(w, end=" ")
            print()

    def edges(self) -> list:
        """ 
        Return a list of edges in the graph. Each edge is represented by a tuple (start, end, weight).
        """
        edges = []
        vertex_count = len(self.labels)
        for i in range(vertex_count):
            for j in range(vertex_count):
                weight = self._matrix[i][j]
                if weight and i != j:  
                    edges.append((self.labels[i], self.labels[j], weight))
    
        return edges
    
    def undirected_edges(self) -> list:
        """ 
        Return a list of undirected edges in the graph. Each edge is represented by a tuple (start, end, weight).
        """
        edges = []
        vertex_count = len(self.labels)
        for i in range(vertex_count):
            for j in range(vertex_count):
                weight = self._matrix[i][j]
                if weight and i != j and (self.labels[j], self.labels[i], weight) not in edges:  
                    edges.append((self.labels[i], self.labels[j], weight))
    
        return edges

    # def has_edge(self, start_label: str, end_label: str) -> bool:
    #     """ 
    #     Return boolean if an edge exists.

        
    #     Args:
    #         start_label (str): Starting vertex label.
    #         end_label (str): Ending vertex label.
        
    #     Returns:
    #         A boolean of whether there is an edge from start to end.
    #     """
    #     return super().has_edge(start_label, end_label)
    
    def get_weight(self, start_label: str, end_label: str):
        """ 
        Get the weight of an edge.

        Args:
            start_label: The starting vertex label. 
            end_label: The ending vertex label. 

        Returns:
            The weight of the edge from start to end.
        """
        start_index = self.label_index[start_label]
        end_index = self.label_index[end_label]

        return self._matrix[start_index][end_index]

    def __getitem__(self, vertex: str) -> dict:
        """ 
        Args:
            vertex: vertex label
        Returns:
            a dictionary of adjacent vertex labels and weights
        """
        index = self.label_index[vertex]
        return {self.labels[i] : self._matrix[index][i] for i in range(len(self._matrix[index])) if self._matrix[index][i]}

class AdjacencyListGraph:
    """ 
    A unweighted adjacency list vertex implementation
    (allows either directed or undirected representation)
    vertex labels are string types
    """
    def __init__(self, directed=False, vertices=None):
        #: hash table of vertices in graph
        self._adjacents = {}
        self.is_directed = directed
        self.is_weighted = False
        if vertices is None:
            vertices = []
        for vertex in vertices:
            self.add_vertex(vertex)


    def add_vertex(self, label: str):
        """ 
        Add a vertex to the graph.

        Args:
            label (str): The vertex label to add.
            
        Raises:
            ValueError: If the vertex label already exists.
        """
        if label in self._adjacents:
            raise ValueError(f"Vertex {label} already exists")
        
        self._adjacents[label] = []

    def delete_vertex(self, label: str):
        """ 
        Delete a vertex from the graph.

        Args:
            label (str): The vertex label to delete.
        """
        if label in self._adjacents:
            del self._adjacents[label]
        for key in self._adjacents.keys():
            if label in self._adjacents[key]:
                self._adjacents[key].remove(label)
        
    def add_edge(self, start_label: str, end_label: str, directed=None):
        """ 
        Add an edge to the graph.

        Args:
            start_label (str): The label of the starting vertex.
            end_label (str): The label of the ending vertex.
            directed (bool): Whether the edge is directed.
        """
        if directed is None:
            directed = self.is_directed

        self.add_directed_edge(start_label, end_label)
        if not directed:
            self.add_directed_edge(end_label, start_label)
                
    def add_directed_edge(self, start_label: str, end_label: str):
        """ 
        Add a directed edge to the graph.

        Args:
            start_label (str): The label of the starting vertex.
            end_label (str): The label of the ending vertex.
        """
        if start_label not in self._adjacents:
            self._adjacents[start_label] = [end_label]
        else:
            if end_label not in self._adjacents[start_label]:
                self._adjacents[start_label].append(end_label)
        if end_label not in self._adjacents:
            self._adjacents[end_label] = []

    def delete_edge(self, start_label: str, end_label: str, directed=None):
        """ 
        Delete an edge in the graph.
        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
            directed (bool): Whether the edge is directed.
        Raises:
            KeyError: If the edge does exist.
        """
        if start_label not in self._adjacents:
            raise KeyError(f"Vertex {start_label} does not exist")
        if end_label not in self._adjacents[start_label]:
            raise KeyError(f"Vertex {end_label} does not exist")
        self._adjacents[start_label].remove(end_label)
        
        if directed is None:
            directed = self.is_directed

        if not directed:
            if end_label not in self._adjacents:
                raise KeyError(f"Vertex {end_label} does not exist")
            if start_label not in self._adjacents[end_label]:
                raise KeyError(f"Vertex {start_label} does not exist")
            self._adjacents[end_label].remove(start_label)

    def vertices(self) -> list:
        """
        Return a list of vertex labels of the graph
        """
        return list(self._adjacents.keys())
  
    def adjacents(self, vertex: str) -> list:
        """
        Return a list of adjacents of a given vertex

        Args:
            vertex (str): The label of the vertex.
        """
        return self._adjacents[vertex]

    def dfs_traverse(self, start_label: str):
        """
        Return a list of vertices through depth first traversal starting at a given vertex.

        Args:
            start_label (str): The starting vertex label.
        Returns:
            A list of vertex labels.
        """
        return self._df_rec_traverse(start_label, set(), [])

    def _df_rec_traverse(self, start_label: str, visited, dflist):
        """
        Helper depth first traversal recursive function.
        """
        visited.add(start_label)
        dflist.append(start_label)
        
        for v in self[start_label]:
            if v not in visited:
                self._df_rec_traverse(v, visited, dflist)
        return dflist
    
    def bfs_traverse(self, start_label: str):
        """
        Return a list of vertices through breadth first traversal starting at a given vertex
        Args:
            start_label (str): The starting vertex label.
        Returns:
            A list of vertex labels.
        """
        visited = set()
        q = Queue()
        bflist = []

        q.enqueue(start_label)
        visited.add(start_label)
        bflist.append(start_label)

        while len(q) > 0:
            current = q.dequeue()

            for v in self[current]:
                if v not in visited:               
                    visited.add(v)
                    q.enqueue(v)
                    bflist.append(v)
        return bflist
        
    def dfs(self, start_label:str, end_label:str) -> str:
        """ 
        Recursive depth first search.

        Args:
            start_label (str): The starting vertex label.
            end_label (str): The vertex label to search for.

        Returns:
            A vertex in the graph if found, None otherwise.
        """
        def dfs_rec(current: str, end: str, visited):
            if current == end:
                return current

            visited.add(current)

            for v in self.adjacents(current):
                if v not in visited:
                    result = dfs_rec(v, end, visited)
                    if result is not None:
                        return result
            
            return None
        
        return dfs_rec(start_label, end_label, set())
    
    def bfs(self, start_label: str, end_label: str) -> str:
        """ 
        Breadth first search.

        Args:
            start_label (str): The starting vertex label.
            end_label (str): The vertex label to search for.

        Returns:
            A vertex in the graph if found, None otherwise.
        """
        visited = set()
        queue = Queue()
        
        visited.add(start_label)
        queue.enqueue(start_label)

        while len(queue) > 0:
            current = queue.dequeue()
            
            if current == end_label:
                return current
            
            for v in self[current]:
                if v not in visited:               
                    visited.add(v)
                    queue.enqueue(v)
        
        return None
    
    def __getitem__(self, label: str):
        """ 
        Args:
            vertex: vertex label
        Returns:
            a list of adjacent vertex labels
        """

        return self._adjacents[label]

    def has_edge(self, start_label: str, end_label: str) -> bool:
        """ 
        Return boolean if an edge exists
        Args:
            start_label (str): The starting vertex label.
            end_label (str): The ending vertex label.
        
        Returns:
            A boolean of whether there is an edge from start to end
        """
        return end_label in self[start_label]

    def size(self) -> int:
        """
        Return the number of edges in the graph.
        Returns:
            int: The number of edges in the graph.
        """
        edge_count = 0
        for start in self._adjacents.keys():
            edge_count += len(self.adjacents(start))
        if not self.is_directed:
            edge_count = edge_count // 2
        return edge_count

    def __len__(self):
        """
        Return the number of nodes in the graph.
        Returns:
            int: The number of nodes in the graph.
        """
        return len(self._adjacents)


    def order(self) -> int:
        """
        Return the number of nodes in the graph.
        Returns:
            int: The number of nodes in the graph.
        """
        return len(self._adjacents)

    def __contains__(self, label: str) -> bool:
        """ 
        Args:
            label (str): The vertex label.
        Returns:
            A boolean indicating if the vertex is in the graph.
        """
        return label in self._adjacents

    def edges(self) -> list:
        """ 
        Return a list of edges in the graph. Each edge is represented by a tuple (start, end)
        """
        edges = []
        for start in self._adjacents.keys():
            for end in self.adjacents(start):
                if start != end:  
                    edges.append((start, end))
        return edges

    def undirected_edges(self) -> list:
        """ 
        Return a list of undirected edges in the graph. Each edge is represented by a tuple (start, end)
        """
        edges = []
        for start in self._adjacents.keys():
            for end in self.adjacents(start):
                if start != end and (end, start) not in edges:  
                    edges.append((start, end))
        return edges
    
    def to_dict(self) -> dict:
        """ 
        Return the adjacency list as a dictionary.
        
        For unweighted graphs, returns a dictionary of lists.
        For weighted graphs, returns a dictionary of dictionaries.
        
        Returns:
            A dictionary representing the adjacency list of the graph.
            - Unweighted: {vertex: [neighbor1, neighbor2, ...]}
            - Weighted: {vertex: {neighbor1: weight1, neighbor2: weight2, ...}}
        """
        return {key: values.copy() for key, values in self._adjacents.items()}
    
class AdjacencyListWeightedGraph(AdjacencyListGraph):
    """ 
    A weighted adjacency list vertex implementation in Python
    (allows either directed or undirected representation)
    """
    def __init__(self, directed=False, vertices=None):
        #: hash table of vertices in graph
        super().__init__(directed=directed, vertices=vertices)
        self._adjacents = {}
        self.is_weighted = True
        
    def add_edge(self, start_label: str, end_label: str, weight, directed=None):
        """ 
        Add an edge to the graph.

        Args:
            start_label: The starting vertex label. 
            end_label: The ending vertex label. 
            weight: The edge weight.
            directed: Whether the edge is directed.
        """
        if start_label not in self._adjacents:
            self._adjacents[start_label] = {}

        if end_label not in self._adjacents:
            self._adjacents[end_label] = {}
            
        self._adjacents[start_label][end_label] = weight

        if directed is None:
            directed = self.is_directed

        if not directed:
            self._adjacents[end_label][start_label] = weight

    def delete_edge(self, start_label: str, end_label: str, directed=None):
        """ 
        Delete an edge in the graph.
        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
            directed (bool): Whether the edge is directed.

        Raises:
            KeyError: If the edge does exist.
        """
        if start_label not in self._adjacents:
            raise KeyError(f"Vertex {start_label} does not exist")
        if end_label not in self._adjacents[start_label]:
            raise KeyError(f"Vertex {end_label} does not exist") 
        del self._adjacents[start_label][end_label]
        
        if directed is None:
            directed = self.is_directed
        
        if not directed:
            if end_label not in self._adjacents:
                raise KeyError(f"Vertex {end_label} does not exist")
            if start_label not in self._adjacents[end_label]:
                raise KeyError(f"Vertex {start_label} does not exist") 
            del self._adjacents[end_label][start_label]

    def adjacents(self, vertex: str) -> list:
        """
        Return a list of adjacents of a given vertex
        Args:
            vertex: starting vertex label 
        """
        return self._adjacents[vertex]

    def get_weight(self, start_label: str, end_label: str):
        """ 
        Get the weight of an edge.

        Args:
            start_label: The starting vertex label. 
            end_label: The ending vertex label. 

        Returns:
            The weight of the edge from start to end.
        """
        return self._adjacents[start_label][end_label]

    def dfs_traverse(self):
        """
        Perform depth first traversal.
        """
        return self._df_traverse_rec(self, set())

    def _df_traverse_rec(self, vertex, visited=None):
        """
        helper depth first traversal recursive function
        """
        visited.add(vertex)
        
        for v in vertex.adjacents:
            if v not in visited:
                v._df_traverse_rec(v, visited)
            
    def bfs_traverse(self):
        """
        Perform breadth first traversal.
        """
        start = self
        visited = set()
        queue = Queue()
        
        queue.enqueue(start)

        while len(queue) > 0:
            current = queue.dequeue()
            
            if current not in visited:               
                visited.add(current)
        
                for v in current.adjacents:
                    queue.enqueue(v)
        
    def dfs(self, start_label: str, end_label: str) -> str:
        """ 
        Recursive depth first search.

        Args:
            start_label: The starting vertex label. 
            end_label: The vertex label to search for. 
        Returns:
            vertex in the graph
            none if not found.
        """
        return self.dfs_rec(start_label, end_label, set())
        
    def dfs_rec(self, current, end_label, visited=None):
        """
        Helper depth-first search recursive function.

        Args:
            current: Current vertex
            end_label: Target vertex label
            visited: Set of visited vertices 

        Returns:
            vertex in the graph if found, None otherwise.
        """
        if visited is None:
            visited = set()
        
        if current == end_label:
            return current

        visited.add(current)
        
        for v in self.adjacents(current):
            if v not in visited:
                result = self.dfs_rec(v, end_label, visited)
                if result is not None:
                    return result
        
        return None


    def bfs(self, start_label: str, end_label: str) -> str:
        """ 
        Recursive breadth first search.

        Args:
            end: vertex to search for

        Returns:
            vertex in the graph
            None if not found.
        """
        visited = set()
        queue = Queue()
        
        visited.add(start_label)
        queue.enqueue(start_label)

        while not queue.is_empty():
            current = queue.dequeue()
            
            if current == end_label:
                return current
            
            for v in self[current]:
                if v not in visited:
                    visited.add(v)
                    queue.enqueue(v)
        
        return None

    def __getitem__(self, vertex: str) -> dict:
        """
        Args:
            vertex: vertex label
        Returns:
        Return a hashtable of adjacent vertices
        """
        if vertex not in self._adjacents:
            return {}
        return self._adjacents[vertex]

    def __len__(self):
        """
        Return the number of nodes in the graph.

        Returns:
            int: The number of nodes in the graph.
        """
        return len(self._adjacents)

    def edges(self) -> list:
        """ 
        Return a list of edges in the graph. Each edge is represented by a tuple (start, end, weight)
        """
        edges = []
        for start in self._adjacents.keys():
            for end in self.adjacents(start):
                weight = self[start][end]
                if start != end:  
                    edges.append((start, end, weight))
        return edges

    def undirected_edges(self) -> list:
        """ 
        Return a list of undirected edges in the graph. Each edge is represented by a tuple (start, end, weight)
        """
        edges = []
        for start in self._adjacents.keys():
            for end in self.adjacents(start):
                weight = self[start][end]
                if start != end and (end, start, weight) not in edges:  
                    edges.append((start, end, weight))
        return edges

    def has_edge(self, start_label: str, end_label: str) -> bool:
        """ 
        Return boolean if an edge exists
        Args:
            start_label (str): starting vertex label
            end_label (str): starting vertex label
        
        Returns:
            A boolean of whether there is an edge from start to end.
        """
        return end_label in self[start_label]

