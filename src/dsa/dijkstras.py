""" Module to access functions for Dijkstra's Algorithm. """
from dsa.heap import MinHeap
from dsa.graph import AdjacencyListWeightedGraph

def shortest_path(graph: AdjacencyListWeightedGraph, start: str, end: str, debug: bool=False) -> tuple:
    """ 
    Helper function that returns a weight table and a previous vertex table using Dijkstra's Algorithm.

    Args:
        graph (AdjacencyListWeighted Graph): The graph to search.
        start (str): The starting vertex label.
        end (str): The ending vertex label.
        debug (bool): If True, display weight table as it is being built.
    
    Returns:
        A tuple of a weight table dictionary and a previous path dictionary.
    """
    weight_table = {}
    previous = {}
    visited = set()
    h = MinHeap()

    current = start
    h.insert(current)
    weight_table[current] = 0
    previous[current] = current
    
    while not h.is_empty():
        current_weight = weight_table.get(current, float('inf'))
        visited.add(current)

        for adjacent in graph[current]:
            weight = graph[current][adjacent]
            if adjacent not in visited:
                h.insert(adjacent)

            wt = weight_table.get(adjacent, float('inf'))
            if wt > weight + current_weight:
                weight_table[adjacent] = weight + current_weight
                previous[adjacent] = current
                if debug:
                    print(weight_table)

        current = h.pop()

    return weight_table, previous

def find_path(graph: AdjacencyListWeightedGraph, start: str, end: str, debug: bool=False) -> list:
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
    weight_table, previous = shortest_path(graph, start, end, debug)
    path = []

    current = end
    path.append(current)
    while current != start:
        current = previous[current]
        path.append(current)
        
    path.reverse()

    if debug:
        print("previous table")
        print(previous)

        print("weight table")
        print(weight_table)
        print("price ", weight_table[end])
    return path
