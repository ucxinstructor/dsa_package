""" Module containing array classes. """

class Array:
    """ 
    A static array implementation.

    Special Methods:

        Index Operator: 
            array[index]
    
        Assignment: 
            array[index] = value
    """
    def __init__(self, contents=None, capacity=10):
        """ 
        Args:
            contents: optional container to fill array with default values
            capacity: the initial size of the array (defaults to 10)
        """
        self._array = [ None ] * capacity
        #: number of elements in array
        self.count = 0

        if contents:
            self.extend(contents)
        
    def append(self, element):
        """
        Append an element. Raise Exception when trying to append more elements than the capacity.

        Args:
            element: the element to append
        """
        if self.count >= self.capacity():
            raise Exception(f"Capacity Error: {len(self)} maximum")

        self._array[self.count] = element
        self.count += 1

    def extend(self, array):
        """ 
        Append each element from a given array. Raise Exception when trying to add more elements than the capacity.
        
        Args:
            array: contains elements to be appended
        """
        for e in array:
            self.append(e)

    def insert(self, index: int, element):
        """ 
        Insert an element at a specified index.  Raise IndexError if index is out of range.
        
        Args:
            index: index to insert an element
            element: the element to insert
        """
        if index < 0 or index >= self.count:
            raise IndexError

        self.shift_right(self.count, index)
        self._array[index] = element
        self.count += 1
        
    def shift_right(self, start: int, end: int):
        """
        a helper method to shift elements to the right

        Args:
            start: starting index of shift
            end: ending index of shift
        """
        for i in range(start, end, -1):
            self._array[i] = self._array[i - 1]

    def delete(self, index: int):
        """  
        Delete an element at a specified index. Raise IndexError if index is out of range.

        Args:
            index: index of the element to be deleted
        
        """
        if index >= self.count or index < 0:
            raise IndexError

        self.shift_left(index, self.count)
        self.count -= 1

    def shift_left(self, start: int, end: int):
        """
        a helper method to shift elements to the right

        Args:
            start: starting index of shift
            end: ending index of shift
        """
        for i in range(start, end):
            self._array[i] = self._array[i + 1]

    ### special methods for handling index operator
    def __getitem__(self, index: int):
        """
        Returns: 
            the element at the specified index of an array
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        return self._array[index]
            
    def __setitem__(self, index: int, value):
        """
        set a new value at the specified index of an array
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        self._array[index] = value
        
    ### special methods for len()
    def __len__(self):
        """ 
        Returns: 
            the count of an array
        """
        return self.count
    
    def is_empty(self) -> bool:
        """ 
        Returns:
            True if the array is empty
        """
        return self.count == 0

    def capacity(self) -> int:
        """ 
        Returns:
            the capacity of an array
        """
        return len(self._array)
    
    def to_list(self) -> list:
        """ 
        Returns:
            a python list with contents of this array
        """
        return self._array[:self.count]

    @classmethod
    def from_list(cls, mylist: list):
        ''' create an array from a list '''
        ll = cls()
        ll._array = mylist
        ll.count = len(mylist)

        return ll

    ### override the representation value with the Python interpreter
    def __repr__(self):
        """
        display the contents of the array
        """
        contents = self._array[:self.count]
        return f'{contents} Count: {self.count} Capacity: {self.capacity()}'

class DynamicArray(Array):
    """ 
    A dynamic array implementation.

    Special Methods:

        Index Operator: 
            array[index]
    
        Assignment: 
            array[index] = value
    """

    def grow(self):
        """ 
        double the capacity of the current array 
        """
        new_size = len(self._array) * 2
        new_array = [ None ] * new_size

        # copy elements
        for i in range(len(self._array)):
            new_array[i] = self._array[i]

        self._array = new_array

    def shrink(self):
        """ 
        halve the capacity of the current array 
        """
        new_size = len(self._array) // 2
        new_array = [ None ] * new_size
        
        # copy elements
        for i in range(new_size):
            new_array[i] = self._array[i]

        self._array = new_array

    def check_capacity(self):
        """ 
        if count >= capacity, grow the array
        if count <= 1/4 of capacity, shrink the array
        """
        if self.count >= len(self._array):
            self.grow()
        elif self.count * 4 <= len(self._array):
            self.shrink()

    def append(self, element):
        """
        Append an element. Raise Exception if trying to append more elements than the capacity.

        Args:
            element: the element to append

        """
        self.check_capacity()

        self._array[self.count] = element
        self.count += 1

    def extend(self, array):
        """ 
        Append each element from a given array. Raise Exception if trying to add more elements than the capacity.
        
        Args:
            array: contains elements to be appended
        """
        for e in array:
            self.append(e)

    def insert(self, index: int, element):
        """  
        Insert an element at a specified index. Raise IndexError if index is out of range.

        Args:
            index: index to insert an element
            element: the element to insert

        """
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_right(self.count, index)
        self._array[index] = element
        self.count += 1
        
    def delete(self, index: int):
        """  
        Delete an element at a specified index. Raise IndexError if index is out of range.

        Args:
            index: index of the element to be deleted
        
        """
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_left(index, self.count)
        self.count -= 1

        
