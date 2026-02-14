import unittest
from dsa.hashset import HashSet

class TestHashSet(unittest.TestCase):
    def test_add_duplicates(self):
        s = HashSet()
        s.add(1)
        s.add(1)
        s.add(2)
        self.assertEqual(len(s), 2)
        self.assertIn(1, s)
        self.assertIn(2, s)

    def test_init_with_iterable(self):
        s = HashSet.from_list([1, 2, 2, 3])
        self.assertEqual(len(s), 3)
        self.assertIn(1, s)
        self.assertIn(2, s)
        self.assertIn(3, s)

    def test_add_and_contains(self):
        s = HashSet()
        s.add(1)
        s.add(2)
        s.add(3)
        self.assertIn(1, s)
        self.assertIn(2, s)
        self.assertIn(3, s)
        self.assertNotIn(4, s)

    def test_remove(self):
        s = HashSet.from_list([1, 2, 3])
        s.remove(2)
        self.assertNotIn(2, s)
        self.assertIn(1, s)
        self.assertIn(3, s)
        with self.assertRaises(KeyError):
            s.remove(4)

    def test_len_and_iter(self):
        s = HashSet.from_list([1, 2, 3])
        self.assertEqual(len(s), 3)
        self.assertEqual(set(s), {1, 2, 3})

    def test_eq(self):
        s1 = HashSet.from_list([1, 2, 3])
        s2 = HashSet.from_list([3, 2, 1])
        s3 = HashSet.from_list([1, 2])
        self.assertEqual(s1, s2)
        self.assertNotEqual(s1, s3)
        
        
    def test_from_list_empty(self):
        s = HashSet.from_list()
        self.assertEqual(len(s), 0)
        self.assertNotIn(1, s)
        
    def test_from_list_with_duplicates(self):
        s = HashSet.from_list([1, 2, 2, 3, 3, 3])
        self.assertEqual(len(s), 3)
        self.assertIn(1, s)
        self.assertIn(2, s)
        self.assertIn(3, s)
        
    def test_capacity_initialization(self):
        s = HashSet(capacity=20)
        self.assertEqual(len(s), 0)
        s.add(1)
        s.add(2)
        self.assertIn(1, s)
        self.assertIn(2, s)
        self.assertEqual(s._table.capacity, 20)
        
        s = HashSet(capacity=100)
        self.assertEqual(s._table.capacity, 100)
        
        s = HashSet()
        self.assertEqual(s._table.capacity, 10)
    
    def test_to_list(self):
        s = HashSet.from_list([1, 2, 3])
        lst = s.to_list()
        self.assertEqual(set(lst), {1, 2, 3})
        self.assertEqual(len(lst), 3)
        
        s = HashSet()
        lst = s.to_list()
        self.assertEqual(lst, [])
        
        s = HashSet()
        s.add(1)
        s.add(2)
        lst = s.to_list()
        self.assertEqual(set(lst), {1, 2})
        self.assertEqual(len(lst), 2)
        
if __name__ == "__main__":
    unittest.main()
