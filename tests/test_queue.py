import unittest
from dsa.queue import Queue, DynamicQueue, CircularQueue

class TestQueue(unittest.TestCase):
    def test_create(self):
        q = Queue()
        self.assertEqual(q.count, 0)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.capacity(), 10)

        dq = DynamicQueue()
        self.assertEqual(dq.count, 0)
        self.assertTrue(dq.is_empty())
        self.assertEqual(dq.capacity(), 10)

    def test_insert(self):
        q = Queue()
        for _ in range(10):
            q.enqueue(_ * 2)
        self.assertEqual(q.count, 10)
        self.assertEqual(q.peek(), 0)
        self.assertRaises(Exception, q.enqueue, 10)
        self.assertEqual(q.capacity(), 10)

        dq = DynamicQueue()
        for _ in range(20):
            dq.enqueue(_ * 2)
        self.assertEqual(dq.count, 20)
        self.assertEqual(dq.peek(), 0)
        self.assertGreater(dq.capacity(), 10)
        dq.enqueue(20)
        self.assertGreater(dq.capacity(), 10)

    def test_delete(self):
        q = Queue()
        self.assertRaises(Exception, q.dequeue)
        for _ in range(10):
            q.enqueue(_ * 2)

        for _ in range(10):
            p = q.peek()
            v = q.dequeue()
            self.assertEqual(p, v)
            self.assertEqual(_ * 2, v)
        self.assertEqual(q.count, 0)
        self.assertRaises(Exception, q.dequeue)

        dq = DynamicQueue()
        self.assertRaises(Exception, dq.dequeue)
        for _ in range(20):
            dq.enqueue(_ * 2)

        for _ in range(20):
            p = dq.peek()
            v = dq.dequeue()
            self.assertEqual(p, v)
            self.assertEqual(_ * 2, v)
        self.assertEqual(dq.count, 0)
        self.assertRaises(Exception, dq.dequeue)
        
    def test_lists(self):
        test_list = [0, 2, 4, 6, 8]
        q1 = Queue.from_list(test_list)
        self.assertTrue(test_list)
        q2 = Queue()
        for n in [0, 2, 4, 6, 8]:
            q2.enqueue(n)
        self.assertEqual(q1.to_ordered_list(), q2.to_ordered_list())

        q1 = Queue(capacity=5)
        for n in [1, 2, 3, 4, 5]:
            q1.enqueue(n)
        q1.dequeue()
        q1.dequeue()
        q1.enqueue(6)
        q1.enqueue(7)
        self.assertEqual(q1.to_ordered_list(), [3, 4, 5, 6, 7])

        dq = DynamicQueue(capacity=5)
        for n in [1, 2, 3, 4, 5]:
            dq.enqueue(n)
        dq.dequeue()
        dq.dequeue()
        dq.enqueue(6)
        dq.enqueue(7)
        self.assertEqual(dq.to_ordered_list(), [3, 4, 5, 6, 7])

    def test_to_list(self):
        q = Queue()
        self.assertEqual(q.to_ordered_list(), [])

        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            q.enqueue(elem)
        self.assertEqual(q.to_ordered_list(), elements)

        q.dequeue()
        self.assertEqual(q.to_ordered_list(), elements[1:])

        q.enqueue(6)
        self.assertEqual(q.to_ordered_list(), elements[1:] + [6])

        dq = DynamicQueue()
        self.assertEqual(dq.to_ordered_list(), [])

        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for elem in elements:
            dq.enqueue(elem)
        self.assertEqual(dq.to_ordered_list(), elements)

        dq.dequeue()
        self.assertEqual(dq.to_ordered_list(), elements[1:])

        dq.enqueue(13)
        self.assertEqual(dq.to_ordered_list(), elements[1:] + [13])

    def test_eq(self):
        q1 = Queue.from_list([1, 2, 3, 4])
        q2 = Queue.from_list([1, 2, 3, 4])
        q3 = Queue.from_list([1, 2, 3])
        self.assertEqual(q1, q2)
        self.assertNotEqual(q1, q3)

        dq1 = DynamicQueue.from_list([5, 6, 7])
        dq2 = DynamicQueue.from_list([5, 6, 7])
        dq3 = DynamicQueue.from_list([5, 6])
        self.assertEqual(dq1, dq2)
        self.assertNotEqual(dq1, dq3)

        self.assertEqual(q1, DynamicQueue.from_list([1, 2, 3, 4]))
        self.assertEqual(dq1, Queue.from_list([5, 6, 7]))

        cq1 = CircularQueue([1, 2, 3, 4])
        self.assertEqual(q1, cq1)
        self.assertEqual(cq1, q1)
        self.assertEqual(DynamicQueue.from_list([1, 2, 3, 4]), cq1)
        self.assertEqual(cq1, DynamicQueue.from_list([1, 2, 3, 4]))

        self.assertNotEqual(q1, [1, 2, 3, 4])

        q4 = Queue()
        dq4 = DynamicQueue()
        cq4 = CircularQueue()
        self.assertEqual(q4, dq4)
        for q in [q1, q2, q3]:
            self.assertNotEqual(q, q4)
            self.assertNotEqual(q, dq4)
            self.assertNotEqual(q, cq4)

            self.assertNotEqual(q4, q)
            self.assertNotEqual(dq4, q)
            self.assertNotEqual(cq4, q)

        for dq in [dq1, dq2, dq3]:
            self.assertNotEqual(dq, q4)
            self.assertNotEqual(dq, dq4)
            self.assertNotEqual(dq, cq4)

            self.assertNotEqual(q4, dq)
            self.assertNotEqual(dq4, dq)
            self.assertNotEqual(cq4, dq)


if __name__ == '__main__':
    unittest.main()
