"""Module containing doubly linked list class."""
from __future__ import annotations

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

    def insert_after(self, target_value, value):
        """
        Insert a value after a specified value. Raise exception if value is not found.

        Args:
            target_value: The value of node to insert after.
            value: The value to append.

        Returns:
            None

        Raises:
            ValueError: If value is not found.
        """
                
        current = self.head

        while current is not None and current.value != target_value:
            current = current.next

        if current is not None:
            new_node = Node(value)
            new_node.next = current.next
            new_node.prev = current

            if new_node.next is not None:
                 new_node.next.prev = new_node
            else:
                 self.tail = new_node

            current.next = new_node
            self.count += 1
        else:
            raise ValueError("Value not found")

    def prepend(self, value):
        """
        Place a value at the beginning of the doubly linked list.

        Args:
            value: The value to prepend to the doubly linked list.
        """
        new_node = Node(value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node
        self.count += 1

    def append(self, value):
        """
        Place a value at the end of the doubly linked list.

        Args:
            value: The value to append to the doubly linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
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

        # 1. Find the actual node to delete
        current = self.head
        while current is not None and current.value != value:
            current = current.next

        # 2. If we finished the loop and didn't find it
        if current is None:
            raise ValueError("Value not found")

        # 3. Case: Deleting the Head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # List is now empty

        # 4. Case: Deleting the Tail
        elif current == self.tail:
            self.tail = current.prev
            self.tail.next = None

        # 5. Case: Deleting from the Middle
        else:
            # The "Double Leapfrog"
            current.prev.next = current.next
            current.next.prev = current.prev

        self.count -= 1

    def delete_head(self):
        """
        Delete the head node of the doubly linked list.

        Raises:
            ValueError: If linked list is empty.
        """
        if self.tail is None:
            raise ValueError("DoublyLinkedList is Empty")

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1


    def delete_tail(self):
        """
        Delete the tail node of the doubly linked list.

        Raises:
            ValueError: If linked list is empty.
        """
        if self.tail is None:
            raise ValueError("DoublyLinkedList is Empty")

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
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
