""" Module containing deque classes. """

class Deque:
    """ 
    A static deque implementation that supports appending and popping elements 
    from both ends, with a fixed capacity.
    """
    def __init__(self, capacity: int=10):
        """ 
        Initialize a deque with a fixed capacity.

        Args:
            capacity (int): The initial size of the deque (default is 10).
        """
        self._array = [None] * capacity
        self._left = -1
        self._right = 0
        self.count = 0
        
    def push_front(self, element):
        """
        Push an element at the front of the deque. (synonym for append_left)
        Raises an exception when the deque is full.

        Args:
            element: The element to append.

        Raises:
            Exception: If the deque is full.
        """
        self.append_left(element)

    def push_back(self, element):
        """
        Push an element at the back of the deque. (synonym for append_right)
        Raises an exception when the deque is full.

        Args:
            element: The element to append.

        Raises:
            Exception: If the deque is full.
        """
        self.append_right(element)

    def pop_front(self):
        """
        Pop an element from the front of the deque. (synonym for pop_left)
        Raises an exception if the deque is empty.

        Returns:
            The leftmost element of the deque.

        Raises:
            Exception: If the deque is empty.
        """
        return self.pop_left()

    def pop_back(self):
        """
        Pop an element from the back of the deque. (synonym for pop_right)
        Raises an exception if the deque is empty.

        Returns:
            The rightmost element of the deque.

        Raises:
            Exception: If the deque is empty.
        """
        return self.pop_right() 
    
    def front(self):
        """
        Get the element at the front of the deque without removing it.
        Raises an exception if the deque is empty.

        Returns:
            The leftmost element.

        Raises:
            Exception: If the deque is empty.
        """
        return self.peek_left()
    
    def back(self):
        """
        Get the element at the back of the deque without removing it.
        Raises an exception if the deque is empty.

        Returns:
            The rightmost element.

        Raises:
            Exception: If the deque is empty.
        """
        return self.peek_right()

    def append_left(self, element):
        """
        Append an element to the left of the deque. Raises an exception when the deque is full.

        Args:
            element: The element to append.

        Raises:
            Exception: If the deque is full.
        """
        if self.count >= self.capacity():
            raise Exception("Deque Full")
        if self._left < 0:
            self._left = self.capacity() - 1
        self._array[self._left] = element
        self._left -= 1
        self.count += 1
        
    def append_right(self, element):
        """
        Append an element to the right of the deque. Raises an exception when the deque is full.

        Args:
            element: The element to append.

        Raises:
            Exception: If the deque is full.
        """
        if self.count >= self.capacity():
            raise Exception("Deque Full")
        if self._right > self.capacity() - 1:
            self._right = 0
        self._array[self._right] = element
        self._right += 1
        self.count += 1

    def pop_left(self):
        """
        Remove and return the element from the left of the deque. Raises an exception if the deque is empty.

        Returns:
            The leftmost element of the deque.

        Raises:
            Exception: If the deque is empty.
        """
        if self.is_empty():
            raise Exception("Empty Deque")

        element = self._array[self._left + 1]
        self._left += 1
        if self._left + 1 >= len(self._array):
            self._left = -1
        self.count -= 1
        return element
    
    def pop_right(self):
        """
        Pop an element from right the deque. Raise an exception if the deque is empty.

        Returns:
            The rightmost element of the deque.

        Raises:
            Exception: If the deque is empty.
        """
        if self.is_empty():
            raise Exception("Empty Deque")
        element = self._array[self._right - 1]
        self.count -= 1

        self._right -= 1
        if self._right < 0:
            self._right = len(self._array) - 1
        return element

    def peek_left(self):
        """
        Get the element at the left of the deque without removing it.
        Raises an exception if the deque is empty.

        Returns:
            The leftmost element.

        Raises:
            Exception: If the deque is empty.
        """
        if self.is_empty():
            raise Exception("Empty deque")
        return self._array[self._left + 1]

    def peek_right(self):
        """
        Get the element at the right of the deque without removing it.
        Raises an exception if the deque is empty.

        Returns:
            The rightmost element.

        Raises:
            Exception: If the deque is empty.
        """
        if self.is_empty():
            raise Exception("Empty deque")
        return self._array[self._right - 1]
    
    def is_empty(self) -> bool:
        """
        Return a Boolean on whether the deque is empty or not.
        """
        return self.count == 0

    @classmethod
    def from_list(cls, alist: list):
        """
        Create a deque from a given list. Raises an exception if list exceeds the deque's capacity.

        Args:
            alist: The list to initialize the deque with.

        Returns:
            a deque instance with elements from the list.

        Raises:
            Exception: If list exceeds the deque's capacity.
        """
        dq = cls()
        for e in alist:
            dq.append_right(e)
        return dq

    def to_list(self):
        """
        Convert the deque's contents into a list.

        Returns:
            A list containg the elements in the deque.
        """
        arr = []
        for i in range(self.count):
            index = (i + self._left + 1) % len(self._array) 
            arr.append(self._array[index])
        return arr

    def capacity(self) -> int:
        """
        Get the maximum capacity of the deque.

        Returns:
            The capacity of the deque.
        """
        return len(self._array)
    
    def __len__(self) -> int:
        """
        Get the number of elements in the deque.

        Returns:
            The count of elements.
        """
        return self.count
    
    def __repr__(self):
        """
        String representation of the deque for debugging purposes.

        Returns:
            A string displaying the contents and size of the deque.
        """
        arr = []
        for i in range(self.count):
            index = (i + self._left + 1) % len(self._array) 
            arr.append(str(self._array[index]))
        arrstr = ", ".join(arr)
        return f"[{arrstr}] Count: {self.count} Capacity: {len(self._array)}" # {self.array}"

    def __eq__(self, other):
        """
        Compare two deques (static/dynamic) for value-based equality.

        Returns:
            True if both are Deque or DynamicDeque instances and their contents are equal.
            For non-deque types, returns NotImplemented.
        """
        if isinstance(other, (Deque, DynamicDeque)):
            return self.to_list() == other.to_list()
        return NotImplemented
    
class DynamicDeque(Deque):
    """ 
    A dynamic deque implementation that adjusts its capacity as needed.
    """
    def grow(self):
        """ 
        Helper method to double the capacity of the deque.
        """
        new_array = [ None ] * self.capacity() * 2
        
        # copy elements
        for i in range(self.count):
            index = (i + self._left + 1) % len(self._array) 
            new_array[i] = self._array[index]

        self._array = new_array
        self._left = -1
        self._right = self.count

    def shrink(self):
        """ 
        Helper method to halve the capacity of the deque. 
        """
        if self.capacity() < 10:
            return

        new_capacity = self.capacity() // 2
        new_array = [ None ] * new_capacity
        
        # copy elements
        for i in range(self.count):
            index = (i + self._left + 1) % len(self._array) 
            new_array[i] = self._array[index]

        self._array = new_array
        self._left = -1
        self._right = self.count


    def check_capacity(self):
        """ 
        Helper method to adjust the capacity of the deque based on its count:
        if count >= capacity, grow the deque
        if count <= 1/4 of capacity, shrink the deque
        """
        if self.count >= self.capacity():
            self.grow()
        elif self.count * 4 <= self.capacity():
            self.shrink()
        
    def append_left(self, element):
        """
        Append an element to the left, adjusting capacity if needed.

        Args:
            element: The element to append.
         """
        self.check_capacity()
        super().append_left(element)
        
    def append_right(self, element):
        """
        Append an element to the right, adjusting capacity if needed.

        Args:
            element: The element to append.
        """
        self.check_capacity()
        super().append_right(element)

    def pop_left(self):
        """
        Remove and return the element from the left, adjusting capacity if needed.

        Returns:
            The leftmost element.
        """
        self.check_capacity()
        return super().pop_left()


    def pop_right(self):
        """
        Remove and return the element from the right, adjusting capacity if needed.

        Returns:
            The rightmost element.
        """
        self.check_capacity()
        return super().pop_right()
    