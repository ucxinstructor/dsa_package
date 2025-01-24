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
        
    def hash_function(self, key: str) -> int:
        """ 
        Return a hash value based on a given key. 

        Args:
            key: The key to convert to a hashvalue.
        Returns:
            Hash value modded to the hashtable capacity.
        """
        mult = 31
        hash_val = 0
        for character in key:
            hash_val *= mult
            hash_val += ord(character)
            hash_val %= (2**32)

        return hash_val % self.capacity
        
    def key_exists(self, key: str) -> bool:
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

    def set(self, key: str, value):
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

    def get(self, key: str):
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

    def delete(self, key: str):
        """ 
        Delete key-value pair if specified key is found. 

        Args:
            key: The key to check for.
        """
        bucket = self.hash_function(key)

        for i in range(len(self.array[bucket])):
            kvpair = self.array[bucket][i]
            if kvpair and kvpair[0] == key:
                del self.array[bucket][i]
                self.count -= 1
                break
    
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

