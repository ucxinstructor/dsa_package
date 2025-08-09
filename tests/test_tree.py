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

        with self.assertRaises(ValueError):
            t.search(0)
        with self.assertRaises(ValueError):
            t.search(60)
        with self.assertRaises(ValueError):
            t.search(-1)

    def test_delete(self):
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

        t.delete(20)
        with self.assertRaises(ValueError):
            t.search(20)

        with self.assertRaises(ValueError):
            t.delete(20)

        t.delete(7)
        t.delete(35)
        t.delete(5)

        # additional checks after deletions
        self.assertIsNotNone(t.search(30))
        self.assertIsNotNone(t.search(10))
        self.assertIsNotNone(t.search(40))
        with self.assertRaises(ValueError):
            t.search(7)
        t.print()
        t.delete(10)
        with self.assertRaises(ValueError):
            t.search(10)
        t.delete(30)

    def test_eq(self):
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.right = TreeNode(3)
        t1 = Tree(n1)

        n2 = TreeNode(1)
        n2.left = TreeNode(2)
        n2.right = TreeNode(3)
        t2 = Tree(n2)

        n3 = TreeNode(1)
        n3.left = TreeNode(2)
        t3 = Tree(n3)

        self.assertEqual(t1, t2)
        self.assertNotEqual(t1, t3)

        self.assertNotEqual(t1, [1, 2, 3])