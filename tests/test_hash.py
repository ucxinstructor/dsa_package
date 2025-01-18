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

    def test_delete(self):
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