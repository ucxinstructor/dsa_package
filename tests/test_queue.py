import unittest
from dsa.queue import Queue, DynamicQueue

class TestQueue(unittest.TestCase):
    def test_create(self):
        q = Queue()
        self.assertEqual(q.count, 0)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.capacity(), 10)
#        self.assertEqual(q.front, 0)

        dq = DynamicQueue()
        self.assertEqual(dq.count, 0)
        self.assertTrue(dq.is_empty())
        self.assertEqual(dq.capacity(), 10)
 #       self.assertEqual(dq.front, 0)

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
if __name__ == '__main__':
    unittest.main()
