import unittest

from dsa.tree import Tree, TreeNode

class TestTree(unittest.TestCase):
    def test_create(self):
        n = TreeNode(1)
        n.left = TreeNode(2)
        n.right = TreeNode(3)
        n.left.left = TreeNode(4)
        t = Tree(n)
        self.assertEqual(t.root.left.left.value, 4)
        self.assertEqual(t.root.left.right, None)
        self.assertEqual(repr(t.root), "1")
        self.assertEqual(repr(t.root.right), "3")

    def test_insert(self):
        t = Tree()

        t.insert(20)
        t.insert(30)
        t.insert(10)
        t.insert(5)
        t.insert(40)
        t.insert(2)
        t.insert(35)
        t.insert(7)

        t.print()

        self.assertIsNotNone(t.search(20))
        self.assertIsNotNone(t.search(7))
        self.assertIsNotNone(t.search(5))
        self.assertIsNotNone(t.search(40))

        self.assertIsNone(t.search(0))
        self.assertIsNone(t.search(60))
        self.assertIsNone(t.search(-1))

        t.delete(20)
        self.assertIsNone(t.search(20))
        t.delete(20)
        self.assertIsNone(t.search(20))
