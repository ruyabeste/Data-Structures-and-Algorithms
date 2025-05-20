.. sphinx_odev documentation master file, created by
   sphinx-quickstart on Wed May 14 00:17:38 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sphinx_odev documentation
=========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

Bubble Sort Algorithm
=====================

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
The algorithm gets its name because smaller elements \"bubble\" to the top of the list.

Example Python code:

.. code-block:: python

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   modules

