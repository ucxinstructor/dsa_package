import unittest
from dsa.queue import CircularQueue 

class TestQueue(unittest.TestCase):
    def test_create(self):
        q = CircularQueue()
        self.assertEqual(q.count, 0)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.capacity(), 10)

        q = CircularQueue([1, 2, 3, 4, 5])
        self.assertEqual(q.count, 5)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.capacity(), 10)

        q = CircularQueue([1, 2, 3, 4, 5], capacity=5)
        self.assertEqual(q.count, 5)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.capacity(), 5)

    def test_enqueue(self):
        q = CircularQueue()
        for _ in range(10):
            q.enqueue(_ * 2)
        self.assertEqual(q.count, 10)
        self.assertEqual(q.peek(), 0)
        self.assertEqual(q.capacity(), 10)

    def test_dequeue(self):
        q = CircularQueue()
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

    def test_peek(self):
       q = CircularQueue()
       self.assertRaises(Exception, lambda x: q.peek)
       for _ in range(10):
           q.enqueue(_ * 2)
       self.assertEqual(q.peek(), 0)
    
    def test_is_empty(self):
        q = CircularQueue()
        self.assertTrue(q.is_empty())
        for _ in range(10):
            q.enqueue(_ * 2)
        self.assertFalse(q.is_empty())

    def test_capacity(self):
        q = CircularQueue()
        self.assertEqual(q.capacity(), 10)
        for _ in range(10):
            q.enqueue(_ * 2)
        self.assertEqual(q.capacity(), 10)

    def test_circularity(self):
        q = CircularQueue(capacity=5)
        for _ in range(6):
            q.enqueue(_ * 2)

        # problem in dequeue
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 4)

        q.enqueue(100)
        q.enqueue(110)
        self.assertEqual(q.to_list(), [10, 100, 110, 6, 8])

        q = CircularQueue([10, 20, 30], capacity=3)
        q.enqueue(40)
        q.enqueue(50)
        self.assertEqual(q.to_list(), [40, 50, 30])

        q = CircularQueue([10, 20, 30], capacity=3)
        q.enqueue(40)
        self.assertEqual(q.dequeue(), 20)
        self.assertEqual(q.dequeue(), 30)
        q.enqueue(50)
        self.assertEqual(q.to_list(), [40, 50])
        
if __name__ == '__main__':
    unittest.main()
