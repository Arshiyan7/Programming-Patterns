# Sliding Window Technique

## What is Sliding Window?

The Sliding Window technique is a powerful algorithmic pattern used to solve problems involving arrays (or strings) where you need to perform operations on a contiguous subarray (or substring) of a specific size.  Instead of recomputing results for each subarray from scratch, the sliding window cleverly *slides* the window one element at a time, updating the result incrementally.  This significantly reduces the time complexity from often O(n^2) or O(n^3) to O(n).

**Basic Idea:**

1.  **Define a window:**  Create a window of a specific size (`k`) within the array/string.
2.  **Perform calculation:**  Calculate some result (e.g., sum, max, average) within the current window.
3.  **Slide the window:**  Move the window one element forward (or backward, depending on the problem). This usually involves adding one element to the right of the window and removing one element from the left.
4.  **Update calculation:**  Update the result based on the added and removed elements. Avoid recalculating the entire window's result.
5.  **Repeat:** Continue sliding and updating until you've covered the entire array/string.

**When to Use Sliding Window:**

*   The problem involves arrays or strings.
*   You need to find the best subarray/substring that satisfies a certain condition.
*   The size of the subarray/substring is either fixed or can be dynamically adjusted based on constraints.

**Benefits:**

*   **Efficiency:** Reduces time complexity significantly (often from O(n^2) to O(n)).
*   **Simplicity:**  Once understood, the pattern is relatively easy to implement.

**Example Problems:**

*   Maximum Sum Subarray of Size K
*   Minimum Size Subarray Sum
*   Longest Substring Without Repeating Characters
*   Find All Anagrams in a String
