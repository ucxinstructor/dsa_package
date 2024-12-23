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
        Initialize the array with optional contents and a fixed capacity.

        Args:
            contents: an optional iterable to fill array with default values
            capacity: the initial size of the array (default is 10)
        """
        self._array = [ None ] * capacity
        #: number of elements currently in array
        self.count = 0

        if contents:
            self.extend(contents)
        
    def append(self, element):
        """
        Append an element to the array. Raise an exception if capacity is exceeded.

        Args:
            element: the element to append
        
        Raises:
            Exception: If the array is full.
        """
        if self.count >= self.capacity():
            raise Exception(f"Capacity Error: Maximum capacity {len(self)} reached.")

        self._array[self.count] = element
        self.count += 1

    def extend(self, array):
        """ 
        Append multiple elements from a given array.  
        
        Args:
            array: an iterable containing elements to append

        Raises:
            Exception: If appending the elements exceeds the array's capacity.
        """
        for e in array:
            self.append(e)

    def insert(self, index: int, element):
        """ 
        Insert an element at a specified index, shifting existing elements to the right.

        Args:
            index: the index at which to insert the element
            element: the element to insert

        Raises:
            IndexError: If the index is out of bounds.        
        """
        if index < 0 or index >= self.count:
            raise IndexError

        self.shift_right(self.count, index)
        self._array[index] = element
        self.count += 1
        
    def shift_right(self, start: int, end: int):
        """
        Helper method to shift elements to the right between the specified range.

        Args:
            start: the starting index of the shift
            end: the ending index of the shift
        """
        for i in range(start, end, -1):
            self._array[i] = self._array[i - 1]

    def delete(self, index: int):
        """  
        Delete an element at a specified index, shifting subsequent elements to the left.

        Args:
            index: the index of the element to delete

        Raises:     
            IndexError: If index is out of bounds.        
        """
        if index < 0 or index >= self.count:
            raise IndexError

        self.shift_left(index, self.count)
        self.count -= 1

    def shift_left(self, start: int, end: int):
        """
        Helper method to shift elements to the left between the specified range.

        Args:
            start: The starting index of the shift.
            end: The ending index of the shift.
        """
        for i in range(start, end):
            self._array[i] = self._array[i + 1]

    def __getitem__(self, index: int):
        """
        Retrieve the element at the specified index.

        Args:
            index: The index of the element.

        Returns:
            The element at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        return self._array[index]
            
    def __setitem__(self, index: int, value):
        """
        Set a new value at the specified index.

        Args:
            index: The index at which to set the value.
            value: The new value to assign.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        self._array[index] = value
        
    def __len__(self):
        """ 
        Return the number of elements in the array.

        Returns:
            The number of elements in the array.
        """
        return self.count
    
    def is_empty(self) -> bool:
        """ 
        Check if the array is empty.

        Returns:
            True if the array is empty, False otherwise.
        """
        return self.count == 0

    def capacity(self) -> int:
        """ 
        Get the total capacity of the array.

        Returns:
            The capacity of the array.
        """
        return len(self._array)
    
    def to_list(self) -> list:
        """ 
        Convert the array's elements to a standard Python list.

        Returns:
            A list containing the elements of the array.
        """
        return self._array[:self.count]

    @classmethod
    def from_list(cls, mylist: list):
        """
        Create an array from a standard Python list.

        Args:
            mylist: A Python list to initialize the array.

        Returns:
            An instance of the Array class.
        """        
        list_instance = cls()
        list_instance.extend(mylist)
 
        return list_instance

    def __repr__(self):
        """
        Represent the array's contents, count, and capacity.

        Returns:
            A string representation of the array.
        """
        return f'{self.to_list()} Count: {self.count} Capacity: {self.capacity()}'

class DynamicArray(Array):
    """ 
    A dynamic array implementation. Capacity will adjust as needed.

    Special Methods:

        Index Operator: 
            array[index]
    
        Assignment: 
            array[index] = value
    """

    def grow(self):
        """ 
        Helper method to double the capacity of the current array.
        """
        new_size = len(self._array) * 2
        new_array = [ None ] * new_size

        # copy elements
        for i in range(len(self._array)):
            new_array[i] = self._array[i]

        self._array = new_array

    def shrink(self):
        """ 
        Helper method to halve the capacity of the current array.
        """
        new_size = len(self._array) // 2
        new_array = [ None ] * new_size
        
        # copy elements
        for i in range(new_size):
            new_array[i] = self._array[i]

        self._array = new_array

    def check_capacity(self):
        """ 
        if count >= capacity, grow the array.
        if count <= 1/4 of capacity, shrink the array.
        """
        if self.count >= len(self._array):
            self.grow()
        elif self.count * 4 <= len(self._array):
            self.shrink()

    def append(self, element):
        """
        Append an element to the array. Adjust the capacity as needed.

        Args:
            element: The element to append.
        """
        self.check_capacity()

        self._array[self.count] = element
        self.count += 1

    def extend(self, array):
        """ 
        Append multiple elements from a given array.  Adjust the capacity as needed.
        
        Args:
            array: An iterable containing elements to append.
        """
        for e in array:
            self.append(e)

    def insert(self, index: int, element):
        """  
        Insert an element at a specified index, shifting existing elements to the right. Adjust the capacity as needed.

        Args:
            index: The index at which to insert the element.
            element: The element to insert.
        """
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_right(self.count, index)
        self._array[index] = element
        self.count += 1
        
    def delete(self, index: int):
        """  
        Delete an element at a specified index, shifting subsequent elements to the left. Adjust the capacity as needed.

        Args:
            index: The index of the element to delete.
        """
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_left(index, self.count)
        self.count -= 1

        
