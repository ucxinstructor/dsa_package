Deque Quick Start
=================

Description
-----------

A deque is a linear data structure that supports appending and popping elements from both ends, with a fixed capacity.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.deque import Deque  # or the appropriate Deque class

**Creation**

Create a deque with a default capacity of 10 elements:

.. code-block:: python

   d = Deque()

Create a deque with a capacity of 100 elements:

.. code-block:: python

   d = Deque(100)

Common Operations
-----------------

**Append left**

Append an element to the left of the deque. Raises an exception when the deque is full.

.. code-block:: python

   d.append_left(10)  # Append 10 to the left

**Append right**

Append an element to the right of the deque. Raises an exception when the deque is full.

.. code-block:: python

   d.append_right(20)  # Append 20 to the right

**Pop left**

Remove and return the element from the left of the deque. Raises an exception if the deque is empty.

.. code-block:: python

   value = d.pop_left()  # Pop from the left

**Pop right**

Pop an element from right the deque. Raise an exception if the deque is empty.

.. code-block:: python

   value = d.pop_right()  # Pop from the right

**Peek left**

Get the element at the left of the deque without removing it. Raises an exception if the deque is empty.

.. code-block:: python

   value = d.peek_left()  # Peek at the left

**Peek right**

Get the element at the right of the deque without removing it. Raises an exception if the deque is empty.

.. code-block:: python

   value = d.peek_right()  # Peek at the right
   
   
**Printing Contents**

Use print() to print the elements of the dequeue.

.. code-block:: python

  d = Deque()
  d.push_front(1)
  d.push_front(2)
  d.push_back(3)
  print(d)

Outputs the following:

.. code-block:: python

   [2, 1, 3] Count: 3 Capacity: 10


Other Related Classes
---------------------

- :class:`dsa.deque.DynamicDeque`
