""" Module to access functions for Dijkstra's Algorithm. """
from dsa.heap import PriorityQueue
from dsa.graph import Graph

def dijkstra_tables(graph: Graph, start: str, end: str, debug: bool = False) -> tuple:
    """ 
    Helper function that returns a weight table and a predecessor table using Dijkstra's Algorithm.

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
    if end not in graph:
        raise KeyError(f"End vertex {end} not in graph.")

    dist_table = {}
    pred_table = {}
    finished = set()
    pq = PriorityQueue()

    for v in graph.vertices():
        dist_table[v] = float('inf')
        pred_table[v] = None

    dist_table[start] = 0

    # insert starting vertex with weight 0
    pq.insert(0, start)
    
    while not pq.is_empty():
        current_dist, current_vertex = pq.extract_min_pair()
        if current_vertex in finished:
            continue
        finished.add(current_vertex)

        # early break
        if current_vertex == end:
            break

        for neighbor in graph.adjacents(current_vertex):
            weight = graph.weight(current_vertex, neighbor)
            new_dist = current_dist + weight
            if debug:
                print("current_vertex ", current_vertex, " adjacent ", neighbor, " weight ", weight, " new_dist ", new_dist, " predecessor ", pred_table)
            if new_dist < dist_table[neighbor]:
                dist_table[neighbor] = new_dist
                pred_table[neighbor] = current_vertex
                pq.insert(new_dist, neighbor)
                if debug:
                    print(dist_table)
    
    return dist_table, pred_table

def find_path(graph: Graph, start: str, end: str, debug: bool = False) -> list:
    """ 
    Return the shortest path of two vertices using Dijkstra's Algorithm.

    Args:
        graph (Graph): The graph to search.
        start (str): The starting vertex label.
        end (str): The ending vertex label.
        debug (bool): If True, display the weight table.
    
    Raises:
        KeyError: If start or end vertex is not in the graph, or if there is no path from start to end.

    Returns:
        A list of vertices that form a shortest path.
    """
    dist_table, pred_table = dijkstra_tables(graph, start, end, debug = False)

    # No path or invalid start/end
    if end not in pred_table:
        raise KeyError(f"No path from {start} to {end}.")

    path = []
    current = end
    path.append(current)

    while current != start:
        current = pred_table[current]
        path.append(current)

    path.reverse()

    if debug:
        print(f"Predecessor: {pred_table}")
        print(f"Weight table: {dist_table}")
        print(f"Shortest path weight: {dist_table[end]}")

    return path