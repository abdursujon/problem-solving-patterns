'''
The K-way Merge pattern involves merging multiple sorted arrays or lists into a single sorted list. This pattern is highly useful in scenarios where you have multiple sorted datasets that you need to combine and maintain the sorted order.
Usage
    • Multiple Sorted Arrays: Ideal for merging multiple sorted arrays or lists.
    • External Sorting: Useful in external sorting, where the data to be sorted does not fit into memory and is stored in sorted chunks.
Pros and Cons
    • Pros:
        ◦ Efficiency: Provides a way to merge multiple sorted arrays in O(N log K) time, where ‘N’ is the total number of elements across all arrays, and ‘K’ is the number of arrays.
        ◦ Space Efficiency: Only requires O(K) space for the priority queue.
    • Cons:
        ◦ Dependent on Sorting: The efficiency of this pattern depends on the arrays being sorted.
        ◦ Priority Queue Overhead: Requires maintenance of a priority queue, which adds to the complexity.
Example Problems from Grokking the Coding Interview
    1. Merge K Sorted Lists: Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
    2. Kth Smallest Number in M Sorted Lists: Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
    3. Find the Smallest Range Covering Elements from K Lists: Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
'''