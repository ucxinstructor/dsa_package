import unittest
from dsa.singlylinkedlist import LinkedList, Node

class TestLinkedList(unittest.TestCase):

    # --- Initialization & Conversion ---
    def test_initialization(self):
        """Test empty init and manual node linking."""
        ll = LinkedList()
        self.assertEqual(ll.count, 0)
        self.assertTrue(ll.is_empty())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

        # Single node
        n1 = Node(10)
        ll = LinkedList(n1, n1, 1)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)

    def test_conversions(self):
        """Test from_list and to_list functionality."""
        cases = [
            ([], 0),
            ([1], 1),
            ([1, 2, 3], 3)
        ]
        for values, expected_count in cases:
            with self.subTest(values=values):
                ll = LinkedList.from_list(values)
                self.assertEqual(len(ll), expected_count)
                self.assertEqual(ll.to_list(), values)
                if values:
                    self.assertEqual(ll.head.value, values[0])
                    self.assertEqual(ll.tail.value, values[-1])

    # --- Insertion Tests ---
    def test_append_prepend_logic(self):
        ll = LinkedList()
        ll.append(20)   # [20]
        ll.prepend(10)  # [10, 20]
        ll.append(30)   # [10, 20, 30]
        
        self.assertEqual(ll.to_list(), [10, 20, 30])
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 30)
        self.assertEqual(ll.count, 3)

    def test_insert_after(self):
        ll = LinkedList.from_list([1, 2, 4])
        
        # Middle
        ll.insert_after(2, 3) 
        # Tail
        ll.insert_after(4, 5)
        # Head
        ll.insert_after(1, 1.5)
        
        self.assertEqual(ll.to_list(), [1, 1.5, 2, 3, 4, 5])
        self.assertEqual(ll.tail.value, 5)

    # --- Deletion Tests ---
    def test_delete_by_value(self):
        ll = LinkedList.from_list([10, 20, 30, 40])
        
        ll.delete(10) # Head
        self.assertEqual(ll.head.value, 20)
        
        ll.delete(40) # Tail
        self.assertEqual(ll.tail.value, 30)
        
        ll.delete(20) # Only two left, delete head again
        self.assertEqual(ll.to_list(), [30])
        self.assertEqual(ll.head, ll.tail)

    def test_delete_head_tail_empty_or_single(self):
        # Test on single element list
        ll = LinkedList.from_list([1])
        ll.delete_head()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.count, 0)

        ll = LinkedList.from_list([1])
        ll.delete_tail()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    # --- Edge Cases & Error Handling ---
    def test_empty_list_operations(self):
        ll = LinkedList()
        with self.assertRaises(ValueError):
            ll.delete_head()
        with self.assertRaises(ValueError):
            ll.delete_tail()
        with self.assertRaises(ValueError):
            ll.delete(100)
        with self.assertRaises(ValueError):
            ll.insert_after(100, 200)

    def test_search_not_found(self):
        ll = LinkedList.from_list([1, 2, 3])
        self.assertIsNone(ll.search(99))
        self.assertIsNone(ll.search(None))

    def test_duplicate_values(self):
        """Ensure search and delete handle duplicates (deleting first occurrence)."""
        ll = LinkedList.from_list([1, 2, 2, 3])
        ll.delete(2)
        self.assertEqual(ll.to_list(), [1, 2, 3])
        self.assertEqual(ll.count, 3)

    def test_indexing_out_of_bounds(self):
        ll = LinkedList.from_list([1, 2, 3])
        with self.assertRaises(IndexError):
            _ = ll[3]
        with self.assertRaises(IndexError):
            _ = ll[-1] # Unless you specifically implement negative indexing

    def test_comparison_and_identity(self):
        ll1 = LinkedList.from_list([1, 2])
        ll2 = LinkedList.from_list([1, 2])
        ll3 = LinkedList.from_list([1, 3])
        
        self.assertEqual(ll1, ll2)
        self.assertNotEqual(ll1, ll3)
        self.assertNotEqual(ll1, "not a list")

    def test_large_dataset(self):
        """Stress test for 1000 items."""
        data = list(range(1000))
        ll = LinkedList.from_list(data)
        self.assertEqual(ll.count, 1000)
        self.assertEqual(ll.tail.value, 999)
        # Check integrity of links
        self.assertEqual(ll.to_list(), data)

if __name__ == "__main__":
    unittest.main()