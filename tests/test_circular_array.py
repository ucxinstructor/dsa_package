import unittest

from dsa.array import CircularArray

class TestArray(unittest.TestCase):
    def setUp(self):
        """Set up common test objects."""
        self.array = CircularArray(capacity=5)
        self.array_with_elements = CircularArray([1, 2, 3], capacity=5)

    def test_initialization(self):
        """Test initialization of CircularArray."""
        self.assertEqual(self.array.size, 0)
        self.assertEqual(self.array.capacity, 5)
        self.assertEqual(self.array_with_elements.size, 3)
        self.assertEqual(self.array_with_elements.capacity, 5)

    def test_insert(self): 
        """Test inserting elements into CircularArray."""
        self.array.insert(1)
        self.assertEqual(self.array.size, 1)
        self.assertEqual(self.array[0], 1)

        self.array.insert(2)
        self.assertEqual(self.array.size, 2)
        self.assertEqual(self.array[1], 2)


    def test_insert_full(self): 
        """Test inserting elements into a full CircularArray."""
        for i in range(5):
            self.array.insert(i+1)
        
        self.assertRaises(Exception, self.array.insert, 6)





if __name__ == "__main__":
    unittest.main()
