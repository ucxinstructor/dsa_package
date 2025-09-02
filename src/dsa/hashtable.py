""" Module containing hash table class. """

class HashTable:
    """ 
    A hashtable implementation. 
    """
    def __init__(self, capacity=20):
        """
        Initialize a hashtable with a given capacity.

        Args:
            capacity: The capacity of the hashtable.
        """
        self.capacity = capacity

        self.array = []
        for _ in range(self.capacity):
            self.array.append([])

        #: the number of items in the hashtable
        self.count = 0
        
    def hash_function(self, key) -> int:
        """ 
        Return a hash value based on a given key. 

        Args:
            key: The key to convert to a hashvalue.
        Returns:
            Hash value modded to the hashtable capacity.
        """
        mult = 31
        hash_val = 0
        for character in str(key):
            hash_val *= mult
            hash_val += ord(character)
            hash_val %= (2**32)

        return hash_val % self.capacity
        
    def key_exists(self, key) -> bool:
        """ 
        Returns a Boolean on whether a key exists in the hashtable or not .

        Args:
            key: The key to check for in the hashtable.
        Returns:
            Boolean of key existence.
        """
        bucket = self.hash_function(key)
        
        for e in self.array[bucket]:
            if e[0] == key:
                return True
        return False

    def set(self, key, value):
        """ 
        Set a key-value pair in the hashtable.

        If key exists, replace the value otherwise, create a new key-pair.

        Args:
            key: The key to check for.
            value: The value to set or create.
        """

        bucket = self.hash_function(key)

        # linear searh for key 
        for e in self.array[bucket]:
            if e[0] == key:
                e[1] = value
                break
        else:
            self.array[bucket].append([ key, value ])
            self.count += 1

    def get(self, key):
        """ 
        Get corresponding value of a given key in the hash table.

        Args:
            key: The key to check for.
            value: The value to set or create.
        Returns:
            corresponding value of key.
            None if key is not found.
        """
        bucket = self.hash_function(key)

        for e in self.array[bucket]:
            if e[0] == key:
                return e[1]

        return None

    def remove(self, key):
        """
        Remove key-value pair if specified key is found. Raise KeyError if not found.

        Args:
            key: The key to check for.
        Raises:
            KeyError: If the key is not found in the hashtable.
        """
        bucket = self.hash_function(key)
        for i in range(len(self.array[bucket])):
            kvpair = self.array[bucket][i]
            if kvpair and kvpair[0] == key:
                del self.array[bucket][i]
                self.count -= 1
                return
        raise KeyError(key)
    
    def __repr__(self):
        """
        Return a string representation of the hashtable.
        """
        s = "{"
        pairs = []
        for bucket in self.array:
            if bucket:
                for chain_link in bucket:
                    pairs.append(f"{chain_link[0]}:{chain_link[1]}")
        s += ", ".join(pairs)
        return s + "}"

    def show_buckets(self):
        """
        Return a string displaying the contents of all buckets in the hashtable.
        """
        s = ""
        for i, bucket in enumerate(self.array):
            s += f"Bucket {i}: {bucket}\n"
        return s
    
    def __len__(self):
        """
        Return the number of items in the hashtable.
        """
        return self.count
    
    def __getitem__(self, key):
        """
        Get the value associated with the key using indexing.

        Args:
            key: The key to look up.
        Returns:
            The value associated with the key.
        """
        return self.get(key)
    
    def __setitem__(self, key, value):
        """
        Set the value associated with the key using indexing.

        Args:
            key: The key to set.
            value: The value to associate with the key.
        """
        self.set(key, value)

    def __delitem__(self, key):
        """
        Remove the key-value pair associated with the key using indexing.

        Args:
            key: The key to remove.
        """
        self.remove(key)

    def __contains__(self, key):
        """
        Check if the key exists in the hashtable using 'in' operator.

        Args:
            key: The key to check for existence.
        Returns:
            True if key exists, False otherwise.
        """
        return self.key_exists(key)
    
    def pop(self, key, default=None):
        """
        Remove specified key and return the value.
        If key is not found, return default.
        """
        bucket = self.hash_function(key)
        for i, kvpair in enumerate(self.array[bucket]):
            if kvpair and kvpair[0] == key:
                value = kvpair[1]
                del self.array[bucket][i]
                self.count -= 1
                return value
        return default
        
    def enumerate(self):
        """
        Return the enumeration of key-value pairs in the hashtable.

        Returns:
            Enumeration of key-value pairs.
        """
        pairs = []
        for bucket in self.array:
            for chain_link in bucket:
                pairs.append(chain_link)
        return enumerate(pairs)
    
    def __eq__(self, other):
        """
        Compare this hashtable to another for equality.

        Args:
            other: The object to compare with.

        Returns:
            True if both are HashTable instances and their key-value pairs are equal, False otherwise.
        """
        if not isinstance(other, HashTable):
            return False
        def to_dict(ht):
            d = {}
            for bucket in ht.array:
                for chain_link in bucket:
                    d[chain_link[0]] = chain_link[1]
            return d
        return to_dict(self) == to_dict(other)
    
    def __iter__(self):
        """
        Iterate over all keys in the hashtable.
        """
        for bucket in self.array:
            for chain_link in bucket:
                yield chain_link[0]