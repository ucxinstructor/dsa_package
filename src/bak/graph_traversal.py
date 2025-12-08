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
    
    
    
    
## adjacecy list weighted graph
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
    
    
    # adjacency matrix graph
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
    
    
    
    # adjacency list graph
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