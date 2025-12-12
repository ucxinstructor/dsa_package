Heap Quick Start
===============

Description
-----------

A heap is a specialized tree-based data structure that satisfies the heap property, used for efficient priority-based operations.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.heap import Heap  # or the appropriate Heap class

**Creation**

Create an empty heap:

.. code-block:: python

   h = Heap()

Common Operations
-----------------

**Insert**

Insert a value into the heap.

.. code-block:: python

   h.insert(10)  # Insert 10 into the heap

**Pop**

Return the value of the root node (max value) and remove it from the heap.

.. code-block:: python

   value = h.pop()  # Remove and return the max value

**Peek**

Get the max value of the max heap.

.. code-block:: python

   value = h.peek()  # Get the max value without removing

Other Related Classes
---------------------

- :class:`dsa.heap.MinHeap`
- :class:`dsa.heap.PriorityQueue`
