import unittest

from dsa.graph import Vertex, WeightedVertex

class TestAdjacencyList(unittest.TestCase):
    def test_create_undirected(self):
        a = Vertex("A")
        b = Vertex("B")
        c = Vertex("C")

        a.add_edge(b)
        a.add_edge(c)

    def test_create_directed(self):
        a = Vertex("A")
        b = Vertex("B")
        c = Vertex("C")

        a.add_directed_edge(b)
        a.add_directed_edge(c)

    def test_create_undirected_weighted(self):
        a = WeightedVertex("A")
        b = WeightedVertex("B")
        c = WeightedVertex("C")

        a.add_edge(b, 10)
        a.add_edge(c, 15)



    def test_create_directed_weighted(self):
        a = WeightedVertex("A")
        b = WeightedVertex("B")
        c = WeightedVertex("C")

        a.add_directed_edge(b, 10)
        a.add_directed_edge(c, 15)
