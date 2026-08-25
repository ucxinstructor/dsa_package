""" Module to access functions for Prim's Algorithm. """
from dsa.graph import Graph
from dsa.heap import PriorityQueue

def prim(graph: Graph, start: str, debug: bool = False) -> tuple:
    """ 
    Helper function that returns a weight table and a predecessor table for Prim's Algorithm.

    Args:
        graph (Graph): The graph to search.
        start (str): The starting vertex label.
        end (str): The ending vertex label.
        debug (bool): If True, display weight table as it is being built.
    
    Raises:
        KeyError: If start or end vertex is not in the graph.

    Returns:
        A tuple of a weight table hashtable and a predecessor hashtable.
    """
    if start not in graph:
        raise KeyError(f"Start vertex {start} not in graph.")

    weight_table = {start: 0}
    predecessor = {start: start}
    visited = set()
    pq = PriorityQueue()

    # insert starting vertex with weight 0
    pq.insert(0, start)
    
    while not pq.is_empty():
        current_weight, current_vertex = pq.extract_min_pair()
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for adjacent, weight in graph.adjacent_items(current_vertex):
            if adjacent in visited:
                continue

            new_dist = weight

            if debug:
                print("current_vertex ", current_vertex, " adjacent ", adjacent, " weight ", weight, " new_dist ", new_dist, " predecessor ", predecessor, "visited ", visited)
            if new_dist < weight_table.get(adjacent, float('inf')):
                weight_table[adjacent] = new_dist
                predecessor[adjacent] = current_vertex
                pq.insert(new_dist, adjacent)
                if debug:
                    print(weight_table)
    return weight_table, predecessor

def reconstruct_mst(predecessor_table: dict, dist_table=None):
    """
    Reconstructs a minimum spanning tree (MST) from the predecessor table and distance table
    
    Args:
        predecessor_table (dict): A hashtable of vertex labels and their predecessors in the MST.
        dist_table (dict): A hashtable of vertex labels and their distances from the starting vertex in the MST.
    Returns:
        Graph: The minimum spanning tree of the graph.
    """
    mst = Graph.create_adjacency_list(directed=False, weighted=True)

    for vertex, parent in predecessor_table.items():
        if parent is None or vertex == parent:
            continue
            
        w = dist_table[vertex] if dist_table else 1
        print(vertex, parent, w)
        mst.add_edge(parent, vertex, w)

    return mst

def get_mst(graph: Graph, start: str, debug: bool=False) -> Graph:
    """
    Returns a minimum spanning tree (MST) of the given graph starting from the specified vertex.

    Args:
        graph (Graph): The graph to search.
        start (str): The starting vertex label.
        debug (bool): If True, display weight table as it is being built.

    Raises:
        KeyError: If start vertex is not in the graph.

    Returns:
        Graph: The minimum spanning tree of the graph.
    """
    weight_table, predecessor_table = prim(graph, start, debug)
    mst = reconstruct_mst(predecessor_table, weight_table)

    return mst

def prim_simple(graph, start: str, mst_graph=None) -> Graph:
    """
    Returns an MST given a graph and starting vertex.
    (Future: return a Tree type instead of a Graph type)

    Args:
        graph: The graph to search an MST from. (can be either an AdjacencyListWeightedGraph or AdjacencyMatrixWeightedGraph)
        start (string): The starting vertex label.
        mst_graph: An empty graph object to output the MST in to.

    Returns:
        AdjacencyListWeightedGraph: the MST of the graph.
    """
    def add_adjacent(graph, pq: PriorityQueue, visited: set, node: str):
        """Add all adjacent vertices from the given node to the priority queue."""
        visited.add(node)
        for adjacent, weight in graph[node].items():
            if adjacent not in visited:
                pq.insert(weight, (node, adjacent))  # Push edge with weight as priority

    if mst_graph is None:
        mst_graph = Graph.create_adjacency_list(directed=False, weighted=True)

    visited = set()
    pq = PriorityQueue()
    total_vertices = len(set(graph.vertices()))

    add_adjacent(graph, pq, visited, start)

    # While the priority queue is not empty and we haven't visited all vertices
    while not pq.is_empty() and len(visited) < total_vertices:
        weight, edge = pq.extract_min_pair()
        start, end = edge
        # If the end vertex has not been visited, add edge to the MST
        if end not in visited:
            mst_graph.add_edge(start, end, graph[start][end])
            # add adjacent vertices to the priority queue and mark the end vertex as visited
            add_adjacent(graph, pq, visited, end)
    return mst_graph

def mst_weight(graph) -> int:
    """
    Returns the total weight of a graph given a starting vertex
    
    Args:
        graph: The graph to find the total edge weight of.

    Returns:
        int: The total weight of the graph.
    """
    total_weight = 0
    visited = set()
    for start, end, weight in graph.edges():
        if (start, end) not in visited:
            total_weight += weight
            visited.add((start, end))
            visited.add((end, start))
    return total_weight