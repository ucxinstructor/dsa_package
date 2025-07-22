""" Module containing a HashSet class implemented using HashTable. """
from dsa.hashtable import HashTable

class HashSet:
    """
    A set implementation using a hash table for storage.
    """
    def __init__(self, iterable=None):
        self._table = HashTable()
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        self._table[item] = True

    def remove(self, item):
        del self._table[item]

    def contains(self, item):
        return item in self._table

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for key in self._table:
            yield key

    def __repr__(self):
        return f"HashSet({list(self)})"

    def __eq__(self, other):
        if not isinstance(other, HashSet):
            return False
        return set(self) == set(other)
