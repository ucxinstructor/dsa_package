import unittest
from dsa.deque import Deque, DynamicDeque

class TestQueue(unittest.TestCase):
    def test_create(self):
        dq = Deque()
        self.assertEqual(dq.count, 0)
        self.assertEqual(len(dq), 0)
        self.assertTrue(dq.is_empty())
        self.assertEqual(dq.capacity(), 10)

        ddq = DynamicDeque()
        self.assertEqual(ddq.count, 0)
        self.assertTrue(ddq.is_empty())
        self.assertEqual(ddq.capacity(), 10)

    def test_insert(self):
        dq = Deque()
        for _ in range(10):
            dq.append_left(_ * 2)
        self.assertEqual(dq.count, 10)
        self.assertEqual(len(dq), 10)
        self.assertEqual(dq.peek_left(), 18)
        self.assertEqual(dq.peek_right(), 0)
        self.assertRaises(Exception, dq.append_left, 10)
        self.assertEqual(dq.capacity(), 10)

        dq2 = Deque()
        for _ in range(10):
            dq2.append_right(_ * 2)
        self.assertEqual(dq2.count, 10)
        self.assertEqual(len(dq2), 10)
        self.assertEqual(dq2.peek_left(), 0)
        self.assertEqual(dq2.peek_right(), 18)
        self.assertRaises(Exception, dq2.append_right, 10)
        self.assertEqual(dq2.capacity(), 10)

        ddq = DynamicDeque()
        for _ in range(10):
            ddq.append_left(_ * 2)
        self.assertEqual(ddq.count, 10)
        self.assertEqual(len(ddq), 10)

        self.assertEqual(ddq.peek_left(), 18)
        self.assertEqual(ddq.peek_right(), 0)
        self.assertEqual(ddq.capacity(), 10)
        for _ in range(20, 40, 2):
            ddq.append_left(_)
        self.assertEqual(ddq.count, 20)
        self.assertEqual(len(ddq), 20)
        self.assertEqual(ddq.peek_left(), 38)
        self.assertEqual(ddq.peek_right(), 0)
        self.assertEqual(ddq.capacity(), 20)

    def test_delete(self):
        dq = Deque()

        for _ in range(10):
            dq.append_left(_ * 2)

        for _ in range(10):
            p = dq.peek_left()
            v = dq.pop_left()
            self.assertEqual(p, v)
            if not dq.is_empty():
                self.assertEqual(dq.peek_right(), 0)

        for _ in range(10):
            dq.append_right(_ * 2)

        for _ in range(10):
            p = dq.peek_right()
            v = dq.pop_right()
            self.assertEqual(p, v)
            if not dq.is_empty():
                self.assertEqual(dq.peek_left(), 0)

        for _ in range(10):
            dq.append_left(_ * 2)

        for _ in range(10):
            p = dq.peek_right()
            v = dq.pop_right()
            self.assertEqual(p, v)
            if not dq.is_empty():
                self.assertEqual(dq.peek_left(), (10 - 1) * 2)

        for _ in range(10):
            dq.append_right(_ * 2)

        for _ in range(10):
            p = dq.peek_left()
            v = dq.pop_left()
            self.assertEqual(p, v)
            if not dq.is_empty():
                self.assertEqual(dq.peek_right(), (10 - 1) * 2)


        self.assertEqual(dq.count, 0)
        self.assertEqual(len(dq), 0)
        with self.assertRaises(Exception):
            dq.pop_left()
        with self.assertRaises(Exception):
            dq.pop_right()

    def test_dynamic_delete(self):
        ddq = DynamicDeque()

        max_range = 100
        for _ in range(max_range):
            ddq.append_left(_ * 2)

        for _ in range(max_range):
            p = ddq.peek_left()
            v = ddq.pop_left()
            if not ddq.is_empty():
                self.assertEqual(ddq.peek_right(), 0)
            self.assertEqual(p, v)

        for _ in range(max_range):
            ddq.append_right(_ * 2)

        for _ in range(max_range):
            p = ddq.peek_right()
            v = ddq.pop_right()
            if not ddq.is_empty():
                self.assertEqual(ddq.peek_left(), 0)

            self.assertEqual(p, v)

        for _ in range(max_range):
            ddq.append_left(_ * 2)

        for _ in range(max_range):
            p = ddq.peek_right()
            v = ddq.pop_right()
            if not ddq.is_empty():
                self.assertEqual(ddq.peek_left(), (max_range - 1) * 2)
            self.assertEqual(p, v)

        for _ in range(max_range):
            ddq.append_right(_ * 2)

        for _ in range(max_range):
            p = ddq.peek_left()
            v = ddq.pop_left()
            self.assertEqual(p, v)
            if not ddq.is_empty():
                self.assertEqual(ddq.peek_right(), (max_range - 1) * 2)

        self.assertEqual(ddq.count, 0)
        self.assertEqual(len(ddq), 0)
        with self.assertRaises(Exception):
            ddq.pop_left()
        with self.assertRaises(Exception):
            ddq.pop_right()

    def test_lists(self):
        test_list = [0, 2, 4, 6, 8]
        dq = Deque.from_list(test_list)
        self.assertTrue(dq)
        self.assertEqual(dq.count, len(test_list))

        dq2 = Deque()
        for n in [0, 2, 4, 6, 8]:
            dq2.append_right(n)

        self.assertEqual(dq.to_list(), dq2.to_list())

        test_list = range(50)
        ddq = DynamicDeque.from_list(test_list)
        self.assertTrue(ddq)
        self.assertEqual(ddq.count, len(test_list))

        ddq2 = DynamicDeque()
        for n in test_list:
            ddq2.append_right(n)

        self.assertEqual(ddq.to_list(), ddq2.to_list())

    def test_is_empty(self):
        dq = Deque()
        self.assertTrue(dq.is_empty())
        dq.append_left(1)
        self.assertFalse(dq.is_empty())
        ddq = DynamicDeque()
        self.assertTrue(ddq.is_empty())
        ddq.append_left(1)
        self.assertFalse(ddq.is_empty())

    def test_add_left(self):
        dq = Deque()
        dq.append_left(1)
        dq.append_left(2)
        self.assertEqual(dq.to_list(), [2, 1])
        ddq = DynamicDeque()
        ddq.append_left(1)
        ddq.append_left(2)
        self.assertEqual(ddq.to_list(), [2, 1])

    def test_add_right(self):
        dq = Deque()
        dq.append_right(1)
        dq.append_right(2)
        self.assertEqual(dq.to_list(), [1, 2])
        ddq = DynamicDeque()
        ddq.append_right(1)
        ddq.append_right(2)
        self.assertEqual(ddq.to_list(), [1, 2])

    def test_remove_left(self):
        dq = Deque()
        dq.append_left(1)
        dq.append_left(2)
        item = dq.pop_left()
        self.assertEqual(item, 2)
        self.assertEqual(dq.to_list(), [1])
        ddq = DynamicDeque()
        ddq.append_left(1)
        ddq.append_left(2)
        item = ddq.pop_left()
        self.assertEqual(item, 2)
        self.assertEqual(ddq.to_list(), [1])

    def test_remove_right(self):
        dq = Deque()
        dq.append_right(1)
        dq.append_right(2)
        item = dq.pop_right()
        self.assertEqual(item, 2)
        self.assertEqual(dq.to_list(), [1])
        ddq = DynamicDeque()
        ddq.append_right(1)
        ddq.append_right(2)
        item = ddq.pop_right()
        self.assertEqual(item, 2)
        self.assertEqual(ddq.to_list(), [1])

    def test_size(self):
        dq = Deque()
        self.assertEqual(len(dq), 0)
        dq.append_left(1)
        dq.append_right(2)
        self.assertEqual(len(dq), 2)

        ddq = DynamicDeque()
        self.assertEqual(len(ddq), 0)
        ddq.append_left(1)
        ddq.append_right(2)
        self.assertEqual(len(ddq), 2)


    def test_remove_front_empty(self):
        dq = Deque()
        with self.assertRaises(Exception):
            dq.pop_left()

        ddq = DynamicDeque()
        with self.assertRaises(Exception):
            ddq.pop_left()

    def test_remove_rear_empty(self):
        dq = Deque()
        with self.assertRaises(Exception):
            dq.pop_right()

        ddq = DynamicDeque()
        with self.assertRaises(Exception):
            ddq.pop_right()

    def test_static_deque_append_pop(self):
        dq = Deque(5)
        dq.append_right(1)
        dq.append_right(2)
        dq.append_left(0)
        self.assertEqual(dq.to_list(), [0, 1, 2])
        self.assertEqual(dq.pop_left(), 0)
        self.assertEqual(dq.pop_right(), 2)
        self.assertEqual(dq.to_list(), [1])

    def test_static_deque_overflow(self):
        dq = Deque(3)
        dq.append_right(1)
        dq.append_right(2)
        dq.append_right(3)
        with self.assertRaises(Exception) as context:
            dq.append_right(4)
        self.assertEqual(str(context.exception), "Deque Full")

    def test_static_deque_underflow(self):
        dq = Deque(3)
        with self.assertRaises(Exception) as context:
            dq.pop_left()
        self.assertEqual(str(context.exception), "Empty Deque")

    def test_static_deque_peek(self):
        dq = Deque(5)
        dq.append_right(10)
        dq.append_left(5)
        self.assertEqual(dq.peek_left(), 5)
        self.assertEqual(dq.peek_right(), 10)

    def test_static_deque_from_list(self):
        dq = Deque.from_list([1, 2, 3])
        self.assertEqual(dq.to_list(), [1, 2, 3])

class TestDynamicDeque(unittest.TestCase):
    def test_dynamic_deque_grow(self):
        dq = DynamicDeque(2)
        dq.append_right(1)
        dq.append_right(2)
        dq.append_right(3)  # Should trigger grow
        self.assertEqual(dq.capacity(), 4)
        self.assertEqual(dq.to_list(), [1, 2, 3])

    def test_dynamic_deque_shrink(self):
        dq = DynamicDeque(8)
        for i in range(6):
            dq.append_right(i)
        for _ in range(4):
            dq.pop_left()  # Should trigger shrink
        self.assertEqual(dq.capacity(), 8)
        self.assertEqual(dq.to_list(), [4, 5])

    def test_dynamic_deque_append_pop(self):
        dq = DynamicDeque()
        dq.append_left(10)
        dq.append_right(20)
        self.assertEqual(dq.pop_left(), 10)
        self.assertEqual(dq.pop_right(), 20)

    def test_dynamic_deque_underflow(self):
        dq = DynamicDeque()
        with self.assertRaises(Exception) as context:
            dq.pop_left()
        self.assertEqual(str(context.exception), "Empty Deque")

    def test_dynamic_deque_overflow_and_resize(self):
        dq = DynamicDeque(2)
        dq.append_right(1)
        dq.append_right(2)
        dq.append_right(3)  # Should grow capacity
        self.assertEqual(dq.capacity(), 4)
        self.assertEqual(dq.to_list(), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
