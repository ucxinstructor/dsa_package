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
        

    def insert_after(self, after_value, value):
        """
        Insert a value after a specified value. Raise exception if value is not found.

        Args:
            after_value: The value to insert after.
            value: The value to append.

        Returns:
            None

        Raises:
            ValueError: If value is not found.
        """
                
        # find node to insert after
        current = self.head
        while current:
            if current.value == after_value:
                break
            current = current.next
        
        if current is None:
            raise ValueError("Value not found")
        
        # insert at the end
        if current == self.tail:
            self.append(value)
            return

        # insert in the middle
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

    def delete(self, value):
        """
        Delete the first occurrence of a value in the linked list.

        Args:
            value: The value to be deleted.
        
        Returns:
            None
            
        Raises:
            ValueError: If the value is not found.
        """
        if self.head is None:
            raise ValueError("Value not found")

        if self.head.value == value:
            self.head = self.head.next
            self.count -= 1
            if self.count == 0:
                self.tail = None
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.count -= 1
                return
            current = current.next
            
        raise ValueError("Value not found")

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
    