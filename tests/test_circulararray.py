import unittest

from dsa.array import CircularArray

class TestArray(unittest.TestCase):
    def setUp(self):
        """Set up common test objects."""
        self.array = CircularArray(capacity=5)
        self.array_with_elements = CircularArray([1, 2, 3], capacity=5)

    def test_initialization(self):
        """Test initialization of CircularArray."""
        self.assertEqual(len(self.array), 0)
        self.assertEqual(self.array.capacity(), 5)

        self.assertEqual(len(self.array_with_elements), 3)
        self.assertEqual(self.array_with_elements.capacity(), 5)

    def test_indexing(self):
        self.assertRaises(IndexError, lambda: self.array[0])

        self.assertEqual(self.array_with_elements[0], 1)
        self.assertEqual(self.array_with_elements[2], 3)
        self.assertRaises(IndexError, lambda: self.array_with_elements[3])

        self.array_with_elements[0] = 10
        self.assertEqual(self.array_with_elements[0], 10)

    def test_append(self):
        """Test appending elements to CircularArray."""
        self.array.append(1)
        self.assertEqual(len(self.array), 1)
        self.assertEqual(self.array[0], 1)

        self.array.append(2)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[1], 2)

        # Test exceeding capacity (should wrap around)
        for i in range(5):
            self.array.append(i + 3)
        self.assertEqual(len(self.array), 5)
        self.assertEqual(self.array[0], 3)
        self.assertEqual(self.array[1], 4)
        self.assertEqual(self.array[4], 7)

        for i in range(12):
            self.array.append(i + 3)
        self.assertEqual(len(self.array), 5)
        self.assertEqual(self.array.capacity(), 5)
        self.assertEqual(self.array[0], 10)
        self.assertEqual(self.array[4], 14)
        self.array[0] = 100
        self.assertEqual(self.array[0], 100)

    def test_circularity(self):
        q = CircularArray(capacity=5)
        for _ in range(6):
            q.append(_ * 2)

        q.append(100)
        q.append(110)
        self.assertEqual(q.to_list(), [6, 8, 10, 100, 110])
        self.assertEqual(q.raw_view(), [10, 100, 110, 6, 8])

        q = CircularArray([0, 2, 4, 6, 8], capacity=5)
        q.append(100)
        q.append(110)
        self.assertEqual(q.to_list(), [4, 6, 8, 100, 110])
        self.assertEqual(q.raw_view(), [100, 110, 4, 6, 8])


if __name__ == "__main__":
    unittest.main()
