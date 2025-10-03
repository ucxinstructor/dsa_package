""" Module containing singly linked list class. """

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
    def __init__(self, head: Node=None, tail: Node=None, count: int=0):
        """ 
        Initialize a singly linked list.
        
        if only the head node is specified, tail is set to the head node and count is automatically set to 0
        if both head and tail nodes are specified, count should be specified as well
        
        Args:
            head: The reference to the head node.
            tail: The reference to the tail node.
            count: The number of nodes in the linked list.

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

    def print(self):
        """
        Print the contents of the linked list.
        """
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

            
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
    
    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.
        """
        return self.count == 0
        
    def search(self, value) -> int:
        """
        Search for a value in the linked list.

        Args:
            value: The value to search for.

        Returns:
            Return index of found value.
        
        Raises:
            Exception: If value is not found.
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
            value: The value to append.

        Returns:
            None

        Raises:
            IndexError: If index is out of bounds.
        """
        i = 0
        
        # insert front
        if index == 0:
            self.prepend(value)
            return
        elif index == self.count: # insert at end
            self.append(value)
            return
        elif index > self.count:
            raise IndexError("Index Out of Bounds")
        
        # find node to insert after
        current = self.head
        while index < i or current:
            i += 1
            if i == index:
                break
            current = current.next
        
        if index > i:
            raise IndexError("Index Out of Bounds")

        new_node = Node(value)
        tmp = current.next
        current.next = new_node
        new_node.next = tmp
        self.count += 1

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
        self.count += 1
        
    def append(self, value):
        """
        Place a value at the end of the linked list.

        Args:
            value: A value to append.

        Returns:
            None
        
        Raises:
            IndexError: If linked list is empty or index is not found.
        """
        if self.head is None:
            self.head = Node(value)
            if self.count == 0:
                self.tail = self.head
            self.count += 1
            return

        # go to the end of the list
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        
        self.count += 1

    def delete(self, index: int):
        """
        Delete a node at a specified index. Raise IndexError if linked list is empty or if index is not found.

        Args:
            index: Index of element to be deleted.
        
        Returns:
            None
            
        Raises:
            IndexError: If linked list is empty or index is not found.
        """
        if index == 0:
            self.delete_head()
            return
        elif index + 1 == self.count:
            self.delete_tail()
            return

        i = 0
        current = self.head
        prev = None
        while current:
            if index == i:
                if prev is not None:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.count -= 1
                return
            i += 1
            prev = current
            current = current.next
        raise IndexError("Index not found")

    def delete_head(self):
        """
        Delete the head node in the linked list. Raise IndexError if linked list is empty.

        Returns:
            None

        Raises:
            IndexError: If linked list is empty.
        """
        if self.head is None:
            raise IndexError("LinkedList is Empty")
        self.head = self.head.next
        self.count -= 1

    def delete_tail(self):
        """
        Delete the last node in the linked list. Raise IndexError if linked list is empty.

        Returns:
            None
            
        Raises:
            IndexError: If linked list is empty.
        """
        if self.head is None:
            raise IndexError("LinkedList is Empty")
        
        if self.head.next is None:
            self.head = None
            self.count -= 1
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        
        current.next = None
        self.tail = current
        self.count -= 1

    def __eq__(self, other):
        """
        Compare two LinkedList objects for value-based equality.
        
        Returns:
            True if both are LinkedList instances and their contents are equal.
        """
        if not isinstance(other, self.__class__):
            return False
        return self.to_list() == other.to_list()
    