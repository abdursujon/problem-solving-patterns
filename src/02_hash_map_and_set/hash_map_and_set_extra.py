
from typing import List
"""This solution covers the book Coding Interview Patterns by Alex Xu and Shaun"""

# Hashmap problem 

"""
Problem 1: 
Pair Sum - Unsorted
Given an array of integers, return the indexes of any two numbers that add up to a target. 
The order of the indexes in the result doesn't matter. 
If no pair is found, return an empty array.
Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
"""
def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    num_mp = {}
    for i, num in enumerate(nums):
        num_mp[num] = i 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_mp and num_mp[complement] != i:
            return [i, num_mp[complement]]
    return []


"""
Problem 2: Geometric Sequenc Triplets
Geometric Sequence Triplets
Medium
A geometric sequence triplet is a sequence of three numbers where each successive number is obtained 
by multiplying the preceding number by a constant called the common ratio.

Let's examine three triplets to understand how this works:

(1, 2, 4): This is a geometric sequence with a ratio of 2 (i.e., [1, 1⋅2 = 2, 2⋅2 = 4]).
(5, 15, 45): This is a geometric sequence with a ratio of 3 (i.e., [5, 5⋅3 = 15, 15⋅3 = 45]).
(2, 3, 4): Not a geometric sequence.
Given an array of integers and a common ratio r, find all triplets of indexes (i, j, k) that follow a 
geometric sequence for i < j < k. It's possible to encounter duplicate triplets in the array.

Example:
Input: nums = [2, 1, 2, 4, 8, 8], r = 2
Output: 5
"""

# Hash Set Problems 

"""
Problem 3: Verify Sudoku Board
Given a partially completed 9×9 Sudoku board, determine if the current state of the board adheres to the rules of the game:
Each row and column must contain unique numbers between 1 and 9, or be empty (represented as 0).
Each of the nine 3×3 subgrids that compose the grid must contain unique numbers between 1 and 9, or be empty.
Note: You are asked to determine whether the current state of the board is valid given these rules, not whether the board is solvable.
"""
def verify_sudoku_board(board: List[List[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    sub_grid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
      for c in range(9):
        num = board[r][c]
        if num == 0:
          continue
        if num in row_sets[r]:
          return False
        if num in column_sets[c]:
          return False
        if num in sub_grid_sets[r // 3][c // 3]:
          return False
        row_sets[r].add(num)
        column_sets[c].add(num)
        sub_grid_sets[r//3][c//3].add(num)
        
    return True


"""
Problem 4:
Zero Striping
For each zero in an m x n matrix, set its entire row and column to zero in place.
"""
def zero_striping(matrix: List[List[int]]) -> None:
    zero_cols, zero_rows = set(), set()

    if not matrix or not matrix[0]:
        return 

    row_len, col_len = len(matrix), len(matrix[0])

    for r in range(row_len):
        for c in range(col_len):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
                
    for r in range(row_len):
        for c in range(col_len):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

                
"""
Problem 5: Longest Chain of Consecutive Numbers
Find the longest chain of consecutive numbers in an*array. Two numbers are consecutive if they have a difference of 1.
Example:
Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4
"""