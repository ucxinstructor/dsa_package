""" Module containing queue classes. """

class Queue:
    """ 
    A static queue implementation. 
    """
    def __init__(self, capacity=10):
        """ 
        Args:
            capacity: the initial size of the stack (defaults to 10)
        """
        self._array = [None] * capacity
        self._front = 0
        #: number of elements in queue
        self.count = 0
    
    def enqueue(self, element):
        """
        Enqueue an element into the queue. Raise Exception when trying to enqueue more elements than the capacity.

        Args:
            element: the element to enqueue
        """
        if self.count >= len(self._array):
            raise Exception("Capacity Reached")

        index = (self._front + self.count) % len(self._array)
        self._array[index] = element
        self.count += 1
        
    def dequeue(self):
        """
        Dequeue an element from the queue. Raise Exception when there are no elements to dequeue.

        Returns:
            the from element in the queue
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
        """
        if self.is_empty():
            raise Exception("Empty Queue")

        return self._array[self._front]

    def is_empty(self):
        """
        Return a Boolean on whether the stack is empty or not.
        """
        return self.count == 0
    
    def capacity(self):
        """
        Return the capacity of the queue.
        """
        return len(self._array)
    
    @classmethod
    def from_list(cls, alist):
        """
        Set the contents of a queue into an array. Raise Exception when trying to enqueue more elements than the capacity.

        Args:
            alist: the list with contents to enqueue
        """
        q = cls()
        for e in alist:
            q.enqueue(e)
        return q

    def to_list(self):
        """
        Return the contents of the queue as an array.
        """
        return self._array[self._front: self._front + self.count]

    def __repr__(self):
        """
        Return a string with details of the queue.
        """
        arr = []
        for i in range(self.count):
            index = (i + self._front) % len(self._array)
            arr.append(str(self._array[index]))
        arrstr = ", ".join(arr)
        return f"[{arrstr}] count: {self.count} Capacity: {self.capacity()}"
    
    def __len__(self):
        """
        Return the count of items in the queue.
        """
        return self.count
    

class DynamicQueue(Queue):
    """ 
    A dynamic queue implementation. Note that shrink is not impelmented.
    """
    def __init__(self, capacity=10):
        super().__init__(capacity)
    
    def grow(self):
        """ 
        double the capacity of the current array 
        """
        new_array = [ None ] * len(self._array) * 2
        
        # copy elements
        for i in range(self.count):
            new_array[i] = self._array[i + self._front]
        self._front = 0
        self._array = new_array

    def check_capacity(self):
        """ 
        if count >= capacity, grow the array
        """
        if self._front + self.count >= len(self._array):
            self.grow()

    def enqueue(self, element):
        """
        Enqueue an element into the queue. Increae capacity if count is greater than the capacity.

        Args:
            element: the element to enqueue
        """
        self.check_capacity()
        index = self._front + self.count
        self._array[index] = element
        self.count += 1

