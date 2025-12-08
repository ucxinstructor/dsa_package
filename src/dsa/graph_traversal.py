from dsa.queue import DynamicQueue

def dfs(graph, vertex: str, visited=None, path=None, debug=False, stack=None) -> list:
    """
    Depth-first traversal.
    
    Args:
        graph: Graph object with an adjacents(v) method
        vertex (str): Starting vertex
        visited (set): Set of visited vertices
        path (list): Traversal order result
        debug (bool): If True, print internal state
        stack (list): Internal recursion stack (debug only)
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if stack is None:
        stack = []

    visited.add(vertex)
    stack.append(vertex)
    path.append(vertex)

    if debug:
        print(f"Current: {vertex}\tAdjacents: {graph.adjacents(vertex)}")
        print(f"Stack: {stack}")
        print(f"Visited: {visited}")

    for adjacent in graph.adjacents(vertex):
        if adjacent not in visited:
            dfs(graph, adjacent, visited, path, debug, stack)

    stack.pop()

    if debug:
        print(f"Stack: {stack}")

    return path

def dfs_path(graph, start: str, end: str, visited=None) -> list | None:
    """
    
    Return a path from start to end using DFS, or None if not found.
    
    Args:
        graph: Graph object with an adjacents(v) method.
        start: Starting vertex.
        end: Ending vertex.
        visited (set): Set of visited vertices.

    Returns:
        list or None: Path from start to end if exists, else None.
    """
    if visited is None:
        visited = set()

    visited.add(start)

    # Base case: start == end
    if start == end:
        return [start]

    # Explore neighbors
    for adjacent in graph.adjacents(start):
        if adjacent not in visited:
            subpath = dfs_path(graph, adjacent, end, visited)
            if subpath is not None:
                return [start] + subpath

    # No path through this branch
    return None

def bfs(graph, start: str, debug=False) -> list:
    """
    Breadth-first traversal.

    Args:
        graph: Graph object with an adjacents(v) method.
        start (str): Starting vertex.
        debug (bool): If True, print internal state.

    Returns:
        list: The vertices in BFS order.
    """
    queue = DynamicQueue()
    visited = set()
    path = []

    visited.add(start)
    queue.enqueue(start)

    if debug:
        print(f"Queue: {queue}")

    while not queue.is_empty():
        current = queue.dequeue()

        if debug:
            print(f"Current: {current}\tAdjacents: {graph.adjacents(current)}")

        path.append(current)

        for adjacent in graph.adjacents(current):
            if adjacent not in visited:
                visited.add(adjacent)
                queue.enqueue(adjacent)

        if debug:
            print(f"Queue: {queue}")

    return path
    

def bfs_path(graph, start: str, end: str) -> list | None:
    """
    Return the shortest path from start to end using BFS.
    If no path exists, return None.
    
    Args:
        graph: Graph object with an adjacents(v) method.
        start (str): Starting vertex.
        end (str): Ending vertex.
    """
    queue = DynamicQueue()
    visited = set()
    parent = {start: None}   # used to reconstruct the path

    queue.enqueue(start)
    visited.add(start)

    while queue:
        current = queue.dequeue()

        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))

        for adjacent in graph.adjacents(current):
            if adjacent not in visited:
                visited.add(adjacent)
                parent[adjacent] = current
                queue.enqueue(adjacent)

    return None