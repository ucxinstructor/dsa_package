""" Module containing graph classes. """

from dsa.queue import Queue

class AdjacencyMatrixGraph:
    """ 
    An unweighted adjacency matrix graph implementation.
    
    This class allows either directed or undirected representation of a graph.
    Vertex labels are string types.
    """
    def __init__(self, labels: list[str]):
        """ 
        Initialize the graph with a list of vertex labels.

        Args:
            labels (list[str]): List of labels for each vertex.
        """
        self.labels = labels
        self.label_index = { label: index for index, label  in enumerate(labels) }

        node_count = len(self.labels)
        self.array = [[None for i in range(node_count)] for j in range(node_count)]

    def add_edge(self, start_label: str, end_label: str, directed=False):
        """ 
        Add an edge in the graph.
        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
            directed (bool): Whether the edge is directed.
        """
        a = self.label_index[start_label]
        b = self.label_index[end_label]
        self.array[a][b] = True
        if not directed:
            self.array[b][a] = True

    def add_vertex(self, label: str):
        """ 
        Add a vertex to the graph.
        
        Args:
            label (str): The vertex label to add.
        """
        self.labels.append(label)
        self.label_index[label] = len(self.labels) - 1
        for row in self.array:
            row.append(None)
        self.array.append([None for i in range(len(self.labels))])

    def delete_vertex(self, label: str):
        """ 
        Delete a vertex from the graph.
        
        Args:
            label (str): The vertex label to delete.
        """
        index = self.label_index[label]
        self.labels.pop(index)
        self.label_index = { label: index for index, label in enumerate(self.labels) }
        self.array.pop(index)
        for row in self.array:
            row.pop(index)

    def delete_edge(self, start_label: str, end_label: str, directed=False):
        """ 
        Delete an edge in the graph.
        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
            directed (bool): Whether the edge is directed.
        """
        a = self.label_index[start_label]
        b = self.label_index[end_label]
        if self.array[a][b] is None:
            raise KeyError(f"Edge {start_label} to {end_label} does not exist")

        self.array[a][b] = None
        if not directed:
            if self.array[b][a] is None:
                raise KeyError(f"Edge {end_label} to {start_label} does not exist")
            self.array[b][a] = None

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

        for adj_index, is_connected in enumerate(self.array[start_index]):
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
            for i in range(len(self.array)):
                if start_index != i and self.array[current][i] and (i not in visited):
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
                if self.array[i][j] and i != j:  
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
                if self.array[i][j] and i != j and (self.labels[j], self.labels[i]) not in edges:  
                    edges.append((self.labels[i], self.labels[j]))
    
        return edges

    def is_edge(self, start_label: str, end_label: str) -> bool:
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

        return self.array[start_index][end_index] is not None

    def __getitem__(self, vertex: str) -> list:
        """ 
        Args:
            vertex (str): The vertex label.
        Returns:
            A list of adjacent vertex labels.
        """
        index = self.label_index[vertex]
        return [self.labels[i] for i in range(len(self.array[index])) if self.array[index][i]]
    
    def print_graph(self):
        """ 
        Print the contents of the graph.
        """
        print("   |", end="")
        for label in self.labels:
            print(f"{label:^3}", end=" ")
        print()
        print("----" * (len(self.array) + 1))
        for r, row in enumerate(self.array):
            label = self.labels[r]
            print(f"{label:^3}|", end="")
            for col in row:
                b = " T " if col else "   "
                print(b, end=" ")
            print()
            
class AdjacencyMatrixWeightedGraph(AdjacencyMatrixGraph):
    """ 
    A weighted adjacency matrix graph implementation
    (allows either directed or undirected representation)
    vertex labels are string types
    """
    def __init__(self, labels):
        """ 
        Args:
            labels: list of labels for each vertex (string types)
        """
        super().__init__(labels)

    def add_edge(self, start_label: str, end_label: str, weight, directed=False):
        """ 
        Add an edge to the graph.

        Args:
            start_label (str): The starting vertex label.
            end_label (str): The ending vertex label.
            weight: The weight of the vertex.
            directed: Whether the edge is directed.
        """
        a = self.label_index[start_label]
        b = self.label_index[end_label]

        self.array[a][b] = weight
        self.array[a][a] = 0
        self.array[b][b] = 0

        if not directed:
            self.array[b][a] = weight
        
    def print_graph(self):
        """ 
        Print the contents of the graph.
        """
        print("   |", end="")
        for label in self.labels:
            print(f"{label:>3}", end=" ")
        print()
        print("----" * (len(self.array) + 1))
        for r, row in enumerate(self.array):
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
                weight = self.array[i][j]
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
                weight = self.array[i][j]
                if weight and i != j and (self.labels[j], self.labels[i], weight) not in edges:  
                    edges.append((self.labels[i], self.labels[j], weight))
    
        return edges

    def is_edge(self, start_label: str, end_label: str) -> bool:
        """ 
        Return boolean if an edge exists.

        
        Args:
            start_label (str): Starting vertex label.
            end_label (str): Ending vertex label.
        
        Returns:
            A boolean of whether there is an edge from start to end.
        """
        return super().is_edge(start_label, end_label)
    
    def weightx(self, start: str, end: str) -> bool:
        """ 
        Return weight of an edge (is this used???)
        Args:
            start_label: starting vertex label
            end_label: starting vertex label
        
        Returns:
            weight value of an edge from start to end
        """
        return super().is_edge(start, end)

    def __getitem__(self, vertex: str) -> dict:
        """ 
        Args:
            vertex: vertex label
        Returns:
            a dictionary of adjacent vertex labels and weights
        """
        index = self.label_index[vertex]
        return {self.labels[i] : self.array[index][i] for i in range(len(self.array[index])) if self.array[index][i]}

class AdjacencyListGraph:
    """ 
    A unweighted adjacency list vertex implementation
    (allows either directed or undirected representation)
    vertex labels are string types
    """
    def __init__(self):
        #: hash table of vertices in graph
        self._adjacents = {}
        
    def add_edge(self, start_label: str, end_label: str, directed=False):
        """ 
        Add an edge to the graph.

        Args:
            start_label (str): The label of the starting vertex.
            end_label (str): The label of the ending vertex.
            directed (bool): Whether the edge is directed.
        """
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

    def delete_edge(self, start_label: str, end_label: str, directed=False):
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

    def is_edge(self, start_label: str, end_label: str) -> bool:
        """ 
        Return boolean if an edge exists
        Args:
            start_label (str): The starting vertex label.
            end_label (str): The ending vertex label.
        
        Returns:
            A boolean of whether there is an edge from start to end
        """
        return end_label in self[start_label]

    def __len__(self):
        """
        Return the number of nodes in the graph.
        Returns:
            int: The number of nodes in the graph.
        """
        return len(self._adjacents)

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

class AdjacencyListWeightedGraph(AdjacencyListGraph):
    """ 
    A weighted adjacency list vertex implementation in Python
    (allows either directed or undirected representation)
    """
    def __init__(self):
        #: hash table of vertices in graph
        self._adjacents = {}
        
    def add_edge(self, start_label: str, end_label: str, weight, directed=False):
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
            
        self._adjacents[start_label][end_label] = weight

        if not directed:
            if end_label not in self._adjacents:
                self._adjacents[end_label] = {}
            self._adjacents[end_label][start_label] = weight

    def delete_edge(self, start_label: str, end_label: str, directed=False):
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

    def is_edge(self, start_label: str, end_label: str) -> bool:
        """ 
        Return boolean if an edge exists
        Args:
            start_label (str): starting vertex label
            end_label (str): starting vertex label
        
        Returns:
            A boolean of whether there is an edge from start to end.
        """
        return end_label in self[start_label]



__pdoc__ = {
    'AdjacencyMatrixGraph.add_vertex': False,
    'AdjacencyMatrixGraph.delete_vertex': False,
    'AdjacencyListGraph.add_directed_edge': False,
}
