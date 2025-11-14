""" Module to access functions for Dijkstra's Algorithm. """
from dsa.heap import MinHeap
from dsa.graph import AdjacencyListWeightedGraph

def shortest_path(graph: AdjacencyListWeightedGraph, start: str, end: str, debug: bool=False) -> tuple:
    """ 
    Helper function that returns a weight table and a predecessor table using Dijkstra's Algorithm.

    Args:
        graph (AdjacencyListWeighted Graph): The graph to search.
        start (str): The starting vertex label.
        end (str): The ending vertex label.
        debug (bool): If True, display weight table as it is being built.
    
    Raises:
        KeyError: If start or end vertex is not in the graph.
        
    Returns:
        A tuple of a weight table hashtable and a predecessor predecessorhashtable.
    """
    if start not in graph:
        raise KeyError(f"Start vertex {start} not in graph.")
    if end not in graph:
        raise KeyError(f"End vertex {end} not in graph.")

    weight_table = {start: 0}
    predecessor = {start: start}
    visited = set()
    pq = MinHeap()

    pq.insert((0, start))
    
    while not pq.is_empty():
        current_weight, current = pq.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            break

        for adjacent, weight in graph[current].items():
            new_dist = current_weight + weight
            if new_dist < weight_table.get(adjacent, float('inf')):
                weight_table[adjacent] = new_dist
                predecessor[adjacent] = current
                pq.insert((new_dist, adjacent))
                if debug:
                    print(weight_table)
    
    return weight_table, predecessor

def find_path1(graph: AdjacencyListWeightedGraph, start: str, end: str, debug: bool=False) -> list:
    """ 
    Return the shortest path of two vertices using Dijkstra's Algorithm.

    Args:
        graph (AdjacencyListWeighted Graph): The graph to search.
        start (str): The starting vertex label.
        end (str): The ending vertex label.
        debug (bool): If True, display the weight table.

    Returns:
        A list of vertices that form a shortest path.
    """
    weight_table, predecessor = shortest_path(graph, start, end, debug)
    path = []

    current = end
    path.append(current)
    while current != start:
        current = predecessor[current]
        path.append(current)
        
    path.reverse()

    if debug:
        print("predecessor table")
        print(predecessor)

        print("weight table")
        print(weight_table)
        print("shortest path weight ", weight_table[end])
    return path


def find_path(graph: AdjacencyListWeightedGraph, start: str, end: str, debug: bool=False) -> list:
    """ 
    Return the shortest path of two vertices using Dijkstra's Algorithm.

    Args:
        graph (AdjacencyListWeighted Graph): The graph to search.
        start (str): The starting vertex label.
        end (str): The ending vertex label.
        debug (bool): If True, display the weight table.
    
    Raises:
        KeyError: If there is no path from start to end.

    Returns:
        A list of vertices that form a shortest path.
    """
    weight_table, predecessor = shortest_path(graph, start, end, debug)

    # No path or invalid start/end
    if end not in predecessor:
        raise KeyError(f"No path from {start} to {end}.")

    path = []
    current = end
    path.append(current)

    while current != start:
        current = predecessor[current]
        path.append(current)

    path.reverse()

    if debug:
        print("predecessor table")
        print(predecessor)
        print("weight table")
        print(weight_table)
        print("shortest path weight", weight_table[end])

    return path