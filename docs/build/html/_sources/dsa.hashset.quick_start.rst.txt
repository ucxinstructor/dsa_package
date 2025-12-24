HashSet Quick Start
==================

Description
-----------

A hashset is a collection that stores unique elements, using a hash table for efficient membership testing and operations.

Creation
--------

**Import class**

.. code-block:: python

   from dsa.hashset import HashSet  # or the appropriate HashSet class

**Creation**

Create an empty hashset:

.. code-block:: python

   hs = HashSet()

Create a hashset from an iterable:

.. code-block:: python

   hs = HashSet([1, 2, 3])

Common Operations
-----------------

**Add**

Add an item to the set.

.. code-block:: python

   hs.add(10)  # Add 10 to the set

**Contains**

Check if an item is in the set.

.. code-block:: python

   exists = hs.contains(10)  # Check if 10 is in the set

**Remove**

Remove an item from the set.

.. code-block:: python

   hs.remove(10)  # Remove 10 from the set


**Printing Contents**

Use print() to print the contents of the set.

.. code-block:: python

   hs = HashSet()
   hs.add(1)
   hs.add(2)
   hs.add(3)
   hs.add(1)
   
   print(hs)

Outputs the following:

.. code-block:: python

   HashSet([1, 2, 3])
