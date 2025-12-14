SinglyLinkedList Quick Start
===========================

Description
-----------

A singly linked list is a linear data structure where each element points to the next, allowing efficient insertions and deletions.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.singlylinkedlist import LinkedList  # or the appropriate LinkedList class

**Creation**

Create an empty singly linked list:

.. code-block:: python

   ll = LinkedList()

Common Operations
-----------------

**Prepend**

Place a value at the beginning of the linked list.

.. code-block:: python

   ll.prepend(10)  # Add 10 to the front

**Append**

Place a value at the end of the linked list.

.. code-block:: python

   ll.append(20)  # Add 20 to the end

**Access element**

Return value at a specified index. Raise IndexError if index is out of bounds.

.. code-block:: python

   value = ll[0]  # Get the first element

**Delete**

Delete the first occurrence of a value in the linked list.

.. code-block:: python

   ll.delete(10)  # Delete the first occurrence of 10

Other Related Classes
---------------------

- :class:`dsa.doublylinkedlist.DoublyLinkedList`
