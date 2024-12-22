import unittest

from dsa.array import Array, DynamicArray

class TestArray(unittest.TestCase):
    def test_create(self):
        a = Array()
        self.assertEqual(len(a), 0)

        b = Array([1, 2, 3, 4])
        self.assertEqual(b.count, 4)

        c = Array.from_list([1, 2, 3, 4, 5])        
        self.assertEqual(c.count, 5)

        da = DynamicArray()
        self.assertEqual(len(da), 0)

        db = DynamicArray([1, 2, 3, 4])
        self.assertEqual(db.count, 4)

        dc = Array.from_list([1, 2, 3, 4, 5])        
        self.assertEqual(dc.count, 5)

    def test_modify(self):
        a = Array()
        self.assertTrue(a.is_empty())
        a.append(10)
        self.assertFalse(a.is_empty())
        self.assertEqual(len(a), 1)
        a.append(20)
        self.assertEqual(len(a), 2)
        a.extend([30, 40])
        self.assertEqual(len(a), 4)

        self.assertEqual(a[0], 10)
        self.assertEqual(a[3], 40)
        self.assertEqual(a.to_list(), [10, 20, 30, 40])

        a.insert(0, 2)
        a.insert(4, 100)
        self.assertEqual(a[0], 2)
        self.assertEqual(a[1], 10)
        self.assertEqual(a[4], 100)

        a.delete(0)
        a.delete(3)
        self.assertEqual(a[0], 10)
        self.assertEqual(a[3], 40)

        a[0] = 1
        a[3] = 1000
        self.assertEqual(a[0], 1)
        self.assertEqual(a[3], 1000)

        # catch exceptions
        self.assertRaises(IndexError, a.__getitem__, 6)
        self.assertRaises(IndexError, a.__setitem__, 10, 10)
        self.assertRaises(Exception, a.extend, [1, 2, 3, 4, 5, 6, 7])

    def test_dynamic_modify(self):
        da = DynamicArray()
        self.assertTrue(da.is_empty())
        da.append(10)
        self.assertEqual(da.to_list(), [10])

        for _ in range(15):
            da.append(_)
        self.assertEqual(da.capacity() > 10, True)
        self.assertEqual(da.count, 16)
        self.assertFalse(da.is_empty())


if __name__ == '__main__':
    unittest.main()
