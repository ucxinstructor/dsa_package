import unittest
from dsa.hashtable import HashTable

class TestHashTable(unittest.TestCase):
    
    def setUp(self):
        self.ht = HashTable()

    # --- Constructor Tests ---
    def test_create_with_default_and_custom_capacity(self):
        self.assertEqual(self.ht.count, 0)
        self.assertEqual(self.ht.capacity, 20)

        custom_ht = HashTable(1000)
        self.assertEqual(custom_ht.count, 0)
        self.assertEqual(custom_ht.capacity, 1000)

        small_ht = HashTable(5)
        self.assertEqual(small_ht.count, 0)
        self.assertEqual(small_ht.capacity, 5)

    # --- Set and Get Tests ---
    def test_set_and_get_values(self):
        self.ht.set("A", 1)
        self.ht.set("B", 2)
        self.ht.set("C", 3)
        self.ht.set("A", 4)  # overwrite

        self.assertEqual(self.ht.get("A"), 4)
        self.assertEqual(self.ht.get("B"), 2)
        self.assertEqual(self.ht.get("C"), 3)
        self.assertEqual(self.ht.count, 3)

    def test_set_with_varied_key_types(self):
        self.ht.set(1, "one")
        self.ht.set(2.5, "two point five")
        self.ht.set((1, 2), "tuple key")

        self.assertEqual(self.ht.get(1), "one")
        self.assertEqual(self.ht.get(2.5), "two point five")
        self.assertEqual(self.ht.get((1, 2)), "tuple key")

    def test_update_value(self):
        self.ht.set("key", "initial")
        self.ht.set("key", "updated")
        self.assertEqual(self.ht.get("key"), "updated")

    # --- Key Existence and Membership ---
    def test_key_existence_and_membership(self):
        self.ht.set("exists", "yes")
        self.assertTrue(self.ht.key_exists("exists"))
        self.assertFalse(self.ht.key_exists("missing"))

        self.assertTrue("exists" in self.ht)
        self.assertFalse("missing" in self.ht)

    # --- Remove Tests ---
    def test_remove_keys(self):
        self.ht.set("A", 1)
        self.ht.set("B", 2)
        self.ht.set("C", 3)
        self.ht.remove("A")
        with self.assertRaises(KeyError):
            self.ht.remove("D")  # nonexistent

        self.assertEqual(self.ht.count, 2)
        self.ht.remove("B")
        self.ht.remove("C")
        self.assertEqual(self.ht.count, 0)

    def test_remove_varied_key_types(self):
        self.ht.set(1, "one")
        self.ht.set(2.5, "two point five")
        self.ht.set((1, 2), "tuple key")

        self.ht.remove(1)
        self.ht.remove(2.5)
        self.ht.remove((1, 2))

        self.assertEqual(self.ht.count, 0)

    # --- Pop Test ---
    def test_pop_method(self):
        self.ht.set("A", 1)
        self.ht.set("B", 2)

        self.assertEqual(self.ht.pop("A"), 1)
        self.assertEqual(self.ht.pop("C", "not found"), "not found")
        self.assertEqual(len(self.ht), 1)
        self.assertFalse(self.ht.key_exists("A"))

    # --- Dunder Method Tests ---
    def test_dunder_methods(self):
        self.ht["A"] = 1
        self.ht["B"] = 2

        self.assertEqual(self.ht["A"], 1)
        self.assertEqual(self.ht["B"], 2)
        self.assertIsNone(self.ht["C"])

        self.ht["C"] = 3
        self.assertEqual(len(self.ht), 3)

        del self.ht["A"]
        self.assertEqual(len(self.ht), 2)
        self.assertFalse("A" in self.ht)
        self.assertTrue("B" in self.ht)

    # --- Miscellaneous Tests ---
    def test_repr_format(self):
        self.ht.set("key", "value")
        self.assertEqual(repr(self.ht), "{key:value}")

    def test_show_buckets_output(self):
        self.ht.set("key", "value")
        buckets = self.ht.show_buckets()
        self.assertIn("Bucket", buckets)
        self.assertIn("key", buckets)

    def test_len_behavior(self):
        new_ht = HashTable()
        self.assertEqual(len(new_ht), 0)
        new_ht.set("A", 1)
        new_ht.set("B", 2)
        self.assertEqual(len(new_ht), 2)
        new_ht.remove("A")
        self.assertEqual(len(new_ht), 1)

    def test_enumerate_method(self):
        ht = HashTable()
        ht.set("A", 1)
        ht.set("B", 2)
        ht.set("C", 3)

        items = list(ht.enumerate())
        self.assertEqual(len(items), 3)
        self.assertIn((0, ["A", 1]), items)
        self.assertIn((1, ["B", 2]), items)
        self.assertIn((2, ["C", 3]), items)
    
    def test_eq(self):
        ht1 = HashTable()
        ht2 = HashTable()
        ht3 = HashTable()
        for k, v in [("A", 1), ("B", 2), ("C", 3)]:
            ht1.set(k, v)
            ht2.set(k, v)
        ht3.set("A", 1)
        ht3.set("B", 2)
        ht3.set("C", 4)
        ht_empty1 = HashTable()
        ht_empty2 = HashTable()
        self.assertEqual(ht1, ht2)
        self.assertNotEqual(ht1, ht3)
        self.assertEqual(ht_empty1, ht_empty2)
        self.assertNotEqual(ht1, HashTable())
        self.assertNotEqual(ht1, {"A": 1, "B": 2, "C": 3})