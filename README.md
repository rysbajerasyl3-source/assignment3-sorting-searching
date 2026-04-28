 Assignment 3: Sorting and Searching Algorithm Analysis System

 Project Overview

This project implements and compares different sorting and searching algorithms in Java.
The goal is to analyze their performance using execution time measurements and understand how algorithm efficiency changes with input size and data structure.

Selected algorithms:

* **Insertion Sort** (Basic Sorting)
* **Merge Sort** (Advanced Sorting)
* **Binary Search** (Searching)

Algorithms Description

Insertion Sort

Insertion Sort builds a sorted array one element at a time by inserting elements into their correct position.

**How it works:**

* Starts from the second element
* Compares it with previous elements
* Shifts larger elements to the right
* Inserts the element in the correct position

**Time Complexity:**

* Best case: O(n)
* Average case: O(n²)
* Worst case: O(n²)

Merge Sort

Merge Sort is a divide-and-conquer algorithm that splits the array into smaller parts and merges them back in sorted order.

**How it works:**

* Divides the array into halves
* Recursively sorts each half
* Merges sorted halves together

**Time Complexity:**

* Best case: O(n log n)
* Average case: O(n log n)
* Worst case: O(n log n)

Binary Search

Binary Search finds an element in a sorted array by repeatedly dividing the search interval in half.

**How it works:**

* Compares target with middle element
* If equal → found
* If smaller → search left half
* If larger → search right half

**Time Complexity:**

* Best case: O(1)
* Average case: O(log n)
* Worst case: O(log n)

Experimental Setup

The program tests algorithms on different datasets:

Array Sizes:

* Small: 10 elements
* Medium: 100 elements
* Large: 1000 elements

### Data Types:

* Random arrays
* Sorted arrays

Measurements:

Execution time using `System.nanoTime()`

Experimental Results

### Example Output:

```
Array size: 10
Insertion Sort time: 12000
Merge Sort time: 8000
Binary Search time: 2000

Array size: 100
Insertion Sort time: 150000
Merge Sort time: 20000
Binary Search time: 3000

Array size: 1000
Insertion Sort time: 5000000
Merge Sort time: 120000
Binary Search time: 5000
```

Analysis

Which sorting algorithm performed faster? Why?

Merge Sort performed significantly faster than Insertion Sort on larger datasets.
This is because Merge Sort has a time complexity of **O(n log n)**, while Insertion Sort has **O(n²)**.

How does performance change with input size?

For small arrays, the difference is minimal
For large arrays, Merge Sort becomes much faster
Insertion Sort slows down rapidly as input size increases

How does sorted vs unsorted data affect performance?

Insertion Sort becomes faster on sorted arrays (close to O(n))
Merge Sort performance remains stable regardless of input order

Do the results match Big-O expectations?

Yes:
Insertion Sort shows quadratic growth
Merge Sort shows logarithmic growth

Which searching algorithm is more efficient?

Binary Search is more efficient because it runs in **O(log n)** time, compared to Linear Search which runs in **O(n)**.

Why does Binary Search require a sorted array?

Binary Search relies on dividing the array into halves.
This is only possible when the array is sorted, so we know which half to discard.


Reflection

During this assignment, I learned how different algorithms behave in practice and how their theoretical time complexity affects real performance.

Merge Sort proved to be much more efficient than Insertion Sort for large datasets, while Insertion Sort performed well on small or nearly sorted data.

One challenge was correctly implementing Merge Sort and handling array splitting and merging. Another challenge was ensuring accurate time measurement using `System.nanoTime()`.

Overall, this project helped me better understand algorithm efficiency and performance analysis.

Project Structure

```
assignment2-sorting-searching/
├── src/
│   ├── Sorter.java
│   ├── Searcher.java
│   ├── Experiment.java
│   └── Main.java
├── docs/
│   ├── screenshots/
│   └── results/
├── README.md
└── .gitignore
```

Conclusion

This project demonstrates how algorithm choice affects performance.
Efficient algorithms like Merge Sort and Binary Search are essential when working with large datasets.
