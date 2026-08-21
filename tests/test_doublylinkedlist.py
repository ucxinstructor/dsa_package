import unittest
from dsa.doublylinkedlist import DoublyLinkedList, Node

class TestDoublyLinkedList(unittest.TestCase):

    # --- Helper Method ---
    def verify_integrity(self, dll):
        """Custom helper to ensure all next/prev links and head/tail are consistent."""
        if dll.count == 0:
            self.assertIsNone(dll.head)
            self.assertIsNone(dll.tail)
            return

        # Check forward and backward consistency
        nodes = []
        curr = dll.head
        while curr:
            nodes.append(curr)
            if curr.next:
                self.assertEqual(curr.next.prev, curr, "Next node's prev link is broken")
            curr = curr.next
        
        self.assertEqual(len(nodes), dll.count, "Count does not match actual nodes")
        self.assertEqual(nodes[0], dll.head)
        self.assertEqual(nodes[-1], dll.tail)
        self.assertIsNone(dll.head.prev, "Head prev should be None")
        self.assertIsNone(dll.tail.next, "Tail next should be None")

    # --- Initialization & Conversion ---
    def test_initialization(self):
        dll = DoublyLinkedList()
        self.assertTrue(dll.is_empty())
        self.verify_integrity(dll)

        # Init with chain
        n1, n2 = Node(1), Node(2)
        n1.next = n2
        n2.prev = n1
        dll = DoublyLinkedList(n1, n2, 2)
        self.verify_integrity(dll)

    def test_conversions(self):
        cases = [[], [1], [1, 2, 3]]
        for values in cases:
            with self.subTest(values=values):
                dll = DoublyLinkedList.from_list(values)
                self.assertEqual(dll.to_list(), values)
                self.verify_integrity(dll)

    # --- Insertion Tests ---
    def test_append_prepend_logic(self):
        dll = DoublyLinkedList()
        dll.append(20)   # [20]
        dll.prepend(10)  # [10, 20]
        dll.append(30)   # [10, 20, 30]
        
        self.assertEqual(dll.to_list(), [10, 20, 30])
        self.verify_integrity(dll)

    def test_insert_after(self):
        dll = DoublyLinkedList.from_list([10, 30])
        
        # Insert in middle
        dll.insert_after(10, 20)
        # Insert at tail
        dll.insert_after(30, 40)
        
        self.assertEqual(dll.to_list(), [10, 20, 30, 40])
        self.verify_integrity(dll)

    # --- Deletion Tests ---
    def test_delete_by_value(self):
        dll = DoublyLinkedList.from_list([1, 2, 3])
        
        dll.delete(2) # Middle
        self.assertEqual(dll.to_list(), [1, 3])
        self.verify_integrity(dll)
        
        dll.delete(1) # Head
        self.assertEqual(dll.head.value, 3)
        self.verify_integrity(dll)

    def test_delete_head_tail_edge_cases(self):
        # Single element list
        dll = DoublyLinkedList.from_list([100])
        dll.delete_head()
        self.assertEqual(dll.count, 0)
        self.verify_integrity(dll)

        # Test delete_tail on single element
        dll = DoublyLinkedList.from_list([200])
        dll.delete_tail()
        self.verify_integrity(dll)

    # --- Search & Indexing ---
    def test_search_and_indexing(self):
        dll = DoublyLinkedList.from_list([10, 20, 30])
        self.assertEqual(dll.search(20).value, 20)
        self.assertIsNone(dll.search(99))
        self.assertEqual(dll[1], 20)

    # --- Traversals ---
    def test_traversals(self):
        values = [1, 2, 3]
        dll = DoublyLinkedList.from_list(values)
        
        # Manually check reverse via prev links
        curr = dll.tail
        results = []
        while curr:
            results.append(curr.value)
            curr = curr.prev
        self.assertEqual(results, [3, 2, 1])

    # --- New Edge Cases ---
    def test_empty_list_errors(self):
        dll = DoublyLinkedList()
        with self.assertRaises(ValueError):
            dll.delete_head()
        with self.assertRaises(ValueError):
            dll.delete_tail()
        with self.assertRaises(ValueError):
            dll.delete(5)

    def test_re_insertion_after_clear(self):
        """Check if list works correctly after being emptied."""
        dll = DoublyLinkedList.from_list([1, 2])
        dll.delete(1)
        dll.delete(2)
        self.assertTrue(dll.is_empty())
        
        dll.append(10)
        self.assertEqual(dll.head.value, 10)
        self.assertEqual(dll.tail.value, 10)
        self.verify_integrity(dll)

    def test_equality(self):
        dll1 = DoublyLinkedList.from_list([1, 2])
        dll2 = DoublyLinkedList.from_list([1, 2])
        self.assertEqual(dll1, dll2)
        self.assertNotEqual(dll1, [1, 2]) # Type safety check

if __name__ == "__main__":
    unittest.main()