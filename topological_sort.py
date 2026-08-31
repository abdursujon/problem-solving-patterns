'''
Topological Sort is a pattern used for linearly ordering the vertices of a directed graph in such a way that for every directed edge (U, V), vertex U comes before V. This pattern is particularly useful in scenarios where you have a set of tasks and some tasks depend on others.
Usage
    • Task Scheduling: Ideal for problems where tasks need to be scheduled in a specific order, respecting their dependencies.
    • Course Scheduling: Useful in scenarios like course scheduling where some courses have prerequisites.
Pros and Cons
    • Pros:
        ◦ Clarity: Provides a clear and systematic way to order tasks or vertices.
        ◦ Detecting Cycles: Helps in detecting cycles in a directed graph, which is important for understanding if a valid ordering is possible.
    • Cons:
        ◦ Applicability: Mainly beneficial for problems involving directed graphs and ordering of vertices.
        ◦ Complexity: Implementation can be complex, especially for beginners.
Example Problems from Grokking the Coding Interview
    1. Topological Sort: Given a directed graph, find the topological ordering of its vertices.
    2. Tasks Scheduling: Find if it is possible to schedule all the tasks.
    3. Tasks Scheduling Order: Find the order of tasks we should pick to finish all tasks.
'''    