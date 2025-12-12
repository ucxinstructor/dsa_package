Stack Quick Start
=================

Description
-----------

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. It supports push and pop operations at one end.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.stack import Stack  # or the appropriate Stack class

**Creation**

Create a stack with a default capacity of 10 elements:

.. code-block:: python

   s = Stack()

Create a stack with a capacity of 100 elements:

.. code-block:: python

   s = Stack(100)

Common Operations
-----------------

**Push element**

Push an element into the stack. Raise Exception when trying to push more elements than the capacity.

.. code-block:: python

   s.push(10)  # Push 10 onto the stack

**Pop element**

Pop an element from the stack. Raise Exception when there are no elements to pop.

.. code-block:: python

   value = s.pop()  # Pop the top element

**Peek element**

Return the element from the top of the stack. Raise Exception if stack is empty.

.. code-block:: python

   value = s.peek()  # Peek at the top element

Other Related Classes
---------------------

- :class:`dsa.stack.DynamicStack`