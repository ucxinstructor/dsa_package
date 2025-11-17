""" Module containing heap (max heap), min heap and priority queue classes. """
class Heap:
    """ 
    A max heap implementation.
    """
    def __init__(self):
        self._array = []

    @classmethod
    def from_list(cls, mylist: list):
        """
        Create a heap from a list of elements.
        Args:
            mylist (list): The list of elements to be inserted into the heap.
        Returns:
            Heap: An instance of the heap with all elements from the list inserted.
        """

        hp = cls()
        for e in mylist:
            hp.insert(e)

        return hp

    def raw_view(self) -> list:
        """
        Return the heap in its array representation.

        Returns:
            list: The list representation of the heap.
        """

        return self._array
    
    def root(self):
        """
        Get the root value.

        Returns:
            The root node's value. None if count is 0.
        """
        if self.count() == 0:
            return None

        return self._array[0]
    
    def peek(self):
        """
        Get the max value of the max heap.

        Returns:
            The maximum value of the max heap.
        """
        return self.root()

    def last(self):
        """
        Get the last node of the max heap.

        Returns:
            The last node's value. 
            None if count is 0.
        """
        if self.count() == 0:
            return None

        return self._array[-1] 
    
    def left_index(self, index: int) -> int:
        """
        Get the index of the left child.

        Args:
            index (int): The index of the node.

        Returns:
            Return the index of the left child.
        """
        return (index * 2) + 1

    def right_index(self, index: int) -> int:
        """
        Get the index of the right child.

        Args:
            index (int): The index of the node.

        Returns:
            Return the index of the right child.
        """
        return (index * 2) + 2

    def parent_index(self, index: int) -> int:
        """
        Get the index of the parent node.

        Args:
            index (int): The index of the node.  

        Returns:
            Return the index of the parent child.
        """
        return (index - 1) // 2
    
    def has_left(self, index: int) -> bool:
        """
        Check if current node has an left child.

        Args:
            index (int): The index of the node.

        Returns:
            Boolean on whether a node has a left child node.
        """
        return self.left_index(index) < self.count()
    
    def has_right(self, index: int) -> bool:
        """
        Check if current node has an right child.

        Args:
            index (int): The index of the node.  

        Returns:
            Boolean on whether a node has a right child node.
        """
        return self.right_index(index) < self.count()

    def has_parent(self, index: int) -> bool:
        """
        Check if a node has a parent node.

        Args:
            index (int): The index of the node. 

        Returns:
            Boolean on whether a node has a parent node.
        """
        return self.parent_index(index) >= 0
    
    def insert(self, value):
        """
        Insert a value into the heap.

        Args:
            value: The value to insert. 
        """
        self._array.append(value)
        
        start_index = self.count() - 1
        self.heapify_up(start_index)
    
    def heapify_up(self, index: int):
        """
        Perform heapify up starting at a given index.

        Args:
            index (int): The starting index.
        """
        parent_index = self.parent_index(index)
        while self.has_parent(index) and self._array[index] > self._array[parent_index]:
            self._array[index], self._array[parent_index] = self._array[parent_index], self._array[index]
            index = parent_index
            parent_index = self.parent_index(index)

    def pop(self):
        """
        Return the value of the root node (max value) and remove it from the heap.

        Returns:
            Return the value from the root node.
        """
        root_value = self.root()
        
        # start at root node
        start_index = 0
        if self.count() == 0:
            raise Exception("Heap is empty")
        if self.count() == 1:
            self._array.pop()
        else:
            self._array[start_index] = self._array.pop()
        
        self.heapify_down(start_index)
        return root_value
        
    def heapify_down(self, index: int):
        """
        Perform heapify down starting at a given index.

        Args:
            index (int): The starting index.
        """
        while self.has_left(index):
            higher_index = self.left_index(index)
            right_index = self.right_index(index)
            if self.has_right(index) and self._array[right_index] > self._array[higher_index]:
                higher_index = right_index
            
            if self._array[index] > self._array[higher_index]:
                break
            else:
                self._array[index], self._array[higher_index] = self._array[higher_index], self._array[index]
                
            index = higher_index
    
    def enumerate(self):
        """
        Return the enumeration of a heap.

        Returns:
            Enumeration of a heap.
        """
        return enumerate(self._array)

    def count(self) -> int:
        """
        Return the number of items in the heap.

        Returns:
            The number of items in the heap.
        """
        return len(self._array)
    
    def is_empty(self) -> bool:
        """
        Check if a heap has any items.

        Returns:
            True if heap has no items.
            False if heap has more than 0 items.
        """
        return self.count() == 0

    def print(self):
        """
        Print the contents of a heap.
        """
        node_count = 1
        for i in range(self.count()):
            if i + 1 >= node_count:
                print()
                node_count *= 2
            print(self._array[i], end=" ")

    def to_sorted_list(self) -> list:
        """
        Return a sorted list from the heap.

        Returns:
            A sorted list.
        """
        temp_heap = Heap()
        temp_heap._array = self._array[:]

        result = []
        while not temp_heap.is_empty():
            result.append(temp_heap.pop())

        return result

    def __repr__(self):
        """
        Return string representation of a heap in order of priority.
        """
        ordered_list = self.to_sorted_list()
        return "[" + " ".join([str(e) for e in ordered_list]) + "]"

    def __len__(self):
        """
        Get the number of items in the priority queue.

        Returns:
            Number of items in the priority queue
        """
        return self.count()

    def __eq__(self, other):
        """
        Compare two Heap objects for value-based equality.

        Returns: 
            True if both are Heap (or subclass) instances and their arrays are equal.
        """
        if not isinstance(other, self.__class__):
            return False
        return self._array == other._array

class MinHeap(Heap):
    def heapify_up(self, index: int):
        """
        Perform heapify up starting at a given index.

        Args:
            index (int): The starting index.
        """
        parent_index = self.parent_index(index)
        while self.has_parent(index) and self._array[index] < self._array[parent_index]:
            self._array[index], self._array[parent_index] = self._array[parent_index], self._array[index]
            index = parent_index
            parent_index = self.parent_index(index)

    def heapify_down(self, index: int):
        """
        Perform heapify down starting at a given index.

        Args:
            index (int): The starting index.
        """
        while self.has_left(index):
            higher_index = self.left_index(index)
            right_index = self.right_index(index)
            if self.has_right(index) and self._array[right_index] < self._array[higher_index]:
                higher_index = right_index
            
            if self._array[index] < self._array[higher_index]:
                break
            else:
                self._array[index], self._array[higher_index] = self._array[higher_index], self._array[index]
                
            index = higher_index
    

class PriorityQueue(MinHeap):
    """ 
    A priority queue implementation in Python.
    """
    def push(self, priority: int, item):
        """
        Insert an item with a priority into the priority queue.

        Args:
            priority (int): Priority of item.
            item: The item to insert.
        """
        super().insert((priority, item))

    def pop(self):
        """
        Return and remove the highest priority value in the heap.

        Returns:
            Return The highest priority value in the heap.
        """
        priority, item = super().pop()
        return item

    def pop_pair(self) -> tuple:
        """
        Return and remove the highest priority value pair in the heap.

        Returns:
            Return the highest priority, value pair (tuple) in the heap.
        """
        return super().pop()

    def peek(self):
        """
        Return the highest priority value in the heap.

        Returns:
            Return The highest priority value in the heap.
        """
        priority, item = super().peek()
        return item

    def peek_pair(self) -> tuple:
        """
        Return the highest priority value pair in the heap.

        Returns:
            Return the highest priority, value pair (tuple) in the heap.
        """
        return super().peek()

    def to_string_with_priority(self):
        """
        Return string representation of a heap in order of priority.
        """
        temp_array = self._array[:]
        result = []
        while not self.is_empty():
            result.append(str(self.pop_pair()))
        self._array = temp_array

        return "[" + " ".join(result) + "]"

