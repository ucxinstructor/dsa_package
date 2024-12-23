import unittest
from dsa.sorttools import rand_int_array, filled_array, shuffle_array

class TestSortTools(unittest.TestCase):

    def test_rand_int_array(self):
        n = 10
        maxnum = 50
        result = rand_int_array(n, maxnum)
        self.assertEqual(len(result), n)
        for num in result:
            self.assertTrue(0 <= num <= maxnum)

    def test_filled_array(self):
        n = 10
        result = filled_array(n)
        self.assertEqual(len(result), n)
        for i in range(n):
            self.assertEqual(result[i], i)

    def test_shuffle_array(self):
        n = 10
        result = shuffle_array(n)
        self.assertEqual(len(result), n)
        self.assertEqual(set(result), set(range(n)))
        self.assertNotEqual(result, list(range(n)))  # Ensure the array is shuffled

if __name__ == '__main__':
    unittest.main()