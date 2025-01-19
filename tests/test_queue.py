import unittest
from dsa.queue import Queue, DynamicQueue

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
        print(q)

        dq = DynamicQueue()
        for _ in range(20):
            dq.enqueue(_ * 2)
        self.assertEqual(dq.count, 20)
        self.assertEqual(dq.peek(), 0)
        self.assertGreater(dq.capacity(), 10)
        try:
            dq.enqueue(20)
        except Exception:
            self.fail("enqueue raised Exception unexpectedly")
        print(dq)

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
        self.assertEqual(q1.to_list(), q2.to_list())

        q1 = Queue(capacity=5)
        for n in [1, 2, 3, 4, 5]:
            q1.enqueue(n)
        q1.dequeue()
        q1.dequeue()
        q1.enqueue(6)
        q1.enqueue(7)
        self.assertEqual(q1.to_list(), [3, 4, 5, 6, 7])

        dq = DynamicQueue(capacity=5)
        for n in [1, 2, 3, 4, 5]:
            dq.enqueue(n)
        dq.dequeue()
        dq.dequeue()
        dq.enqueue(6)
        dq.enqueue(7)
        self.assertEqual(dq.to_list(), [3, 4, 5, 6, 7])

    def test_to_list(self):
        q = Queue()
        self.assertEqual(q.to_list(), [])

        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            q.enqueue(elem)
        self.assertEqual(q.to_list(), elements)

        q.dequeue()
        self.assertEqual(q.to_list(), elements[1:])

        q.enqueue(6)
        self.assertEqual(q.to_list(), elements[1:] + [6])

        dq = DynamicQueue()
        self.assertEqual(dq.to_list(), [])

        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for elem in elements:
            dq.enqueue(elem)
        self.assertEqual(dq.to_list(), elements)

        dq.dequeue()
        self.assertEqual(dq.to_list(), elements[1:])

        dq.enqueue(13)
        self.assertEqual(dq.to_list(), elements[1:] + [13])


if __name__ == '__main__':
    unittest.main()
