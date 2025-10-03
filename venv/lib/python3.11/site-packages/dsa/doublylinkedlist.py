""" Module containing doubly linked list class. """

class Node:
    """ 
    A doubly linked list node implementation.
    """
    def __init__(self, value):
        """ 
        Args:
            value: The value of the node.
        """
        #: value of the node
        self.value = value
        #: reference to the next node
        self.next = None
        #: reference to the previous node
        self.prev = None
    
class DoublyLinkedList:
    """ 
    A doubly linked list implementation.
    """
    def __init__(self, head: Node|None=None, tail: Node|None=None, count: int=0):
        """ 
        Initialize a singly linked list.
        
        if only the head node is specified, tail is set to the head node and count is automatically set to 0.
        if both head and tail nodes are specified, count should be specified as well.
        
        Args:
            head (Node): Reference to the head node.
            tail (Node): Reference to the tail node.
            count (int): The number of nodes in the linked list.
        """        
        self.head = head
        if head and tail is None:
            self.tail = head
            self.count = 1
        else:
            self.tail = tail
            self.count = count

    @classmethod
    def from_list(cls, mylist: list):
        """
        Create a doubly linked list from a list.

        Args:
            mylist: A list or container to convert from.
        
        Returns:
            Doubly linked list with the contents of the list.
        """
        dll = cls()
        for value in mylist:
            dll.append(value)

        return dll
    
    def to_list(self) -> list:
        """
        Create a list with contents of the doubly linked list.

        Returns:
            A list with contents of the doubly linked list.
        """
        mylist = []
        current = self.head
        while current:
            mylist.append(current.value)
            current = current.next
        return mylist
        
    def __repr__(self):
        """
        Return a string representation of the doubly linked list.

        The string representation includes all the values in the list
        separated by spaces and the total count of nodes in the list.

        Returns:
            str: A string representation of the list in the format
                 "[ value1 value2 ... valueN] Count: count"
        """
        s = ""
        current = self.head
        while current:
            s += str(current.value) + " "
            current = current.next

        return f"[ {s}] Count: {self.count}"

    def __getitem__(self, index: int) -> Node:
        """ 
        Return value at a specified index. Raise exception if index is out of bounds.
        
        Args:
            index (int): The index of the value.
        Raises:
            IndexError: if index is out of bounds.
        """        
        i = 0
        current = self.head
        while current:
            if i == index:
                return current.value
            current = current.next
            i += 1
        raise IndexError("Index Out of Bounds")
    
    def __len__(self) -> int:
        """
        Return the number of elements in the doubly linked list.
        """
        return self.count
    
    def is_empty(self) -> bool:
        """
        Return True if the doubly linked list is empty.
        """
        return self.count == 0

    def print(self):
        """
        Print the contents of the doubly linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def print_reverse(self):
        """
        Print the contents of the doubly linked list in reverse order.
        """
        current = self.tail
        while current:
            print(current.value, end=" ")
            current = current.prev
        print()
    
    def search(self, value) -> int:
        """
        Search for a value in the linked list. Raise exception if value is not found.

        Args:
            value: The value to search for in the doubly linked list.

        Returns:
            Return index of found value.

        Raises:
            Exception: if value is not found.
        """
        i = 0
        current = self.head
        while current:
            if current.value == value:
                return i
            i += 1
            current = current.next
        raise Exception("Value not found")
    
    def insert(self, index: int, value):
        """
        Insert a value at a specified index. Raise exception if index is out of bounds.

        Args:
            index (int): The index to insert a value.
            value: The value to insert in the doubly linked list.

        Raises:
            IndexError: if index is out of bounds.
        """
        
        # insert front
        if index == 0:
            self.prepend(value)
            return
        elif index == self.count:
            self.append(value)
            return
        elif index > self.count:
            raise IndexError("Index Out of Bounds")
        
        # find node to insert after
        i = 0
        current = self.head
        while index < i or current:
            if i == index:
                break
            current = current.next
            i += 1

        if index > i:
            raise IndexError("Index Out of Bounds")

        new_node = Node(value)
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
        new_node.prev.next = new_node

        self.count += 1
        
    def prepend(self, value):
        """
        Place a value at the beginning of the doubly linked list.

        Args:
            value: The value to prepend to the doubly linked list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.count += 1

    def append(self, value):
        """
        Place a value at the end of the doubly linked list.

        Args:
            value: The value to append to the doubly linked list.
        """
        if self.head is None:
            self.head = Node(value)
            if self.count == 0:
                self.tail = self.head
            self.count += 1
            return
        
        # go to the end of the list
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        
        self.count += 1
        

    def delete(self, index: int):
        """
        Delete a node at a specified index. Raises exception if linked list is empty or if index is invalid.

        Args:
            index (int): The index of element to be deleted.

        Raises:
            IndexError: If linked list is empty or index is invalid.
        """
        if self.head is None:
            raise IndexError("DoublyLinkedList is Empty")

        if index == 0: # Special case: Delete the head node
            self.delete_head()
            return
        elif index == self.count - 1:
            self.delete_tail()
            return
        elif index >= self.count:
            raise IndexError("Index out of range")
        
        # Traverse the list to find the node at the specified index
        current = self.head
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        # Remove the node by adjusting pointers
        if current.next:
            current.next.prev = current.prev
        else:  # If the node to be deleted is the tail (might be redundant)
            self.tail = current.prev

        if current.prev:
            current.prev.next = current.next

        self.count -= 1

    def delete_tail(self):
        """
        Delete the tail node of the doubly linked list. 

        Raises:
            IndexError: If linked list is empty.
        """
        if self.tail is None:
            raise IndexError("DoublyLinkedList is Empty")
        
        self.tail = self.tail.prev
        self.tail.next = None
        self.count -= 1

    def delete_head(self):
        """
        Delete the head node of the doubly linked list.

        Raises:
            IndexError: If linked list is empty.
        """
        if self.head is None:
            raise IndexError("DoublyLinkedList is Empty")
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:  # If the list becomes empty
            self.tail = None
        self.count -= 1

    def __eq__(self, other):
        """
        Compare this doubly linked list to another for equality.

        Args:
            other: The object to compare with.

        Returns:
            True if both are DoublyLinkedList instances and their contents are equal, False otherwise.
        """
        if not isinstance(other, DoublyLinkedList):
            return False
        return self.to_list() == other.to_list()    

