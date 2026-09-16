'''
The Two Heaps pattern involves using two priority queues (heaps) to maintain a running balance or median of a set of numbers. One heap keeps track of the smaller half of the numbers, and the other keeps track of the larger half.
Usage
    • Running Median: Perfect for problems where you need to find the median of a set of numbers as new numbers are added.
    • Balanced Partition: Useful for problems where you need to maintain a balanced partition of numbers.
Pros and Cons
    • Pros:
        ◦ Efficiency: Provides a way to efficiently find the median or maintain balance in O(log N) time.
        ◦ Dynamic: Can handle dynamic datasets where numbers are added over time.
    • Cons:
        ◦ Complexity: Implementation can be more complex due to the need to balance the two heaps.
        ◦ Space Overhead: Requires additional space to store the numbers in the heaps.
Example Problems from Grokking the Coding Interview
    1. Find the Median of a Number Stream: Design a class to calculate the median of a number stream.
    2. Sliding Window Median: Find the median of all subarrays of size ‘K’ in the array.
    3. Maximize Capital: Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit.
'''    