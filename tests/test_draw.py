import unittest

from dsa.draw import TreeDraw, HeapDraw, TrieDraw, GraphDraw
from dsa.trie import Trie
from dsa.tree import Tree, TreeNode
from dsa.heap import Heap, MinHeap
from dsa.graph import AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph
from dsa.pretty_print import heap_print, tree_print

import os
import shutil

class TestDraw(unittest.TestCase):
    def setUp(self) -> None:
        # create the images folder if it does not exist
        if not os.path.exists('images'):
            os.makedirs('images')
        else:
            self.cleanup()

    def delete_files_in_folder(self, folder_path):
        # Check if the folder exists
        if not os.path.exists(folder_path):
            self.fail(f"The folder {folder_path} does not exist.")
            return

        # Iterate over all the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory and its contents
            except Exception as e:
                self.fail(f"Failed to delete {file_path}. Reason: {e}")
                return

    def cleanup(self):
        self.delete_files_in_folder('images')
        
    def test_tree(self):
        n = TreeNode(40)
        n.left = TreeNode(20)
        n.left.left = TreeNode(10)
        n.left.right = TreeNode(30)

        n.right = TreeNode(60)
        n.right.left = TreeNode(50)
        n.right.right = TreeNode(70)

        t = Tree(n)
        tree_print(t)

        td = TreeDraw(t)
        td.set_figsize((5, 3))
        td.save('images/tree1.png')
        tree_print(td.tree)
        td.tree.print()

        n = TreeNode(40)
        n.left = TreeNode(20)
        n.left.left = TreeNode(10)
        n.left.left.left = TreeNode(5)
        t = Tree(n)
        td = TreeDraw(t)
        td.set_figsize((10, 8))
        td.save('images/tree2.png')


        n = TreeNode(40)
        n.right = TreeNode(50)
        n.right.right = TreeNode(60)
        n.right.right.right = TreeNode(65)
        t = Tree(n)
        td = TreeDraw(t)
        td.set_figsize((12, 6))
        td.save('images/tree3.png')

    def test_heap(self):
        h = Heap()
        h.insert(10)
        h.insert(20)
        h.insert(30)
        h.insert(40)
        h.insert(50)
        h.insert(60)
        h.insert(70)
        h.insert(80)
        h.insert(100)
        heap_print(h)

        hd = HeapDraw(h)
        hd.set_figsize((12, 6))
        hd.save('images/heap1.png')

        h = MinHeap()
        h.insert(10)
        h.insert(20)
        h.insert(30)
        h.insert(40)
        h.insert(50)
        h.insert(60)
        h.insert(70)
        h.insert(80)
        h.insert(100)
        heap_print(h)

        hd = HeapDraw(h)
        hd.set_figsize((8, 4))
        hd.save('images/heap2.png')

    def test_trie(self):
        t = Trie()
        words = ["cat", "car", "cart", "dog", "dot", "doggie", "smart"]
        for word in words:
            t.insert(word.upper())

        td = TrieDraw(t)
        td.set_figsize((12, 4))
        td.save('images/trie.png')

    def test_graph(self):
        graph = AdjacencyMatrixGraph(["A", "B", "C", "D"])
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")
        graph.add_edge("D", "A")

        gd = GraphDraw(graph)
        gd.set_figsize((12, 10))
        gd.save('images/graph1.png')
        gd.set_figsize((12, 6))
        gd.save('images/graph1.1.png')

        graph = AdjacencyMatrixGraph(["A", "B", "C", "D"])
        graph.add_edge("A", "B", directed=True)
        graph.add_edge("A", "C", directed=True)
        graph.add_edge("B", "C", directed=True)
        graph.add_edge("C", "D", directed=True)
        graph.add_edge("D", "A", directed=True)

        gd = GraphDraw(graph, directed=True)
        gd.set_figsize((8, 4))
        gd.save('images/graph2.png')

        graph = AdjacencyMatrixWeightedGraph(["A", "B", "C", "D"])
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 2)
        graph.add_edge("B", "C", 3)
        graph.add_edge("C", "D", 4)
        graph.add_edge("D", "A", 5)

        gd = GraphDraw(graph, directed=False, weighted=True)
        gd.set_figsize((6, 3))
        gd.save('images/graph3.png')

        #weighted #adjacency list
        graph = AdjacencyMatrixWeightedGraph(["A", "B", "C", "D"])
        graph.add_edge("A", "B", 1, directed=True)
        graph.add_edge("A", "C", 2, directed=True)
        graph.add_edge("B", "C", 3, directed=True)
        graph.add_edge("C", "D", 4, directed=True)
        graph.add_edge("D", "A", 5, directed=True)

        gd = GraphDraw(graph, directed=True, weighted=True)
        gd.set_figsize((5, 5))
        gd.save('images/graph4.png')




