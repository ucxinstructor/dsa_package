import unittest
from dsa.doublylinkedlist import DoublyLinkedList, Node

class TestDoublyLinkedList(unittest.TestCase):

    # --- Initialization Tests ---
    def test_empty_initialization(self):
        ll = DoublyLinkedList()
        self.assertEqual(ll.count, 0)
        self.assertTrue(ll.is_empty())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_init_with_head(self):
        node = Node(1)
        ll = DoublyLinkedList(head=node)
        self.assertEqual(ll.head, node)
        self.assertEqual(ll.tail, node)
        self.assertEqual(ll.count, 1)

    def test_init_with_head_and_tail(self):
        head = Node(1)
        tail = Node(2)
        ll = DoublyLinkedList(head=head, tail=tail, count=2)
        self.assertEqual(ll.head, head)
        self.assertEqual(ll.tail, tail)
        self.assertEqual(ll.count, 2)

    def test_create_chain(self):
        n1, n2, n3 = Node(10), Node(20), Node(30)
        n1.next = n2
        n2.next = n3
        ll = DoublyLinkedList(n1, n3, 3)
        self.assertEqual(ll.count, 3)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 30)
        self.assertFalse(ll.is_empty())

    # --- List Conversion Tests ---
    def test_from_list_various_lengths(self):
        for values in [[], [1], [1, 2], [1, 2, 3]]:
            ll = DoublyLinkedList.from_list(values)
            self.assertEqual(ll.to_list(), values)
            self.assertEqual(ll.count, len(values))

    def test_repr_output(self):
        ll = DoublyLinkedList.from_list([1, 2, 3, 4])
        self.assertEqual(repr(ll), "[ 1 2 3 4 ] Count: 4")

    # --- Search and Indexing ---
    def test_search_existing_and_invalid(self):
        ll = DoublyLinkedList.from_list(range(20))
        self.assertEqual(ll.search(1), 1)
        self.assertEqual(ll.search(10), 10)
        self.assertRaises(Exception, ll.search, -1)
        self.assertRaises(Exception, ll.search, 20)

    def test_index_access(self):
        ll = DoublyLinkedList.from_list(range(20))
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[19], 19)

    # --- Insertion Tests ---
    def test_append_and_prepend(self):
        ll = DoublyLinkedList()
        for i in range(15):
            ll.append(i)
        for i in range(10):
            ll.prepend(i)
        self.assertEqual(ll[0], 9)
        self.assertEqual(ll[2], 7)
        self.assertEqual(ll.count, 25)
        self.verify_prev_links(ll)

    def test_insert_at_various_indices(self):
        ll = DoublyLinkedList.from_list(list(range(15)))
        inserts = [(0, 100), (1, 200), (10, 300), (14, 400), (15, 500)]
        for index, value in inserts:
            ll.insert(index, value)
            self.assertEqual(ll[index], value)
        self.assertEqual(ll.head.value, 100)
        self.assertEqual(ll.tail.value, 14)
        self.assertRaises(IndexError, ll.insert, 21, 600)
        self.assertEqual(ll.tail.value, 14)
        self.verify_prev_links(ll)

    # --- Deletion Tests ---
    def test_delete_at_indices(self):
        ll = DoublyLinkedList.from_list(range(15))
        self.assertRaises(IndexError, ll.delete, 15)
        for _ in range(15):
            ll.delete(0)
        self.assertEqual(ll.count, 0)
        self.assertRaises(IndexError, ll.delete, 0)

        ll = DoublyLinkedList.from_list(range(15))
        for _ in range(15):
            ll.delete(len(ll) - 1)
        self.assertEqual(ll.count, 0)
        self.verify_prev_links(ll)

        ll = DoublyLinkedList.from_list(range(15))
        for _ in range(5):
            ll.delete(len(ll) // 2)
        self.assertEqual(ll.count, 10)
        self.verify_prev_links(ll)

    def test_delete_head_tail_and_middle(self):
        ll = DoublyLinkedList.from_list(range(20))
        ll.delete(19)
        self.assertEqual(ll.tail.value, 18)
        ll.delete(0)
        self.assertEqual(ll.head.value, 1)
        ll.delete(3)
        self.assertEqual(ll[3], 5)
        self.assertEqual(ll.count, 17)
        self.verify_prev_links(ll)

    def test_delete_head_method(self):
        dll = DoublyLinkedList()
        self.assertRaises(IndexError, dll.delete_head)
        dll = DoublyLinkedList.from_list([1, 2, 3])
        dll.delete_head()
        self.assertEqual(dll.to_list(), [2, 3])
        self.assertEqual(dll.count, 2)

    def test_delete_tail_method(self):
        dll = DoublyLinkedList()
        self.assertRaises(IndexError, dll.delete_tail)
        dll = DoublyLinkedList.from_list([1, 2, 3])
        dll.delete_tail()
        self.assertEqual(dll.to_list(), [1, 2])
        self.assertEqual(dll.count, 2)

    # --- Traversal ---
    def test_traverse_forward_and_backward(self):
        ll = DoublyLinkedList.from_list(range(15))
        node = ll.head
        for i in range(15):
            self.assertEqual(node.value, i)
            node = node.next

        node = ll.tail
        for i in range(15):
            self.assertEqual(node.value, 14 - i)
            node = node.prev

    # --- Helper Verification ---
    def verify_prev_links(self, ll):
        node = ll.head
        while node and node.next:
            self.assertEqual(node.next.prev, node)
            node = node.next
            self.assertIsNotNone(node.prev, "Malformed list: missing prev link")
    
    def test_eq(self):
        dll1 = DoublyLinkedList.from_list([1, 2, 3, 4])
        dll2 = DoublyLinkedList.from_list([1, 2, 3, 4])
        dll3 = DoublyLinkedList.from_list([1, 2, 3, 5])
        dll_empty1 = DoublyLinkedList()
        dll_empty2 = DoublyLinkedList()
        self.assertEqual(dll1, dll2)
        self.assertNotEqual(dll1, dll3)
        self.assertEqual(dll_empty1, dll_empty2)
        self.assertNotEqual(dll1, DoublyLinkedList.from_list([1, 2, 3]))
        self.assertNotEqual(dll1, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
