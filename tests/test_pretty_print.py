import unittest

from dsa.tree import Tree
from dsa.heap import Heap
from dsa.pretty_print import heap_print, tree_print

class TestPrettyPrint(unittest.TestCase):
    def test_tree(self):
        t = Tree()
        tree_print(t)

    def test_tree2(self):
        t = Tree()
        t.insert(20)
        tree_print(t)
        t.insert(30)
        tree_print(t)
        t.insert(10)
        t.insert(5)
        tree_print(t)

        t.insert(40)
        t.insert(2)
        t.insert(35)
        t.insert(7)
        tree_print(t)


    def test_heap(self):
        h = Heap()
        heap_print(h)

        h.insert(10)
        heap_print(h)

        h.insert(20)
        heap_print(h)

        h.insert(5)
        heap_print(h)

        h.insert(35)
        heap_print(h)
