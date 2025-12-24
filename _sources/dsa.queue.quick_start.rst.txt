Queue Quick Start
=================

Description
-----------

A queue is a linear data structure that follows the First In, First Out (FIFO) principle. It supports enqueue and dequeue operations.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.queue import Queue  # or the appropriate Queue class

**Creation**

Create a queue with a default capacity of 10 elements:

.. code-block:: python

   q = Queue()

Create a queue with a capacity of 100 elements:

.. code-block:: python

   q = Queue(capacity=100)

Common Operations
-----------------

**Enqueue element**

Enqueue an element into the queue. Raise Exception when trying to enqueue more elements than the capacity.

.. code-block:: python

   q.enqueue(10)  # Enqueue 10 into the queue

**Dequeue element**

Dequeue an element from the queue. Raise Exception when there are no elements to dequeue.

.. code-block:: python

   value = q.dequeue()  # Dequeue the front element

**Peek element**

Return the element in front of the queue. Raise Exception if queue is empty.

.. code-block:: python

   value = q.peek()  # Peek at the front element
   
**Printing Contents**

Use print() to print the elements of the queue.

.. code-block:: python

   q = Queue()
   q.enqueue(1)
   q.enqueue(2)
   q.enqueue(3)
   print(q)

Outputs the following:

.. code-block:: python

   [1, 2, 3] Count: 3 Capacity: 10


Other Related Classes
---------------------

- :class:`dsa.queue.DynamicQueue`
- :class:`dsa.queue.CircularQueue`
