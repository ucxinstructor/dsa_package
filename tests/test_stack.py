import unittest
from dsa.stack import Stack, DynamicStack

class TestStack(unittest.TestCase):

    # --- Static Stack Tests ---
    def test_stack_creation(self):
        st = Stack()
        self.assertTrue(st.is_empty())
        self.assertEqual(len(st), 0)
        self.assertEqual(st.capacity(), 10)
        self.assertEqual(st.top(), -1)

    def test_stack_from_list_and_limits(self):
        st = Stack.from_list([1, 2, 3, 4, 5])
        self.assertFalse(st.is_empty())
        self.assertEqual(len(st), 5)
        self.assertEqual(st.capacity(), 10)
        self.assertEqual(st.top(), 4)
        self.assertEqual(st.peek(), 5)

        self.assertRaises(Exception, lambda: Stack.from_list([10] * 20))

    def test_stack_push_behavior(self):
        st = Stack()
        for i in range(10):
            st.push(i * 2)
            self.assertEqual(st.peek(), i * 2)
        self.assertEqual(st.top(), 9)
        self.assertEqual(st.count, 10)
        self.assertEqual(len(st), 10)
        self.assertRaises(Exception, st.push, 10)

    def test_stack_pop_behavior(self):
        st = Stack()
        self.assertRaises(Exception, st.pop)

        for i in range(10):
            st.push(i * 2)

        for i in range(10):
            self.assertEqual(st.pop(), 18 - i * 2)

        self.assertTrue(st.is_empty())
        self.assertRaises(Exception, st.pop)

    # --- Dynamic Stack Tests ---
    def test_dynamic_stack_creation(self):
        dst = DynamicStack()
        self.assertTrue(dst.is_empty())
        self.assertEqual(dst.capacity(), 10)
        self.assertEqual(len(dst), 0)
        self.assertEqual(dst.top(), -1)

    def test_dynamic_stack_from_list_and_growth(self):
        dst = DynamicStack.from_list([1, 2, 3, 4, 5])
        self.assertFalse(dst.is_empty())
        self.assertEqual(len(dst), 5)
        self.assertEqual(dst.peek(), 5)

        dst = DynamicStack.from_list([10] * 20)
        self.assertEqual(len(dst), 20)
        self.assertEqual(dst.top(), 19)
        self.assertEqual(dst.peek(), 10)

        dst.push(11)
        self.assertEqual(len(dst), 21)
        self.assertEqual(dst.top(), 20)
        self.assertEqual(dst.peek(), 11)

    def test_dynamic_stack_push_pop_behavior(self):
        dst = DynamicStack()
        self.assertRaises(Exception, dst.pop)

        for i in range(20):
            dst.push(i * 2)
            self.assertEqual(dst.peek(), i * 2)
        self.assertGreater(dst.capacity(), 10)
        self.assertEqual(dst.top(), 19)
        self.assertEqual(len(dst), 20)

        for i in range(20):
            self.assertEqual(dst.pop(), 38 - i * 2)
        self.assertTrue(dst.is_empty())
        self.assertRaises(Exception, dst.pop)

    # --- Shared Behavior Tests ---
    def test_to_and_from_list_consistency(self):
        values = [0, 2, 4, 6, 8]
        st1 = Stack.from_list(values)
        self.assertEqual(len(values), st1.count)

        st2 = Stack()
        for val in values:
            st2.push(val)

        self.assertEqual(st1.to_list(), st2.to_list())

if __name__ == '__main__':
    unittest.main()
