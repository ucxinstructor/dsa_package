import unittest

from dsa.graph import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph

class TestGraph(unittest.TestCase):
    def test_create_undirected(self):
        g = AdjacencyMatrixGraph(["A", "B", "C"])
        g.add_adjacent_vertex("A", "B")
        g.add_adjacent_vertex("A", "C")

        g.print_graph()

    def test_create_directed(self):
        g = AdjacencyMatrixGraph(["A", "B", "C"])
        g.add_adjacent_directed_vertex("A", "B")
        g.add_adjacent_directed_vertex("A", "C")

        g.print_graph()

    def test_create_weighted_directed(self):
        g = AdjacencyMatrixWeightedGraph(["A", "B", "C"])
        g.add_adjacent_directed_vertex("A", "B", 10)
        g.add_adjacent_directed_vertex("A", "C", 15)

        g.print_graph()
