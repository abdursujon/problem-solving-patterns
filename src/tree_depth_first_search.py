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
graph = {
    'A' : ['B', 'G'],
    'B' : ['C' , 'D', 'E'],
    'C' : [], 
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : ['H'],
    'H' : ['I'],
    'I' : []
} 

def depth_first_search(graph, start):
    """Iterative DFS, returns nodes in preorder (root-left-right). Graph is a dictionary, where "key" is a string and each key has a list maped to it."""
    visited = {start} # set to track visited nodes 
    stack = [start] # list to push and pop nodes (list can work as a stack)
    order = [] # a list to store how nodes were visited 

    while stack: 
        s = stack.pop()
        order.append(s)
        for n in reversed(graph[s]):
            # explore a node if it's note visited already otherwise ignore 
            if n not in visited:
                visited.add(n)
                stack.append(n)
    return order

assert depth_first_search(graph, 'A') == list('ABCDEFGHI')   
print(depth_first_search(graph, 'A'))