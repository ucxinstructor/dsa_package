Array Quick Start
=================

Description
-----------

An array is a linear data structure that is simple and fast. It provides index-based access to a fixed-size, contiguous block of elements.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.array import Array  # or the appropriate Array class

**Creation**

Create an array with a default capacity of 10 element:

.. code-block:: python

   a = Array()

Create an array with a capacity of 100 elements:

.. code-block:: python

   a = Array(100)

Common Operations
-----------------

**Access element**

Retrieve an element by its index. Raises IndexError if the index is out of bounds.

.. code-block:: python

   value = a[5]  # Access the element at index 5

**Update element**
Assign a new value to an element at a specific index. Raises IndexError if the index is out of bounds.

.. code-block:: python

   a[5] = 40 # Update the element at index 5 to 42

**Append element**

Append an element to the array. Raise an exception if capacity is exceeded.
.. code-block:: python

   a.append(10)  # Append 10 to the end of the array

**Insert**
Insert an element at a specified index, shifting existing elements to the right.
.. code-block:: python

   a.insert(2, 15)  # Insert 15 at index 2
**Delete**
Delete an element at a specified index, shifting subsequent elements to the left.
.. code-block:: python

   a.delete(3)  # Delete the element at index 3
**Iteration**
- Iteration / Traversal

Other Related Classes
---------------------

- :class:`dsa.array.DynamicArray`
- :class:`dsa.array.CircularArray`
