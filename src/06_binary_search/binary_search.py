'''
Backtracking is a general algorithmic technique that considers searching through all the possible configurations of a search space in order to solve computational problems. It is particularly useful for optimization problems and when a complete search of the solution space is required. The main idea is to explore each possibility until the solution is found or all possibilities have been exhausted.
Usage
    • Combinatorial Problems: Ideal for solving problems that require generating all possible configurations like permutations, combinations, and subsets.
    • Puzzle Solving: Useful for solving puzzles such as Sudoku, crossword puzzles, and the N-Queens problem.
Pros and Cons
    • Pros:
        ◦ Completeness: Ensures that the entire solution space is explored, guaranteeing that the optimal solution will be found if it exists.
        ◦ Space Efficiency: Uses less memory as it only needs to store the current state and the decision stack.
    • Cons:
        ◦ Time Complexity: Can lead to exponential time complexity, as it explores all possible configurations.
        ◦ Optimization Required: May require additional optimizations like pruning to be practical for larger instances.
Example Problems from Grokking the Coding Interview
    1. Subsets: Given a set of numbers, find all of its subsets.
    2. Permutations: Given a set of distinct numbers, find all of its permutations.
    3. N-Queens: Place N queens on an N×N chessboard so that no two queens threaten each other.
'''