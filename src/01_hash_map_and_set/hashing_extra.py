"""Hash map and hash set problems.

Part 1 covers the book Coding Interview Patterns by Alex Xu and Shaun.
Part 2 covers LeetCode / NeetCode hashing problems.
"""

from collections import Counter

# ==================== Part 1: Coding Interview Patterns ====================

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


def pair_sum_unsorted(nums: list[int], target: int) -> list[int]:
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


def verify_sudoku_board(board: list[list[int]]) -> bool:
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
            sub_grid_sets[r // 3][c // 3].add(num)

    return True


"""
Problem 4:
Zero Striping
For each zero in an m x n matrix, set its entire row and column to zero in place.
"""


def zero_striping(matrix: list[list[int]]) -> None:
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


# ==================== Part 2: LeetCode ====================
class HashingProblemSolving:
    # ==== 5 Easy =====
    """
    Problem 1:
    Given an array nums containing n integers in the range [0, n] without any duplicates,
    return the single number in the range that is missing from nums.
    """

    def missingNumber(self, nums) -> int:
        num_set = set()
        limit = max(nums) + 1

        for i in range(0, limit):
            num_set.add(i)

        for num in num_set:
            if num not in nums:
                return num
            else:
                continue

        return max(nums) + 1

    """
    Problem 2: Maximum Number of Balloons
    You are given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
    You can use each character in text at most once. Return the maximum number of instances that can be formed.
    """

    def maxNumberOfBalloons(self, text):
        count = {}
        for t in text:
            if t not in "balon":
                continue
            count[t] = count.get(t, 0) + 1

        result = 0
        need = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        while all(count.get(k, 0) >= need[k] for k in need):
            for k in need:
                count[k] -= need[k]
            result += 1

        return result

    """
    Problem 3:
    Unique Email Addresses, NeetCode 150 hashing problems 
    """

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            valid = local + "@" + domain
            unique.add(valid)
        return len(unique)

    """
    Problem 4:
    Isomorphic Strings
    You are given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the 
    order of characters. No two characters may map to the same character, but a character may map to itself.
    Example 1:
    Input: s = "egg", t = "add"
    Output: true
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index_map, t_index_map = {}, {}
        for i in range(len(s)):
            if s[i] not in s_index_map:
                s_index_map[s[i]] = i
            if t[i] not in t_index_map:
                t_index_map[t[i]] = i
            if s_index_map[s[i]] != t_index_map[t[i]]:
                return False
        return True

    """
    Problem 5:
    You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i in range(len(nums)):
            temp_num = nums[i]
            complement = target - temp_num
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[temp_num] = i
        return [-1, -1]

    """
    Problem 6: 290. Word Pattern
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
    """

    def wordPattern(self, patterns: str, s: str) -> bool:
        words = s.split()
        if len(patterns) != len(words):
            return False
        word_to_pattern = {}
        pattern_to_word = {}
        for pattern, word in zip(patterns, words):
            # if previously stored word not equal to current word
            if pattern in pattern_to_word and pattern_to_word[pattern] != word:
                return False
            # if previously stored pattern not equal to current pattern for this word, means pattern is mappig to different words
            if word in word_to_pattern and word_to_pattern[word] != pattern:
                return False
            word_to_pattern[word] = pattern
            pattern_to_word[pattern] = word

        return True

    """
    Problem 7: 350. Intersection of Two Arrays II
    """

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        freq = dict(Counter(nums1))
        """ Steps: 
        - nums2 = [2, 2]
        - for index 0 = 2 if 2 is in freq? 
        - if so reduce by 1 and add 2 two the res
        - if index 1 = 2 if 2 is in freq? 
        - if so reduce by 1 and add 2 two the res
        - return res
        """
        for i in range(len(nums2)):
            if (
                nums2[i] in freq and freq[nums2[i]] > 0
            ):  # you can't reduce more than how many item that exist in freq
                freq[nums2[i]] -= 1
                res.append(nums2[i])
            else:
                continue
        return res

    """
    Problem 8: 409. Longest Palindrome
    """

    def longestPalindrome(self, s: str) -> int:
        odd_found = False
        mp = dict(Counter(s))
        length = 0
        for count in mp.values():
            if count % 2 == 0:
                length += count
            if count % 2 != 0:
                length += count - 1
                odd_found = True
        if odd_found:
            length += 1
        return length

    """
    Problem 9: 1346. Check If N and Its Double Exist
    """

    def checkIfExist(self, arr: list[int]) -> bool:
        # store value:index
        # for i in range all keys, check if there is a key which is half the current key and not same index
        # if found return true
        # return false
        mp = {}
        for i, num in enumerate(arr):
            mp[num] = i
        for i, num in enumerate(arr):
            complement = num / 2
            if complement in mp and mp[complement] != i:
                return True
        return False
