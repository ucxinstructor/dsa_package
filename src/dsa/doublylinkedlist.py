"""Module containing doubly linked list class."""
from dsa.singlylinkedlist import LinkedList

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


class DoublyLinkedList(LinkedList):
    """
    A doubly linked list implementation.
    Inherits several methods from singly linked list, except for methods that  modify the the contents of the list.
    """

    def __init__(self, head: Node | None = None, 
                       tail: Node | None = None, 
                       count: int = 0
    ):
        """
        Initialize a doubly linked list.

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

    def traverse_reverse(self):
        """
        Print the contents of the doubly linked list in reverse order.
        """
        current = self.tail
        while current:
            print(current.value, end=" ")
            current = current.prev
        print()

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
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
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

    def delete(self, value):
        """
        Delete the first occurrence of a value in the doubly linked list.

        Args:
            value: The value to be deleted.

        Raises:
            ValueError: If the value is not found.
        """
        if self.head is None:
            raise ValueError("Value not found")

        current = self.head
        while current:
            if current.value == value:
                if current == self.head:
                    self.delete_head()
                elif current == self.tail:
                    self.delete_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.count -= 1
                return
            current = current.next

        raise ValueError("Value not found")

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
