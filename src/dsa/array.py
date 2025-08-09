""" Module containing array classes. """

class Array:
    """
    A static array implementation.

    Special Methods:
        Index Operator: array[index]
        Assignment: array[index] = value

    Equality:
        Array instances can be compared for equality with other Array or DynamicArray instances (but not CircularArray), based on their contents.
    """
    def __init__(self, contents=None, capacity: int=10):
        """ 
        Initialize the array with optional contents and a fixed capacity.

        Args:
            contents: An optional iterable to fill array with default values.
            capacity (int): The initial size of the array (default is 10)
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
            element: The element to append.
        
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
            array: An iterable containing elements to append.

        Raises:
            Exception: If appending the elements exceeds the array's capacity.
        """
        for e in array:
            self.append(e)

    def insert(self, index: int, element):
        """ 
        Insert an element at a specified index, shifting existing elements to the right.

        Args:
            index (int): The index at which to insert the element.
            element: The element to insert.

        Raises:
            IndexError: If the index is out of bounds.        
        """
        if index == self.count:
            self.append(element)
            return

        if index < 0 or index > self.count:
            raise IndexError

        self.shift_right(index)
        self._array[index] = element
        self.count += 1
        
    def shift_right(self, start: int):
        """
        Helper method to shift elements to the right from a specified start index until the last element.
        (May delete an element but does not affect the count.)
        Args:
            start (int): The index at which to start shifting (inclusive).

        Raises:
            Exception: If the array is full and cannot accommodate the shift.
        """
        if self.count >= len(self._array):
            raise Exception(f"Capacity Error: Maximum capacity {len(self)} reached.")
        end = self.count
        for i in range(end, start, -1):
            self._array[i] = self._array[i - 1]

    def delete(self, index: int):
        """  
        Delete an element at a specified index, shifting subsequent elements to the left.

        Args:
            index (int): The index of the element to delete.

        Raises:     
            IndexError: If index is out of bounds.        
        """
        if index < 0 or index >= self.count:
            raise IndexError

        self.shift_left(index)
        self.count -= 1

    def shift_left(self, start: int):
        """
        Helper method to shift elements to the left starting at a start index.
        (May delete an element but does not affect the count.)

        Args:
            start (int): The starting index of the shift.
        """
        for i in range(start, self.count - 1):
            self._array[i] = self._array[i + 1]

    def __getitem__(self, index: int):
        """
        Retrieve the element at the specified index.

        Args:
            index (int): The index of the element.

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
            index (int): The index at which to set the value.
            value: The new value to assign.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        self._array[index] = value
        
    def __len__(self) -> int:
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

    def __eq__(self, other):
        """
        Compare this array to another for equality.

        Args:
            other: The object to compare with.

        Returns:
            True if both objects are Array, DynamicArray, or CircularArray instances and their contents are equal.
            For non-array types, returns NotImplemented to allow reverse comparison.
        """
        if isinstance(other, (Array, DynamicArray, CircularArray)):
            return self.to_list() == other.to_list()
        return NotImplemented
    
class DynamicArray(Array):
    """
    A dynamic array implementation. Capacity will adjust as needed.

    Special Methods:
        Index Operator: array[index]
        Assignment: array[index] = value

    Equality:
        DynamicArray instances can be compared for equality with other DynamicArray or Array instances (but not CircularArray), based on their contents.
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
            index (int): The index at which to insert the element.
            element: The element to insert.
        """
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_right(index)
        self._array[index] = element
        self.count += 1
        
    def delete(self, index: int):
        """  
        Delete an element at a specified index, shifting subsequent elements to the left. Adjust the capacity as needed.

        Args:
            index (int): The index of the element to delete.
        """
        if index >= self.count or index < 0:
            raise IndexError

        self.check_capacity()

        self.shift_left(index)
        self.count -= 1

        
class CircularArray(Array):
    """ 
    A circular array implementation.

    Special Methods:

        Index Operator: 
            array[index]
    
        Assignment: 
            array[index] = value
    """
    def __init__(self, contents=None, capacity: int=10):
        """ 
        Initialize the circular array with optional contents and a fixed capacity.

        Args:
            contents: An optional iterable to fill array with default values.
            capacity (int): The initial size of the array (default is 10)
        """
        super().__init__(None, capacity)
        #: index of the first element in the circular array
        self._start = 0
        if contents:
            self.extend(contents)
        
    def __getitem__(self, index: int):
        """
        Retrieve the element at the specified index.

        Args:
            index (int): The index of the element.

        Returns:
            The element at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        return self._array[(self._start + index) % len(self._array)]
            
    def __setitem__(self, index: int, value):
        """
        Set a new value at the specified index.

        Args:
            index (int): The index at which to set the value.
            value: The new value to assign.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count: 
            raise IndexError
        self._array[(self._start + index) % len(self._array)] = value

    def append(self, element):
        """
        Append an element to the circular array. If appending exceeds capacity, it will wrap around to the oldest element.

        Args:
            element: The element to append.
        """
        # self._array[(self._start + self.count) % len(self._array)] = element
        # if self.count < self.capacity():
        #     self.count += 1
        # else:
        #     self._start = (self._start + 1) % len(self._array)
        index = (self._start + self.count) % len(self._array)
        self._array[index] = element

        if self.count < self.capacity():
            self.count += 1
        else:
            self._start = (self._start + 1) % len(self._array)  # Overwrite oldest element

    def raw_view(self):
        """ 
        Return a raw view of the array.

        Returns:
            A raw view of the array.
        """
        return self._array

    def to_list(self):
        """ 
        Convert the array's elements to a standard Python list.

        Returns:
            A list containing the elements of the array.
        """
        output_list = []
        for i in range(self.count):
            output_list.append(self._array[(self._start + i) % len(self._array)])
        return output_list

    def insert(self, index: int, element):
        """
        Insert an element at a specified index, shifting existing elements to the right.

        Args:
            index (int): The index at which to insert the element.
            element: The element to insert.

        Raises:
            IndexError: If the index is out of bounds.
            Exception: If the array is full.
        """
        if index < 0 or index > self.count:
            raise IndexError
        if self.count >= self.capacity():
            raise Exception(f"Capacity Error: Maximum capacity {self.capacity()} reached.")
        # Shift elements to the right
        for i in range(self.count, index, -1):
            self._array[(self._start + i) % self.capacity()] = self._array[(self._start + i - 1) % self.capacity()]
        self._array[(self._start + index) % self.capacity()] = element
        self.count += 1


    def delete(self, index: int):
        """
        Delete an element at a specified index, shifting subsequent elements to the left.

        Args:
            index (int): The index of the element to delete.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count:
            raise IndexError
        # Shift elements to the left
        for i in range(index, self.count - 1):
            self._array[(self._start + i) % self.capacity()] = self._array[(self._start + i + 1) % self.capacity()]
        self.count -= 1
