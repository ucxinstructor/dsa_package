""" Module containing stack classes. """

class Stack:
    """ 
    A static stack implementation.
    """
    def __init__(self, capacity: int=10):
        """ 
        Initialize the stack with a given capacity.

        Args:
            capacity (int): The initial size of the stack (defaults to 10).
        """
        self._array = [None] * capacity
        #: number of elements in stack
        self.count = 0
    
    def push(self, element):
        """
        Push an element into the stack. Raise Exception when trying to push more elements than the capacity.

        Args:
            element: The element to push.
        Raises:
            Exception: When the capacity is reached.
        """
        if len(self) >= len(self._array):
            raise Exception("Capacity Reached")
        self.count += 1
        self._array[self.top()] = element
        
    def pop(self):
        """
        Pop an element from the stack. Raise Exception when there are no elements to pop.

        Returns:
            The top element in the stack.
        
        Raises:
            Exception: When the stack is empty.
        """
        if self.is_empty():
            raise Exception("Empty Stack")
        element = self._array[self.top()]
        self.count -= 1
        return element
    
    def peek(self):
        """
        Return the element from the top of the stack. Raise Exception if stack is empty.

        Returns:
            The top element in the stack.
        
        Raises:
            Exception: When the stack is empty. 
        """
        if self.is_empty():
            raise Exception("Empty Stack")
        return self._array[self.top()]
    
    def __len__(self):
        """
        Return the number of elements in the stack.
        """
        return self.count
    
    def is_empty(self):
        """
        Return a Boolean on whether the stack is empty or not.
        """
        return self.count == 0
    
    def top(self):
        """
        Return the top index of the stack. 
        """
        return self.count - 1

    def capacity(self):
        """
        Return the capacity of the stack. 
        """
        return len(self._array)

    @classmethod
    def from_list(cls, alist: list):
        """
        Set the contents of a stack from a list. Raise Exception when trying to push more elements than the capacity.

        Args:
            alist: The list with contents to set as an array.
        """
        st = cls()
        for e in alist:
            st.push(e)
        return st

    def to_list(self):
        """
        Return the contents of the stack as an array.
        """
        return self._array[:self.count]

    def __repr__(self):
        """
        Return a string representation of the stack.
        """
        return f"{self._array[0:self.count]} Top: {self.top()} Capacity: {self.capacity()}"

    def __eq__(self, other):
        """
        Compare two stacks (static/dynamic) for value-based equality.

        Returns:
            True if both are Stack or DynamicStack instances and their contents are equal.
            For non-stack types, returns NotImplemented.
        """
        if isinstance(other, (Stack, DynamicStack)):
            return self.to_list() == other.to_list()
        return NotImplemented
    
    
class DynamicStack(Stack):
    """ 
    A dynamic stack implementation.
    """
    def grow(self):
        """ 
        Helper method to double the capacity of the current array. 
        """
        new_array = [ None ] * len(self._array) * 2
        
        # copy elements
        for i, e in enumerate(self._array):
            new_array[i] = e

        self._array = new_array

    def shrink(self):
        """ 
        Helper method to halve the capacity of the current array.
        """
        if self.capacity() < 10:
            return

        new_capacity = self.capacity() // 2
        new_array = [ None ] * new_capacity
        
        # copy elements
        for i in range(new_capacity):
            new_array[i] = self._array[i]

        self._array = new_array


    def check_capacity(self):
        """
        Check the capacity of the stack. 
        If count >= capacity, grow the array
        If count <= 1/4 of capacity, shrink the array
        """
        if self.count >= self.capacity():
            self.grow()
        elif self.count * 4 <= self.capacity():
            self.shrink()
        
    def push(self, element):
        """
        Push an element into the stack. Automatically grows array if capacity needs to increase.

        Args:
            element: The element to push.

        Returns:
            None
        """
        self.check_capacity()
        super().push(element)
        
    def pop(self):
        """
        Return an element from the stack. Automatically shrinks array if capacity is 4x the count.

        Returns:
            The top element in the stack.

        Raises:
            Exception: When the stack is empty.
        """
        self.check_capacity()
        return super().pop()
