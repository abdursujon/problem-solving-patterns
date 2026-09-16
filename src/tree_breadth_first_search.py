'''
The Tree Depth First Search (DFS) pattern involves traversing a tree in a depth-first manner, meaning you go as deep as possible down one branch before backing up and exploring other branches. This is typically implemented using recursion or a stack.
Usage
    • Path Finding: Ideal for problems where you need to find a path or check the existence of a path with certain properties.
    • Complex Tree Traversals: Useful for more complex tree traversal problems where you need to maintain state or perform operations as you traverse.
Pros and Cons
    • Pros:
        ◦ Space Efficiency: For a balanced tree, DFS uses less space than BFS.
        ◦ Simplicity: Recursive implementations can be more straightforward and concise.
    • Cons:
        ◦ Can Be Less Efficient for Wide Trees: For very wide trees, DFS can use more space than BFS.
        ◦ May Not Find the Shortest Path: If you're looking for the shortest path in an unweighted tree, BFS is generally a better choice.
Example Problems from Grokking the Coding Interview
    1. Binary Tree Path Sum: Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
    2. All Paths for a Sum: Find all root-to-leaf paths in a binary tree that have a sum equal to a given number.
    3. Count Paths for a Sum: Find the number of paths in a tree that sum up to a given value.
'''