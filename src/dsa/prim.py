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

    dist_table = {}
    pred_table = {}
    visited = set()
    pq = PriorityQueue()

    for vertex in graph.vertices():
        dist_table[vertex] = float('inf')
        pred_table[vertex] = None

    # insert starting vertex with weight 0
    pq.insert(0, start)
    dist_table[start] = 0

    while not pq.is_empty():
        current_weight, current_vertex = pq.extract_min_pair()
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for adjacent, distance in graph.adjacent_items(current_vertex):
            if adjacent in visited:
                continue

            new_dist = distance

            if debug:
                print("current_vertex ", current_vertex, " adjacent ", adjacent, " distance ", distance, " new_dist ", new_dist, " predecessor ", pred_table, "visited ", visited)
            if new_dist < dist_table[adjacent]:
                dist_table[adjacent] = new_dist
                pred_table[adjacent] = current_vertex
                pq.insert(new_dist, adjacent)
                if debug:
                    print(dist_table)
    return dist_table, pred_table

def reconstruct_mst(dist_table: dict, pred_table: dict, representation: str = "list") -> Graph:
    """
    Reconstructs a minimum spanning tree (MST) from the distance table and predecessor table
    
    Args:
        dist_table (dict): A hashtable of vertex labels and their distances from the starting vertex in the MST. Set to None if there are no weights available.
        predecessor_table (dict): A hashtable of vertex labels and their predecessors in the MST.
    Returns:
        Graph: The minimum spanning tree of the graph.
    """
    mst = Graph(representation=representation, directed=False, weighted=True)

    for vertex, connection in pred_table.items():
        if connection is None or vertex == connection:
            continue

        # If dist_table is provided, use it to get the weight of the edge; otherwise, default to 1
        w = dist_table[vertex] if dist_table else 1
        print(vertex, connection, w)
        mst.add_edge(connection, vertex, w)

    return mst

def get_mst(graph: Graph, start: str, debug: bool = False) -> Graph:
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
    mst = reconstruct_mst(weight_table, predecessor_table)

    return mst

def prim_simple(graph, start: str, mst_graph = None) -> Graph:
    """
    Returns an MST given a graph and starting vertex. Uses a simpler implementation of Prim's algorithm that does not return weight and predecessor tables.

    Args:
        graph: The graph to search an MST from. (can be either an AdjacencyListWeightedGraph or AdjacencyMatrixWeightedGraph)
        start (string): The starting vertex label.
        mst_graph: An empty graph object to output the MST in to. If not specified, a new AdjacencyListWeightedGraph will be created.

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

def get_total_weight(graph) -> int:
    """
    Returns the total weight of a graph given a starting vertex
    
    Args:
        graph: The graph to find the total edge weight of.

    Returns:
        int: The total weight of the graph.
    """
    total_weight = 0
    visited_edges = set()

    for u in graph.vertices():
        for v in graph.adjacents(u):
            # Sort the pair so (A, B) and (B, A) look identical
            edge = tuple(sorted((u, v)))
            
            if edge not in visited_edges:
                total_weight += graph.weight(u, v)
                visited_edges.add(edge)
                
    return total_weight