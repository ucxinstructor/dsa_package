import unittest
from dsa.singlylinkedlist import LinkedList, Node

class TestLinkedList(unittest.TestCase):

    # --- Creation Tests ---
    def test_initialization(self):
        ll = LinkedList()
        self.assertEqual(ll.count, 0)
        self.assertTrue(ll.is_empty())

        n1 = Node(10)
        ll = LinkedList(n1)
        self.assertEqual(ll.count, 1)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)

        n2 = Node(20)
        n1.next = n2
        ll = LinkedList(n1, n2, 2)
        self.assertEqual(ll.count, 2)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 20)

        n3 = Node(30)
        n2.next = n3
        ll = LinkedList(n1, n3, 3)
        self.assertEqual(ll.count, 3)
        self.assertEqual(len(ll), 3)
        self.assertFalse(ll.is_empty())

    # --- Conversion Tests ---
    def test_from_list(self):
        for values, expected_count in [([], 0), ([1], 1), ([1, 2], 2), ([1, 2, 3], 3)]:
            ll = LinkedList.from_list(values)
            self.assertEqual(ll.count, expected_count)
            if values:
                self.assertEqual(ll.head.value, values[0])
                self.assertEqual(ll.tail.value, values[-1])
            else:
                self.assertIsNone(ll.head)
                self.assertIsNone(ll.tail)

    def test_to_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), [])
        for i in range(15):
            ll.append(i)
        self.assertEqual(ll.to_list(), list(range(15)))

    # --- Search Tests ---
    def test_search_valid_and_invalid(self):
        ll = LinkedList.from_list(range(20))
        node = ll.search(10)
        self.assertEqual(node.value, 10)
        node = ll.search(1)
        self.assertEqual(node.value, 1)
        node = ll.search(-1)
        self.assertIsNone(node)
        node = ll.search(20)
        self.assertIsNone(node)

    # --- Insertion Tests ---
    def test_append_and_prepend(self):
        ll = LinkedList()
        for i in range(15):
            ll.append(i)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.count, 15)

        for i in range(10):
            ll.prepend(i)
        self.assertEqual(ll[0], 9)
        self.assertEqual(ll[2], 7)
        self.assertEqual(ll.count, 25)


    def test_insert_after_empty_list(self):
        ll = LinkedList()
        self.assertRaises(ValueError, ll.insert_after, 0, 100)

    def test_insert_after_invalid(self):
        ll = LinkedList()
        for i in range(10):
            ll.append(i)
        self.assertRaises(ValueError, ll.insert_after, 20, 100)

    def test_insert_after_head_tail_and_middle(self):
        ll = LinkedList.from_list(range(10))
        ll.insert_after(0, -1)  # after head
        self.assertEqual(ll[1], -1) 
        node = ll.search(0)
        self.assertEqual(node.value, 0)
        node = ll.search(-1)
        self.assertEqual(node.value, -1)
        ll.insert_after(9, 100)  # after tail
        self.assertEqual(ll.tail.value, 100)
        ll.insert_after(4, 50)  # in the middle
        node = ll.search(50)
        self.assertEqual(node.value, 50)
        self.assertEqual(node.next.value, 5)
        self.assertEqual(ll.count, 13)

    # --- Deletion Tests ---
    def test_delete_value(self):
        ll = LinkedList()
        for i in range(15):
            ll.append(i)
        self.assertRaises(ValueError, ll.delete, 15)

        for i in range(15):
            ll.delete(i)
            self.assertEqual(ll.count, 14 - i)
        self.assertRaises(ValueError, ll.delete, 0)

        for i in range(15):
            ll.append(i)
        for i in range(14, -1, -1):
            ll.delete(i)
            self.assertEqual(ll.count, i)
        self.assertRaises(ValueError, ll.delete, 0)

    def test_delete_middle_and_edges(self):
        ll = LinkedList.from_list(range(15))
        ll.delete(7)
        self.assertEqual(ll.count, 14)
        self.assertRaises(ValueError, ll.delete, 7)

        ll.delete(14)
        self.assertEqual(ll.tail.value, 13)
        self.assertEqual(ll.count, 13)

        ll = LinkedList.from_list(range(20))
        ll.delete(19)
        self.assertEqual(ll.tail.value, 18)
        ll.delete(0)
        self.assertEqual(ll.head.value, 1)
        ll.delete(3)
        self.assertEqual(ll[2], 4)
        self.assertEqual(ll.count, 17)

    def test_delete_head(self):
        ll = LinkedList()
        self.assertRaises(IndexError, ll.delete_head)
        for i in range(15):
            ll.append(i)
        ll.delete_head()
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.count, 14)

    def test_delete_tail(self):
        ll = LinkedList()
        self.assertRaises(IndexError, ll.delete_tail)
        for i in range(15):
            ll.append(i)
        ll.delete_tail()
        self.assertEqual(ll.tail.value, 13)
        self.assertEqual(ll.count, 14)

    # --- Utility Tests ---
    def test_traverse_order(self):
        ll = LinkedList()
        for i in range(15):
            ll.append(i)

        node = ll.head
        for i in range(15):
            self.assertEqual(node.value, i)
            node = node.next

    def test_indexing(self):
        ll = LinkedList.from_list(range(20))
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[19], 19)

    def test_eq(self):
        ll1 = LinkedList.from_list([1, 2, 3, 4])
        ll2 = LinkedList.from_list([1, 2, 3, 4])
        self.assertEqual(ll1, ll2)

        ll3 = LinkedList.from_list([1, 2, 3])
        self.assertNotEqual(ll1, ll3)

        ll4 = LinkedList()
        ll5 = LinkedList()
        self.assertEqual(ll4, ll5)

        self.assertNotEqual(ll1, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
