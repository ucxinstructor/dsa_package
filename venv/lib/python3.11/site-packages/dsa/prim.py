""" Module to access functions for Prim's Algorithm. """
from dsa.graph import AdjacencyListWeightedGraph
from dsa.heap import PriorityQueue
    
def prims_mst(graph, start: str, mst_graph=None) -> AdjacencyListWeightedGraph:
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
                pq.push(weight, (node, adjacent))  # Push edge with weight as priority

    # todo: update this so that it will return the appropriate graph type
    if mst_graph is None:
        mst_graph = AdjacencyListWeightedGraph()

    visited = set()
    pq = PriorityQueue()
    total_vertices = len(set(graph.vertices()))

    add_adjacent(graph, pq, visited, start)

    # While the priority queue is not empty and we haven't visited all vertices
    while not pq.is_empty() and len(visited) < total_vertices:
        weight, edge = pq.pop_pair()
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