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

from collections import deque

# Define a decision tree as a dictionary 
tree = {
	'A': ['B', 'C'],
    'B': ['D', 'E'],
	'C': ['F', 'G'],
	'D': ['H', 'I'],
	'E': ['J', 'K'],
	'F': ['L', 'M'],
	'G': ['N', 'O'],
	'H': [],
	'I': [],
	'J': [],
	'K': [],
	'L': [],
	'M': [],
	'N': [],
	'O': []
}

def bfs(tree, start):
    visited = [] # list to keep track of visited nodes 
    queue = deque([start]) # initialise the queue with starting node 
    
    while queue: # While there are still node to process
        node = queue.popleft() # deque a node from the front of the queue 
        if node not in visited: # check if the node has been visited 
            visited.append(node) # mark the current node as visited 
            print(node, end=" ") # print out the visited node 
                        
            # Enqueue all unvisited neighbours (children) of the current node 
            for neighbour in tree[node]: # get the list of the children of current node from tree dictionary (here for neighbour in tree[node] means for each item in that list
                if neighbour not in visited: # if current children node not in visited node list, add them 
                    queue.append(neighbour)

# Test if bfs function works by passing the tree 
bfs(tree, 'A') # Expected printed output is: A B C D E F G H I J K L M N O

# Next challange is figure out V + E where V is the number of vertices and E is the number of edges in the tree 
print("\n")
vertices = len(tree)
count_edges = 0

for key in tree.keys():
    print(f"Node: {key}, Children: {tree[key]}")
    count_edges += len(tree[key])

print("")
print(f"Number of Vertices: {vertices}, Number of Edges: {count_edges}")