Linked List Quick Start
=======================

Description
-----------

Linked lists store values in nodes connected by references. Singly and doubly linked lists share the same API for typical operations; doubly linked lists additionally maintain `prev` references for efficient reverse operations.

Creation
--------

**Import classes**

.. code-block:: python

   from dsa.singlylinkedlist import LinkedList, Node as SNode
   from dsa.doublylinkedlist import DoublyLinkedList, Node as DNode

**Create an empty singly linked list**

.. code-block:: python

   ll = LinkedList()

**Create an empty doubly linked list**

.. code-block:: python

   dll = DoublyLinkedList()

Nodes-Only Construction
-----------------------

**Build a singly linked list using nodes**

.. code-block:: python

   # Create nodes and link them
   n1 = SNode(1)
   n2 = SNode(2)
   n3 = SNode(3)
   n1.next = n2
   n2.next = n3

   # Initialize the list with head/tail
   ll = LinkedList(head=n1, tail=n3, count=3)

**Build a doubly linked list using nodes**

.. code-block:: python

   # Create nodes and link them with next/prev
   d1 = DNode(1)
   d2 = DNode(2)
   d3 = DNode(3)
   d1.next = d2
   d2.prev = d1
   d2.next = d3
   d3.prev = d2

   # Initialize the list with head/tail
   dll = DoublyLinkedList(head=d1, tail=d3, count=3)

Common Operations (Shared)
--------------------------

**Prepend**

Place a value at the beginning of the linked list.

.. code-block:: python

   ll.prepend(0)
   dll.prepend(0)

**Append**

Place a value at the end of the linked list.

.. code-block:: python

   ll.append(4)
   dll.append(4)

**Insert after**

Insert a value after a specified value. Raise exception if value is not found.

.. code-block:: python

   ll.insert_after(2, 99)
   dll.insert_after(2, 99)

**Delete**

Delete the first occurrence of a value in the linked list.

.. code-block:: python

   ll.delete(99)
   dll.delete(99)

**Delete head / tail**

Delete the head or the last node in the linked list. Raise IndexError if linked list is empty.

.. code-block:: python

   ll.delete_head(); ll.delete_tail()
   dll.delete_head(); dll.delete_tail()

**Search**

Search for a value in the linked list.

.. code-block:: python

   node = ll.search(2)
   node2 = dll.search(2)

**Access element**

Return value at a specified index. Raise IndexError if index is out of bounds.

.. code-block:: python

   first = ll[0]
   first2 = dll[0]

**Printing Contents**

Use print() to print the elements of the linked list.

.. code-block:: python

   ll = LinkedList.from_list([1, 2, 3, 4])
   print(ll)

Outputs the following:

.. code-block:: python

   [1, 2, 3, 4] Count: 4
