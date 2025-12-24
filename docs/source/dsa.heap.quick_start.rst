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

Create an empty heap (max heap). Use MinHeap() to create a min heap:

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
   
   
**Printing Contents**

Use print() method to print the elements of the heap.

.. code-block:: python

   h = Heap()
   h.insert(1)
   h.insert(2)
   h.insert(3)
   h.insert(4)
   
   h.print()

Outputs the following:

.. code-block:: python

   4
   3 2
   1
   
Alternative way to print the heap:

.. code-block:: python
   
   from dsa.pretty_print import heap_print
   heap_print(h)

Outputs the following:

.. code-block:: python
   
       4
    3     2
   1

Use the HeapDraw class to draw a visual representation of a heap.

.. code-block:: python   

   from dsa.draw import HeapDraw
   h = Heap()
   h.insert(1)
   h.insert(2)
   h.insert(3)
   h.insert(4)
 
   hd = HeapDraw(h)
   hd.draw()

.. figure:: images/heap.png
   :alt: Heap structure image
   :width: 400px

   Example of a Heap structure using HeapDraw.


Other Related Classes
---------------------

- :class:`dsa.heap.MinHeap`
- :class:`dsa.heap.PriorityQueue`
