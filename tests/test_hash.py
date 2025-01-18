import unittest

from dsa.hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def test_create(self):
        ''' test constructor '''
        ht = HashTable()
        self.assertEqual(ht.count, 0)
        self.assertEqual(ht.capacity, 20)
        ht = HashTable(1000)
        self.assertEqual(ht.count, 0)
        self.assertEqual(ht.capacity, 1000)
        ht = HashTable(5)
        self.assertEqual(ht.count, 0)
        self.assertEqual(ht.capacity, 5)

    def test_set(self):
        ''' test set method '''
        ht = HashTable()

        self.assertEqual(ht.count, 0)
        ht.set("A", 1)
        ht.set("B", 2)
        ht.set("C", 3)
        ht.set("A", 4)
        self.assertEqual(ht.get("A"), 4)
        self.assertEqual(ht.get("B"), 2)
        self.assertEqual(ht.get("C"), 3)
        self.assertEqual(ht.count, 3)

    def test_set_delete(self):
        ''' test delete method'''
        ht = HashTable()
        ht.delete("A")

        self.assertEqual(ht.count, 0)
        ht.set("A", 1)
        ht.set("B", 2)
        ht.set("C", 3)
        ht.set("A", 4)

        ht.delete("A")
        ht.delete("D")
        self.assertEqual(ht.count, 2)

        ht.delete("A")
        ht.delete("D")
        self.assertEqual(ht.count, 2)

        ht.delete("B")
        ht.delete("C")
        ht.delete("X")
        self.assertEqual(ht.count, 0)

    def setUp(self):
        self.ht = HashTable()

    def test_initial_capacity(self):
        self.assertEqual(self.ht.capacity, 20)

    def test_initial_count(self):
        self.assertEqual(self.ht.count, 0)

    def test_set_and_get(self):
        self.ht.set("key1", "value1")
        self.assertEqual(self.ht.get("key1"), "value1")

    def test_key_exists(self):
        self.ht.set("key2", "value2")
        self.assertTrue(self.ht.key_exists("key2"))
        self.assertFalse(self.ht.key_exists("key3"))

    def test_delete(self):
        self.ht.set("key4", "value4")
        self.ht.delete("key4")
        self.assertFalse(self.ht.key_exists("key4"))
        self.assertIsNone(self.ht.get("key4"))

    def test_update_value(self):
        self.ht.set("key5", "value5")
        self.ht.set("key5", "new_value5")
        self.assertEqual(self.ht.get("key5"), "new_value5")

    def test_repr(self):
        self.ht.set("key6", "value6")
        self.assertEqual(repr(self.ht), "{key6:value6}")

    def test_show_buckets(self):
        self.ht.set("key7", "value7")
        buckets = self.ht.show_buckets()
        self.assertIn("Bucket", buckets)
        self.assertIn("key7", buckets)