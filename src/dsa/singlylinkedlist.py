""" Module containing singly linked list class. """
from __future__ import annotations


class Node:
    """ 
    A singly linked list node implementation.
    """
    def __init__(self, value):
        """ 
        A singly linked list node.
        Args:
            value: The value of the node.
        """
        #: value of the node
        self.value = value
        #: reference to the next node
        self.next = None

class LinkedList:
    """ 
    A singly linked list implementation.
    """
    def __init__(self, head: Node | None = None,
                       tail: Node | None = None,
                       count: int = 0):
        """ 
        Initialize a singly linked list.
        
        if only the head node is specified, tail is set to the head node and count is automatically set to 0
        if both head and tail nodes are specified, count should be specified as well
        
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
    def from_list(cls, mylist=None):
        """
        Create a linked list from a list.

        Args:
            mylist: A list or container to convert from.
        
        Returns:
            A  linked list containing the items from mylist.
        """
        ll = cls()
        if mylist is None:
            return ll

        for value in mylist:
            ll.append(value)

        return ll
    
    def to_list(self) -> list:
        """
        Create a list with contents of the linked list.

        Returns:
            List with contents of linked list.
        """
        mylist = []
        current = self.head
        while current:
            mylist.append(current.value)
            current = current.next
        return mylist

    def traverse(self):
        """
        Print the contents of the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def search(self, value) -> Node | None:
        """
        Search for a value in the linked list.

        Args:
            value: The value to search for.

        Returns:
            Return index of found value.
            Return None if value is not found.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
            

    
    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.
        """
        return self.count == 0
        

    def insert_after(self, target_value, value):
        """
        Insert a value after a specified value. Raise exception if value is not found.

        Args:
            target_value: The value of node to insert after.
            value: The new value to insert.
        Returns:
            None

        Raises:
            ValueError: If value is not found.
        """
                
        # find node to insert after
        current = self.head
        while current is not None and current.value != target_value:
            current = current.next
        
        if current is not None:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
            self.count += 1
        else:
            raise ValueError("Value not found")
        
 
    def prepend(self, value):
        """
        Place a value at the beginning of the linked list.

        Args:
            value: A value to append.

        Returns:
            None
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node
        self.count += 1
        
    def append(self, value):
        """
        Place a value at the end of the linked list.

        Args:
            value: A value to append.

        Returns:
            None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node        
        self.count += 1

    def delete(self, value):
        """
        Delete the first occurrence of a value in the linked list.

        Args:
            target: The value to be deleted.
        
        Returns:
            None
            
        Raises:
            ValueError: If the value is not found.
        """
        if self.head is None:
            raise ValueError("Value not found")

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.count -= 1
            return

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self.count -= 1
        else:
            raise ValueError("Value not found")
    

    def delete_head(self):
        """
        Delete the head node in the linked list. Raise IndexError if linked list is empty.

        Returns:
            None

        Raises:
            ValueError: If linked list is empty.
        """
        if self.head is None:
            raise ValueError("LinkedList is Empty")

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.count -= 1

    def delete_tail(self):
        """
        Delete the last node in the linked list. Raise IndexError if linked list is empty.

        Returns:
            None
            
        Raises:
            ValueError: If linked list is empty.
        """
        if self.head is None:
            raise ValueError("LinkedList is Empty")

        if self.count == 1:
            self.head = None
            self.tail = None
        else:         
            current = self.head
            while current.next != self.tail:
                current = current.next        
            current.next = None
            self.tail = current
        self.count -= 1

    def __repr__(self):
        """
        Return a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        s = ""
        current = self.head
        while current:
            s += str(current.value) + " "
            current = current.next

        return f"[ {s}] Count: {self.count}"
    
    def __getitem__(self, index: int) -> Node:
        """ 
        Return value at a specified index. Raise IndexError if index is out of bounds.
        
        Args:
            index: Index of value.

        Raises:
            IndexError: If index is out of bounds.

        Returns:
            The value at the specified index.
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
        Return the number of elements in the linked list.
        """
        return self.count
    
    def __eq__(self, other):
        """
        Compare two LinkedList objects for value-based equality.
        
        Returns:
            True if both are LinkedList instances and their contents are equal.
        """
        if not isinstance(other, self.__class__):
            return False
        return self.to_list() == other.to_list()
    