import unittest

from dsa.array import Array, DynamicArray

class TestArray(unittest.TestCase):
    def setUp(self):
        """Set up common test objects."""
        self.array = Array(capacity=5)
        self.array_with_elements = Array([1, 2, 3], capacity=5)

        self.dynarray = DynamicArray(capacity=5)
        self.dynarray_with_elements = DynamicArray([1, 2, 3], capacity=5)

    def test_create(self):
        a = Array()
        self.assertEqual(len(a), 0)

        b = Array([1, 2, 3, 4])
        self.assertEqual(b.count, 4)

        c = Array.from_list([1, 2, 3, 4, 5])        
        self.assertEqual(c.count, 5)

    def test_create_dynamic(self):
        da = DynamicArray()
        self.assertEqual(len(da), 0)

        db = DynamicArray([1, 2, 3, 4])
        self.assertEqual(db.count, 4)

        dc = Array.from_list([1, 2, 3, 4, 5])        
        self.assertEqual(dc.count, 5)

    def test_modify_static(self):
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

    def test_initialization_empty_static(self):
        """Test initializing an empty array."""
        self.assertEqual(len(self.array), 0)
        self.assertEqual(self.array.capacity(), 5)
        self.assertTrue(self.array.is_empty())

    def test_initialization_empty_dynamic(self):
        self.assertEqual(len(self.dynarray), 0)
        self.assertEqual(self.dynarray.capacity(), 5)
        self.assertTrue(self.dynarray.is_empty())


    def test_initialization_with_contents_static(self):
        """Test initializing an array with contents."""
        self.assertEqual(len(self.array_with_elements), 3)
        self.assertEqual(self.array_with_elements.to_list(), [1, 2, 3])
        self.assertFalse(self.array_with_elements.is_empty())

    def test_initialization_with_contents_dynamic(self):
        """Test initializing an array with contents."""
        self.assertEqual(len(self.dynarray_with_elements), 3)
        self.assertEqual(self.dynarray_with_elements.to_list(), [1, 2, 3])
        self.assertFalse(self.dynarray_with_elements.is_empty())

    def test_append_within_capacity_static(self):
        """Test appending elements within capacity."""
        self.array.append(10)
        self.assertEqual(self.array.to_list(), [10])
        self.assertEqual(len(self.array), 1)

    def test_append_within_capacity_dynamic(self):
        """Test appending elements within capacity."""
        self.dynarray.append(10)
        self.assertEqual(self.dynarray.to_list(), [10])
        self.assertEqual(len(self.dynarray), 1)

    def test_append_exceed_capacity_static(self):
        """Test appending elements exceeding capacity."""
        with self.assertRaises(Exception) as context:
            for i in range(6):
                self.array.append(i)
        self.assertEqual(str(context.exception), "Capacity Error: Maximum capacity 5 reached.")

    def test_append_exceed_capacity_dynamic(self):
        for i in range(1000):
            self.dynarray.append(i)
        self.assertEqual(self.dynarray.count, 1000)

    def test_insert_valid_index_static(self):
        """Test inserting an element at a valid index."""
        self.array_with_elements.insert(1, 99)
        self.assertEqual(self.array_with_elements.to_list(), [1, 99, 2, 3])
        self.assertEqual(len(self.array_with_elements), 4)

    def test_insert_valid_index_dynamic(self):
        self.dynarray_with_elements.insert(1, 99)
        self.assertEqual(self.dynarray_with_elements.to_list(), [1, 99, 2, 3])
        self.assertEqual(len(self.dynarray_with_elements), 4)

    def test_insert_invalid_index(self):
        """Test inserting an element at an invalid index."""
        with self.assertRaises(IndexError):
            self.array.insert(-1, 10)
            self.dynarray.insert(-1, 10)
        with self.assertRaises(IndexError):
            self.array.insert(10, 10)
            self.dynarray.insert(10, 10)

    def test_delete_valid_index_static(self):
        """Test deleting an element at a valid index."""
        self.array_with_elements.delete(1)
        self.assertEqual(self.array_with_elements.to_list(), [1, 3])
        self.assertEqual(len(self.array_with_elements), 2)

    def test_delete_valid_index_dynamic(self):
        """Test deleting an element at a valid index."""
        self.dynarray_with_elements.delete(1)
        self.assertEqual(self.dynarray_with_elements.to_list(), [1, 3])
        self.assertEqual(len(self.dynarray_with_elements), 2)

    def test_delete_invalid_index(self):
        """Test deleting an element at an invalid index."""
        with self.assertRaises(IndexError):
            self.array.delete(-1)
            self.dynarray.delete(-1)
        with self.assertRaises(IndexError):
            self.array.delete(10)
            self.dynarray.delete(-1)

    def test_get_item(self):
        """Test retrieving an element using the index operator."""
        self.assertEqual(self.array_with_elements[1], 2)
        self.assertEqual(self.dynarray_with_elements[1], 2)

    def test_get_item_invalid_index(self):
        """Test retrieving an element with an invalid index."""
        with self.assertRaises(IndexError):
            _ = self.array_with_elements[-1]
            _ = self.dynarray_with_elements[-1]
        with self.assertRaises(IndexError):
            _ = self.array_with_elements[10]
            _ = self.dynarray_with_elements[10]

    def test_set_item(self):
        """Test setting a value using the index operator."""
        self.array_with_elements[1] = 99
        self.assertEqual(self.array_with_elements.to_list(), [1, 99, 3])
        self.dynarray_with_elements[1] = 99
        self.assertEqual(self.dynarray_with_elements.to_list(), [1, 99, 3])

    def test_set_item_invalid_index(self):
        """Test setting a value with an invalid index."""
        with self.assertRaises(IndexError):
            self.array_with_elements[-1] = 10
            self.dynarray_with_elements[-1] = 10
        with self.assertRaises(IndexError):
            self.array_with_elements[10] = 10
            self.dynarray_with_elements[10] = 10

    def test_from_list_static(self):
        """Test creating an array from a standard Python list."""
        new_array = Array.from_list([5, 6, 7])
        self.assertEqual(new_array.to_list(), [5, 6, 7])
        self.assertEqual(len(new_array), 3)
        self.assertEqual(new_array.capacity(), 10)

    def test_from_list_dynamic(self):
        """Test creating an array from a standard Python list."""
        new_dynarray = DynamicArray.from_list([5, 6, 7])
        self.assertEqual(new_dynarray.to_list(), [5, 6, 7])
        self.assertEqual(len(new_dynarray), 3)
        self.assertEqual(new_dynarray.capacity(), 4)

    def test_repr(self):
        """Test the string representation of the array."""
        self.assertEqual(
            repr(self.array_with_elements), "[1, 2, 3] Count: 3 Capacity: 5"
        )
        self.assertEqual(
            repr(self.dynarray_with_elements), "[1, 2, 3] Count: 3 Capacity: 4"
        )

if __name__ == "__main__":
    unittest.main()
