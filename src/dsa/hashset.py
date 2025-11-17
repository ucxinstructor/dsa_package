""" Module containing a HashSet class implemented using HashTable. """
from dsa.hashtable import HashTable

class HashSet:
    """
    A set implementation using a hash table for storage.
    """
    def __init__(self, iterable=None):
        """
        Initialize a hash set.

        Args:
            iterable: An optional iterable of initial elements.
        """
        self._table = HashTable()
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        """
        Add an item to the set.

        args:
            item: The item to add.
        """
        self._table[item] = True

    def remove(self, item):
        """
        Remove an item from the set.

        Args:
            item: The item to remove.
        """
        del self._table[item]

    def contains(self, item):
        """
        Check if an item is in the set.

        Args:
            item: The item to check.
        """
        return item in self._table

    def __contains__(self, item):
        """
        Check if an item is in the set.

        Args:
            item: The item to check.

        Returns:
            bool: True if the item is in the set, False otherwise.
        """
        return self.contains(item)

    def __len__(self):
        """
        Get the number of items in the set.

        Returns:
            int: The number of items in the set.
        """
        return len(self._table)

    def __iter__(self):
        """
        Iterate over the items in the set.

        Yields:
            The items in the set.
        """
        for key in self._table:
            yield key

    def __repr__(self):
        """
        Get a string representation of the set.

        Returns:
            str: A string representation of the set.
        """
        return f"HashSet({list(self)})"

    def __eq__(self, other):
        """
        Check if two sets are equal.

        Args:
            other: The other set to compare.

        Returns:
            bool: True if the sets are equal, False otherwise.
        """
        if not isinstance(other, HashSet):
            return False
        return set(self) == set(other)
