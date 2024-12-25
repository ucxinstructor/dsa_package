""" Module to access functions for Prim's Algorithm. """
from dsa.graph import AdjacencyListWeightedGraph
from dsa.heap import PriorityQueue
    
def prims_mst(graph, start: str, mst_graph=None) -> AdjacencyListWeightedGraph:
    """
    Returns an MST given a graph and starting vertex.

    Args:
        graph: The graph to search an MST from. (can be either an AdjacencyListWeightedGraph or AdjacencyMatrixWeightedGraph)
        start (string): The starting vertex label.
        mst_graph: an empty graph object to output the MST in to 

    Returns:
        AdjacencyListWeightedGraph: the MST of the graph.
    """
    def add_adjacent(graph, pq: PriorityQueue, visited: set, node: str):
        """Add all outgoing edges from the given node to the priority queue."""
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                pq.push(weight, (node, neighbor))  # Push edge with weight as priority

    # update this so that it will return the appropriate graph type
    if mst_graph is None:
        mst_graph = AdjacencyListWeightedGraph()

    visited = set()
    pq = PriorityQueue()

    add_adjacent(graph, pq, visited, start)
    vertices_set = set(graph.vertices())

    while not pq.is_empty() and visited != vertices_set:
        weight, edge = pq.pop_pair()
        u, v = edge
        if v not in visited:
            mst_graph.add_edge(u, v, graph[u][v])
            add_adjacent(graph, pq, visited, v)
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