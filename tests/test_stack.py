import unittest
from dsa.stack import Stack, DynamicStack

class TestStack(unittest.TestCase):
    def test_create(self):
        st = Stack()
        self.assertTrue(st.is_empty())
        self.assertEqual(len(st), 0)
        self.assertEqual(st.capacity(), 10)
        self.assertEqual(st.top(), -1)

        st = Stack.from_list([1, 2, 3, 4, 5])
        self.assertFalse(st.is_empty())
        self.assertEqual(len(st), 5)
        self.assertEqual(st.capacity(), 10)
        self.assertEqual(st.top(), 4)
        self.assertEqual(st.peek(), 5)

        self.assertRaises(Exception, lambda: Stack.from_list([10] * 20))


        dst = DynamicStack()
        self.assertTrue(dst.is_empty())
        self.assertEqual(dst.capacity(), 10)
        self.assertEqual(len(dst), 0)
        self.assertEqual(dst.top(), -1)

        dst = DynamicStack.from_list([1, 2, 3, 4, 5])
        self.assertFalse(dst.is_empty())
        self.assertEqual(len(dst), 5)
        self.assertEqual(dst.peek(), 5)

        dst = DynamicStack.from_list([10] * 20)
        self.assertEqual(len(dst), 20)
        self.assertEqual(dst.top(), 19)
        self.assertEqual(dst.peek(), 10)
        dst.push(11)
        self.assertFalse(dst.is_empty())
        self.assertEqual(len(dst), 21)
        self.assertEqual(dst.top(), 20)
        self.assertEqual(dst.peek(), 11)

    def test_insert(self):
        st = Stack()

        for _ in range(10):
            st.push(_ * 2)
            self.assertEqual(st.peek(), _ * 2)
        self.assertEqual(st.top(), 9)
        self.assertEqual(st.count, 10)
        self.assertEqual(st.capacity(), 10)
        self.assertEqual(len(st), 10)
        self.assertRaises(Exception, st.push, 10)

        dst = DynamicStack()
        for _ in range(20):
            dst.push(_ * 2)
            self.assertEqual(dst.peek(), _ * 2)
        self.assertEqual(dst.top(), 19)
        self.assertEqual(dst.count, 20)
        self.assertEqual(len(dst), 20)
        self.assertGreater(dst.capacity(), 10)

        self.assertRaises(Exception, lambda:st.push(10))

    def test_delete(self):
        st = Stack()
        self.assertRaises(Exception, st.pop)

        for _ in range(10):
            st.push(_ * 2)

        for _ in range(10):
            v = st.pop()
            self.assertEqual(18 - _ * 2, v)
        self.assertTrue(st.is_empty())
        self.assertRaises(Exception, st.pop)

        dst = DynamicStack()
        self.assertRaises(Exception, dst.pop)
        for _ in range(20):
            dst.push(_ * 2)

        for _ in range(20):
            v = dst.pop()
            self.assertEqual(38 - _ * 2, v)
        self.assertTrue(dst.is_empty())
        self.assertRaises(Exception, dst.pop)

    def test_lists(self):
        test_list = [0, 2, 4, 6, 8]
        st1 = Stack.from_list(test_list)
        self.assertEqual(len(test_list), st1.count)

        st2 = Stack()
        for n in [0, 2, 4, 6, 8]:
            st2.push(n)
        self.assertEqual(st1.to_list(), st2.to_list())

if __name__ == '__main__':
    unittest.main()
