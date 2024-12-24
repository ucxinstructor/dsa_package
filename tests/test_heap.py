import unittest

from dsa.heap import Heap, MinHeap, PriorityQueue
from dsa.tree import TreeNode

class TestHeap(unittest.TestCase):
    def test_create(self):
        mxh = Heap()
        mnh = MinHeap()
        self.assertEqual(mxh.count(), 0)
        self.assertEqual(mnh.count(), 0)
    
    def test_list(self):
        arr = [10, 20, 15, 25, 17, 5]
        h = Heap.from_list(arr)
        self.assertEqual(h.count(), len(arr))
        h = Heap.from_list([10, 20])
        self.assertEqual(h.to_list(), [20, 10])

        h = MinHeap.from_list(arr)
        self.assertEqual(h.count(), len(arr))
        h = MinHeap.from_list([10, 20])
        self.assertEqual(h.to_list(), [10, 20])

    def test_add(self):
        mxh = Heap()
        mnh = MinHeap()

        for _ in range(20):
            mxh.insert(_)
            mnh.insert(_)

        self.assertEqual(mxh.count(), 20)
        self.assertEqual(mxh.peek(), 19)
        self.assertEqual(mnh.count(), 20)
        self.assertEqual(mnh.peek(), 0)

    def test_delete(self):
        mxh = Heap()
        mnh = MinHeap()

        for _ in range(20):
            mxh.insert(_)
            mnh.insert(_)

        i = 19
        while not mxh.is_empty():
            v = mxh.pop()
            self.assertEqual(v, i)
            i = i - 1
        self.assertTrue(mxh.is_empty())

        i = 0
        while not mnh.is_empty():
            v = mnh.pop()
            self.assertEqual(v, i)
            i += 1
        self.assertTrue(mnh.is_empty())

    def test_pq(self):
        pq = PriorityQueue()
        pq.push(2, "a")
        pq.push(1, "b")
        pq.push(3, "c")
        pq.push(4, "d")
        pq.push(5, "e")

        self.assertEqual(pq.peek(), "b")
        self.assertEqual(pq.peek_pair(), (1, "b"))
        self.assertEqual(len(pq), 5)
        self.assertEqual(pq.count(), 5)

        print(pq)
        while not pq.is_empty():
            v1 = pq.peek()
            v2 = pq.pop()
            self.assertEqual(v1, v2)

    def test_pq_pair(self):
        pq = PriorityQueue()
        pq.push(2, "a")
        pq.push(1, "b")
        pq.push(3, "c")
        pq.push(4, "d")
        pq.push(5, "e")

        while not pq.is_empty():
            v1 = pq.peek_pair()
            v2 = pq.pop_pair()
            print(pq)
            self.assertEqual(v1, v2)

    def test_pq_misc_types(self):
        pq = PriorityQueue()
        pq.push(3, TreeNode("a"))
        pq.push(2, TreeNode(" "))
        pq.push(1, TreeNode("m"))
        pq.push(0, TreeNode("n"))
        pq.push(4, TreeNode("p"))