'''
The Top 'K' Elements pattern involves finding the 'K' largest or smallest elements in an array or stream of data. This pattern is particularly useful when dealing with large datasets and you need to maintain a subset of the data based on certain criteria.
Usage
    • Priority Queue: Utilizes a min-heap or max-heap to efficiently keep track of the 'K' largest or smallest elements.
    • Streaming Data: Ideal for scenarios where the data is streaming in, and you need to maintain the 'K' largest or smallest elements at any given time.
Pros and Cons
    • Pros:
        ◦ Efficiency: Provides a way to find the 'K' largest or smallest elements in O(N log K) time.
        ◦ Space Efficiency: Only requires O(K) space, regardless of the size of the dataset.
    • Cons:
        ◦ Limited to 'K' Elements: Only maintains information about the top 'K' elements, not the entire dataset.
        ◦ Heap Maintenance: Requires careful maintenance of the heap to ensure efficiency.
Example Problems from Grokking the Coding Interview
    1. Top 'K' Numbers: Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
    2. Kth Smallest Number: Given an unsorted array of numbers, find the Kth smallest number in it.
    3. ‘K’ Closest Points to the Origin: Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.
'''    