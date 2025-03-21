import unittest

from dsa.array import CircularArray

class TestArray(unittest.TestCase):
    def setUp(self):
        """Set up common test objects."""
        self.array = CircularArrayArray(capacity=5)
        self.array_with_elements = CircularArrayArray([1, 2, 3], capacity=5)




if __name__ == "__main__":
    unittest.main()
