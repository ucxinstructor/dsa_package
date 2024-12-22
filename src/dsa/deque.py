""" Module containing deque classes. """

class Deque:
    """ 
    A static deque implementation.
    """
    def __init__(self, capacity=10):
        """ 
        Args:
            capacity: the initial size of the stack (defaults to 10)
        """
        self._array = [None] * capacity
        self._left = -1
        self._right = 0
        self.count = 0
        
    def append_left(self, element):
        """
        Append an element to the right of a deque. Raise Exception when trying to append more elements than the capacity.

        Args:
            element: the element to append
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
        Append an element to the right of a deque. Raise Exception when trying to append more elements than the capacity.

        Args:
            element: the element to append
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
        Pop an element from the left of the deque. Raise Exception when there are no elements to pop.

        Returns:
            the leftmost element of the deque
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
        Pop an element from right the deque. Raise Exception when there are no elements to pop.

        Returns:
            the rightmost element of the deque
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
        Return the element from the left of the deque. Raise Exception if deque is empty.
        """
        if self.is_empty():
            raise Exception("Empty deque")
        return self._array[self._left + 1]

    def peek_right(self):
        """
        Return the element from the right of the deque. Raise Exception if deque is empty.
        """
        if self.is_empty():
            raise Exception("Empty deque")
        return self._array[self._right - 1]
    
    def is_empty(self):
        """
        Return a Boolean on whether the deque is empty or not.
        """
        return self.count == 0

    @classmethod
    def from_list(cls, alist: list):
        """
        Set the contents of a queue into an array. Raise Exception when trying to enqueue more elements than the capacity.

        Args:
            alist: the list with contents to enqueue
        """
        dq = cls()
        for e in alist:
            dq.append_right(e)
        return dq

    def to_list(self):
        """
        Return the contents of the queue as an array.
        """
        arr = []
        for i in range(self.count):
            index = (i + self._left + 1) % len(self._array) 
            arr.append(self._array[index])
        return arr

    def capacity(self):
        """
        Return the capacity of the deque.
        """
        return len(self._array)
    
    def __len__(self):
        """
        Return the number of elements in the deque
        """
        return self.count
    
    def __repr__(self):
        arr = []
        for i in range(self.count):
            index = (i + self._left + 1) % len(self._array) 
            arr.append(str(self._array[index]))
        arrstr = ", ".join(arr)
        return f"[{arrstr}] Count: {self.count} Capacity: {len(self._array)}" # {self.array}"
    
class DynamicDeque(Deque):
    """ 
    A dynamic deque implementation.
    """
    def grow(self):
        """ 
        double the capacity of the current array 
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
        halve the capacity of the current array 
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
        if count >= capacity, grow the array
        if count <= 1/4 of capacity, shrink the array
        """
        if self.count >= self.capacity():
            self.grow()
        elif self.count * 4 <= self.capacity():
            self.shrink()
        
    def append_left(self, element):
        """
        Append an element into the dequeue. Automatically grows array if capacity needs to increase.

        Args:
            element: the element to append
        """
        self.check_capacity()
        super().append_left(element)
        
    def append_right(self, element):
        """
        Append an element into the dequeue. Automatically grows array if capacity needs to increase.

        Args:
            element: the element to append
        """
        self.check_capacity()
        super().append_right(element)

    def pop_left(self):
        """
        Return an element from the left dequeue. Automatically shrinks array if capacity is 4x the count.
        """
        self.check_capacity()
        return super().pop_left()


    def pop_right(self):
        """
        Return an element from the right dequeue. Automatically shrinks array if capacity is 4x the count.
        """
        self.check_capacity()
        return super().pop_right()
