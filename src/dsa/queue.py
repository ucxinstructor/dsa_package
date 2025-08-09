""" Module containing queue classes. """
from dsa.array import CircularArray

class Queue:
    """ 
    A static queue implementation. 
    """
    def __init__(self, contents=None, capacity: int=10):
        """ 
        Initialize the queue with a given capacity.

        Args:
            contents: The list with contents to enqueue.
            capacity: The initial size of the stack (defaults to 10).
        """
        self._array = [None] * capacity
        self._front = 0
        #: number of elements in queue
        self.count = 0

        if contents:
            for e in contents:
                self.enqueue(e)
    
    def enqueue(self, element):
        """
        Enqueue an element into the queue. Raise Exception when trying to enqueue more elements than the capacity.

        Args:
            element: The element to enqueue.

        Raises:
            Exception: When trying to enqueue more elements than the capacity.

        Returns:
            None
        """
        if self.count >= len(self._array):
            raise Exception("Capacity Reached")

        index = (self._front + self.count) % len(self._array)
        self._array[index] = element
        self.count += 1
        
    def dequeue(self):
        """
        Dequeue an element from the queue. Raise Exception when there are no elements to dequeue.

        Raises:
            Exception: When there are no elements to dequeue.

        Returns:
            The from element in the queue.
        """
        if self.is_empty():
            raise Exception("Empty Queue")

        element = self._array[self._front]
        self._front += 1
        if self._front >= len(self._array):
            self._front = 0
        self.count -= 1

        return element
    
    def peek(self):
        """
        Return the element in front of the queue. Raise Exception if queue is empty.

        Returns:
            The element in front of the queue.

        Raises:
            Exception: When the queue is empty.
        """
        if self.is_empty():
            raise Exception("Empty Queue")

        return self._array[self._front]

    def is_empty(self):
        """
        Return a Boolean on whether the stack is empty or not.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.count == 0
    
    def capacity(self):
        """
        Return the capacity of the queue.

        Returns:
            The capacity of the queue.
        """
        return len(self._array)
    
    @classmethod
    def from_list(cls, alist):
        """
        Set the contents of a queue into an array. Raise Exception when trying to enqueue more elements than the capacity.

        Args:
            alist: The list with contents to enqueue.

        Returns:
            The queue with the contents of the list.
        """
        q = cls()
        for e in alist:
            q.enqueue(e)
        return q

    def to_ordered_list(self) -> list:
        """
        Return the contents of the queue as a Python list.

        Returns:
            The contents of the queue as a Python list.
        """
        if self._front + self.count <= len(self._array):
            return self._array[self._front:self._front + self.count]
        else:
            end_part = self._array[self._front:]
            start_part = self._array[:self._front + self.count - len(self._array)]
            return end_part + start_part
        
    def raw_view(self):
        """
        Return the queue in its array representation.

        Returns:
            The array representation of the queue.
        """
        return self._array

    def __repr__(self):
        """
        Return a string with details of the queue.

        Returns:
            A string with details of the queue.
        """
        ordered_list = self.to_ordered_list()
        # arr = []
        # for i in range(self.count):
        #     index = (i + self._front) % len(self._array)
        #     arr.append(str(self._array[index]))
        arrstr = ", ".join([str(e) for e in ordered_list])
        return f"[{arrstr}] count: {self.count} Capacity: {self.capacity()}"
    
    def __len__(self):
        """
        Return the count of items in the queue.

        Returns:
            The count of items in the queue.
        """
        return self.count

    def __eq__(self, other):
        """
        Compare two queues (static/dynamic/circular) for value-based equality.

        Returns:
            True if both are Queue, DynamicQueue, or CircularQueue instances and their contents are equal.
            For non-queue types, returns NotImplemented.
        """
        if isinstance(other, (Queue, DynamicQueue, CircularQueue)):
            def _as_list(obj):
                # Queue/DynamicQueue expose to_ordered_list; CircularQueue exposes to_list
                if hasattr(obj, 'to_ordered_list'):
                    return obj.to_ordered_list()
                if hasattr(obj, 'to_list'):
                    return obj.to_list()
                return None
            return _as_list(self) == _as_list(other)
        return NotImplemented
    

class DynamicQueue(Queue):
    """ 
    A dynamic queue implementation. Note that shrink is not impelmented.
    """
    def __init__(self, contents=None, capacity: int=10):
        """
        Initialize the queue with a given capacity.
        
        Args:
            contents: The list with contents to enqueue.
            capacity: The initial size of the stack (defaults to 10).
        """
        super().__init__(contents, capacity)
    
    def grow(self):
        """ 
        Double the capacity of the current array.

        Returns:
            None
        """
        new_array = [ None ] * len(self._array) * 2
        
        # copy elements
        for i in range(self.count):
            new_array[i] = self._array[i + self._front]
        self._front = 0
        self._array = new_array

    def check_capacity(self):
        """ 
        If count >= capacity, grow the array.

        Returns:
            None
        """
        if self._front + self.count >= len(self._array):
            self.grow()

    def enqueue(self, element):
        """
        Enqueue an element into the queue. Increae capacity if count is greater than the capacity.

        Args:
            element: the element to enqueue

        Returns:
            None
        """
        self.check_capacity()
        index = self._front + self.count
        self._array[index] = element
        self.count += 1

class CircularQueue(CircularArray):
    """ 
    A circular queue implementation. 
    """
    def __init__(self, contents=None, capacity: int=10):
        """
        Initialize the queue with a given capacity.

        Args:
            contents: The list with contents to enqueue.
            capacity: The initial size of the stack (defaults to 10).
        """
        super().__init__(None, capacity)
        # self._start is equivalent to the queue's front index

        if contents:
            for e in contents:
                self.enqueue(e)

    def enqueue(self, element):
        """
        Enqueue an element into the queue. Wrap around when trying to enqueue more elements than the capacity.

        Args:
            element: The element to enqueue.

        Returns:
            None
        """
        return super().append(element)

    def dequeue(self):
        """
        Dequeue an element from the queue. Raise Exception when there are no elements to dequeue.

        Raises:
            Exception: When there are no elements to dequeue.

        Returns:
            The from element in the queue.
        """
        if self.is_empty():
            raise Exception("Empty Queue")

        element = self._array[self._start]
        self._start = (self._start + 1) % len(self._array)
        self.count -= 1
        return element

    def peek(self):
        """
        Return the element in front of the queue. Raise Exception if queue is empty.

        Returns:
            The element in front of the queue.

        Raises:
            Exception: When the queue is empty.
        """
        if self.is_empty():
            raise Exception("Empty Queue")

        return self._array[self._start]
