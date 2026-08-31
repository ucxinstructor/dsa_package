import unittest

from dsa.heap import Heap, MaxHeap, MinHeap, PriorityQueue
from dsa.tree import TreeNode

class TestHeap(unittest.TestCase):
    def test_create(self):
        mxh = MaxHeap()
        mnh = MinHeap()
        self.assertEqual(mxh.count(), 0)
        self.assertEqual(mnh.count(), 0)
    
    def test_list(self):
        arr = [10, 20, 15, 25, 17, 5]
        h = Heap.from_list(arr)
        self.assertEqual(h.count(), len(arr))
        h = Heap.from_list([10, 20])
        self.assertEqual(h.raw_view(), [20, 10])
        self.assertEqual(h.to_sorted_list(), [20, 10])

        h = MinHeap.from_list(arr)
        self.assertEqual(h.count(), len(arr))
        h = MinHeap.from_list([10, 20])
        self.assertEqual(h.raw_view(), [10, 20])
        self.assertEqual(h.to_sorted_list(), [10, 20])

    def test_add(self):
        mxh = MaxHeap()
        mnh = MinHeap()

        for _ in range(20):
            mxh.insert(_)
            mnh.insert(_)

        self.assertEqual(mxh.count(), 20)
        self.assertEqual(mxh.peek(), 19)
        self.assertEqual(mnh.count(), 20)
        self.assertEqual(mnh.peek(), 0)

    def test_delete(self):
        mxh = MaxHeap()
        mnh = MinHeap()

        for _ in range(20):
            mxh.insert(_)
            mnh.insert(_)

        i = 19
        while not mxh.is_empty():
            v = mxh.extract_max()
            self.assertEqual(v, i)
            i = i - 1
        self.assertTrue(mxh.is_empty())

        i = 0
        while not mnh.is_empty():
            v = mnh.extract_min()
            self.assertEqual(v, i)
            i += 1
        self.assertTrue(mnh.is_empty())
        
    def test_peek(self):
        mxh = Heap()
        mnh = MinHeap()

        for _ in range(20):
            mxh.insert(_)
            mnh.insert(_)

        self.assertEqual(mxh.peek(), 19)
        self.assertEqual(mnh.peek(), 0)
    
    def test_extract_max_min(self):
        mxh = Heap()
        mnh = MinHeap()

        for _ in range(20):
            mxh.insert(_)
            mnh.insert(_)

        i = 19
        while not mxh.is_empty():
            v = mxh.extract_max()
            self.assertEqual(v, i)
            i = i - 1
        self.assertTrue(mxh.is_empty())

        i = 0
        while not mnh.is_empty():
            v = mnh.extract_min()
            self.assertEqual(v, i)
            i += 1
        self.assertTrue(mnh.is_empty())

    def test_pq(self):
        pq = PriorityQueue()
        pq.enqueue(2, "a")
        pq.enqueue(1, "b")
        pq.enqueue(3, "c")
        pq.enqueue(4, "d")
        pq.enqueue(5, "e")

        self.assertEqual(pq.peek(), "b")
        self.assertEqual(pq.peek_pair(), (1, "b"))
        self.assertEqual(len(pq), 5)
        self.assertEqual(pq.count(), 5)

        while not pq.is_empty():
            v1 = pq.peek()
            v2 = pq.dequeue()
            self.assertEqual(v1, v2)

    def test_pq_pair(self):
        pq = PriorityQueue()
        pq.enqueue(2, "a")
        pq.enqueue(1, "b")
        pq.enqueue(3, "c")
        pq.enqueue(4, "d")
        pq.enqueue(5, "e")

        while not pq.is_empty():
            v1 = pq.peek()
            v2 = pq.dequeue()
            self.assertEqual(v1, v2)

    def test_pq_misc_types(self):
        pq = PriorityQueue()
        pq.enqueue(3, TreeNode("a"))
        pq.enqueue(2, TreeNode(" "))
        pq.enqueue(1, TreeNode("m"))
        pq.enqueue(0, TreeNode("n"))
        pq.enqueue(4, TreeNode("p"))

    def test_eq(self):
        h1 = Heap.from_list([5, 3, 8, 1])
        h2 = Heap.from_list([5, 3, 8, 1])
        h3 = Heap.from_list([1, 2, 3])
        self.assertEqual(h1, h2)
        self.assertNotEqual(h1, h3)

        m1 = MinHeap.from_list([5, 3, 8, 1])
        m2 = MinHeap.from_list([5, 3, 8, 1])
        m3 = MinHeap.from_list([1, 2, 3])
        self.assertEqual(m1, m2)
        self.assertNotEqual(m1, m3)

        pq1 = PriorityQueue()
        pq2 = PriorityQueue()
        pq3 = PriorityQueue()
        for p, v in [(2, "a"), (1, "b"), (3, "c")]:
            pq1.enqueue(p, v)
            pq2.enqueue(p, v)
        for p, v in [(1, "x"), (2, "y")]:
            pq3.enqueue(p, v)
        self.assertEqual(pq1, pq2)
        self.assertNotEqual(pq1, pq3)

    def test_to_string_with_priority(self):
        pq = PriorityQueue()
        pq.enqueue(2, "a")
        pq.enqueue(1, "b")
        pq.enqueue(3, "c")
        pq.enqueue(4, "d")
        pq.enqueue(5, "e")

        expected_string = "[(1, 'b') (2, 'a') (3, 'c') (4, 'd') (5, 'e')]"
        self.assertEqual(pq.to_string_with_priority(), expected_string)