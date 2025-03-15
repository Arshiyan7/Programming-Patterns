# Two Pointers Technique

## What is Two Pointers?

The Two Pointers technique is an algorithmic pattern that uses two pointers (indices) to iterate through a data structure, usually an array or linked list, in a coordinated manner. These pointers can move independently or dependently, allowing for efficient searching, manipulation, or comparisons within the data. This pattern is especially useful when dealing with sorted arrays or lists, or when searching for pairs or subranges that satisfy specific conditions.

**Basic Idea:**

1.  **Initialize Pointers:** Typically, you start by initializing two pointers, often named `left` and `right`, or `slow` and `fast`. Their initial positions depend on the problem. Common starting points are:
    *   Both pointers at the beginning of the array/list.
    *   One pointer at the beginning and the other at the end.
    *   One pointer ahead of the other by a certain distance.
2.  **Move Pointers Conditionally:**  Move the pointers based on a condition or comparison. The rules for pointer movement are critical to the algorithm.
3.  **Check Condition/Update:** Inside the loop where you are moving pointers, you will check a condition (e.g., sum of elements at the pointers, equality to a target value) and/or update variables based on the problem's requirements.
4.  **Terminate:**  Continue moving the pointers until a specific condition is met, such as reaching the end of the array/list or finding the desired result.

## Types of Two Pointers:

*   **Opposite Direction:**  One pointer starts at the beginning, the other at the end, and they move towards each other (often used for sorted arrays/lists).
*   **Same Direction:** Both pointers start at the same end and move in the same direction (often used for finding subarrays or sublists satisfying a condition).  Can be `slow` and `fast` pointers where one pointer is ahead of the other (used for finding cycles in linked lists, for example).

## When to Use Two Pointers:

*   The problem involves arrays, linked lists, or strings.
*   The problem requires finding pairs, triplets, or subranges that satisfy certain conditions.
*   The data structure is sorted, or can be sorted.
*   The problem can be solved with a single pass through the data.

## Benefits:

*   **Efficiency:**  Reduces time complexity, often from O(n^2) to O(n) or O(n log n) (if sorting is required).
*   **Space Efficiency:**  Typically requires minimal extra space (O(1)).
*   **Elegance:**  Offers a clean and concise solution for many problems.

## Example Problems:

*   Two Sum (find pairs that add up to a target value)
*   Reverse String (in-place)
*   Palindrome Check
*   Merge Sorted Arrays
*   Remove Duplicates from Sorted Array
*   Linked List Cycle Detection (Floyd's Tortoise and Hare Algorithm)