'''
The Tree Breadth First Search (BFS) pattern involves traversing a tree level by level, ensuring that you visit all the nodes at the current depth before moving on to the nodes at the next depth level. This is usually implemented using a queue.

Usage
    • Level Order Traversal: Ideal for problems that require you to traverse a tree in level order or when you need to perform operations on nodes at the same depth.
    • Minimum Depth: Useful for finding the minimum depth of a tree, as you can stop the traversal once you find the first leaf node.
Pros and Cons
    • Pros:
        ◦ Complete Traversal: Ensures that every node in the tree is visited.
        ◦ Level Order Information: Provides information about the depth or level of each node.
    • Cons:
        ◦ Space Overhead: Requires additional space for the queue, which can be as large as the number of nodes at the largest level.
        ◦ Not as Efficient for Depth-Related Queries: For problems that depend on depth information, a depth-first search might be more efficient.
Example Problems from Grokking the Coding Interview
    1. Binary Tree Level Order Traversal: Traverse a tree in level order and return the values of the nodes at each level.
    2. Reverse Level Order Traversal: Traverse a tree in reverse level order.
    3. Zigzag Traversal: Traverse a tree in a zigzag order.
'''