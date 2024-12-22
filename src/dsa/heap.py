""" Module containing heap classes. """
class Heap:
    """ 
    A heap implementation.

    Args:
        maxheap: return a max-heap if True  (default), otherwise return a min-heap
    Todo:
        make heap_print work with pq
    """
    def __init__(self):
        self._array = []

    @classmethod
    def from_list(cls, mylist: list):
        hp = cls()
        for e in mylist:
            hp.insert(e)

        return hp

    def to_list(self) -> list:
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
        Get the max value if max-heap and min value if min-heap.

        Returns:
        Get the max value if max-heap and min value if min-heap.
        """
        return self.root()

    def last(self):
        """
        Get the last node of the heap.

        Returns:
        The last node's value. None if count is 0.
        """
        if self.count() == 0:
            return None

        return self._array[-1] 
    
    def left_index(self, index: int) -> int:
        """
        Get the value of the left child.

        Args:
            index: current index  

        Returns:
        the index of the left child
        """
        return (index * 2) + 1

    def right_index(self, index: int) -> int:
        """
        Get the value of the right child.

        Args:
            index: current node index  

        Returns:
        the index of the right child
        """
        return (index * 2) + 2

    def parent_index(self, index: int) -> int:
        """
        Get the value of the parent child.

        Args:
            index: current node index  

        Returns:
        the index of the parent child
        """
        return (index - 1) // 2
    
    def has_left(self, index: int) -> bool:
        """
        Check if current node has an left child.

        Args:
            index: current node index  

        Returns:
        the index of the left child
        """
        return self.left_index(index) < self.count()
    
    def has_right(self, index: int) -> bool:
        """
        Check if current node has an right child.

        Args:
            index: current node index  

        Returns:
        the index of the left child
        """
        return self.right_index(index) < self.count()

    def has_parent(self, index: int) -> bool:
        """
        Check if current node has a parent node.

        Args:
            index: current index  

        Returns:
        the index of the left child
        """
        return self.parent_index(index) >= 0
    
    def insert(self, value):
        """
        Insert a value into the heap.

        Args:
            value: value to insert  
        """
        self._array.append(value)
        
        start_index = self.count() - 1
        self.heapify_up(start_index)
    
    def heapify_up(self, index: int):
        """
        Perform heapify up starting at a given index.

        Args:
            index: starting index  
        """
        parent_index = self.parent_index(index)
        while self.has_parent(index) and self._array[index] > self._array[parent_index]:
            self._array[index], self._array[parent_index] = self._array[parent_index], self._array[index]
            index = parent_index
            parent_index = self.parent_index(index)

    def pop(self):
        """
        Get the value of the root node and remove it from the heap.

        Returns:
        value of the root node
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
            index: starting index  
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
        enumeration of a heap
        """
        return enumerate(self._array)

    def count(self) -> int:
        """
        Return the number of items in the heap.

        Returns:
        the number of items in the heap
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

    def __len__(self):
        """
        Get the number of items in the priority queue.

        Returns:
        Number of items in the priority queue
        """
        return self.count()

class MinHeap(Heap):
    def heapify_up(self, index: int):
        """
        Perform heapify up starting at a given index.

        Args:
            index: starting index  
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
            index: starting index  
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
    A priority queue implementation in Python
    """
    def push(self, item, priority: int):
        """
        Insert an item with a priority into the priority queue

        Args:
            item: item to insert  
            priority: priority of value
        """
        super().insert((priority, item))

    def pop(self):
        """
        Return and remove the highest priority value in the heap

        Returns:
        Return the highest priority value in the heap
        """
        priority, item = super().pop()
        return item

    def peek(self):
        """
        Return the highest priority value in the heap

        Returns:
        Return the highest priority value in the heap
        """
        priority, item = super().peek()
        return item

