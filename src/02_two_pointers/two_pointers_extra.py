"""Two pointer problems.

Part 1 covers the book Coding Interview Patterns by Alex Xu and Shaun.
Part 2 covers LeetCode two pointer problems.
"""

# ==================== Part 1: Coding Interview Patterns ====================
"""There are three different types of two pointers strategies
1. Inward Traversal Two pointer where left starts at the begining and right starts at the end of the data structure 
2. Unidirection Traversal, often right pointer find information we would like and left pointer keep track of the information
3. Staged Traversal: first pointer is use to search for something then second pointer to find additional information about it 
"""


# If given nums contain duplicate return True otherwise false
def find_duplicate(nums):
    nums.sort()
    left = 0
    for right in range(1, len(nums)):
        if nums[left] == nums[right]:
            return True
        left += 1
    return False


tests = [([134, 52, 31, 3], False), ([3, 4, 2, 2, 3], True)]

for num, expected in tests:
    result = find_duplicate(num)
    print(num, expected, "OK" if result == expected else f"FAIL expected {expected}")

"""Easy"""

"""
Problem 1
Pair Sum - Sorted
Given an array of integers sorted in ascending order and a target value, 
return the indexes of any pair of numbers in the array that sum to the target. 
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.
Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
"""


def pair_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left, right]
        if curr > target:
            right -= 1
        else:
            left += 1

    return []


"""Problem 2
Is Palindrome Valid
A palindrome is a sequence of characters that reads the same forward and backward.
Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. 
A character is alphanumeric if it's either a letter or a number.
Example 1:
Input: s = 'a dog! a panic in a pagoda.'
Output: True
"""


def is_palindrome_valid(s: str) -> bool:
    valid_char = []

    for ch in s:
        if ch.isalnum():
            valid_char.append(ch)
        else:
            continue

    left = 0
    right = len(valid_char) - 1
    while left <= right:
        if valid_char[left] != valid_char[right]:
            return False
        left += 1
        right -= 1

    return True


# Unidirectional Traversal Two Pointer
"""Problem 3
Shift Zeros to the End
Given an array of integers, modify the array in place to move all zeros to the end 
while maintaining the relative order of non-zero elements.
Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]
"""


def shift_zeros_to_the_end(nums: list[int]) -> None:
    left = 0
    for right in range(1, len(nums)):
        temp = 0
        if nums[right] == 0:
            continue
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = 0

        if nums[left] != 0:
            left += 1
        if nums[left] == 0:
            nums[left] = temp


"""Medium"""

"""
Problem 1: Triplet Sum
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . 
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). 
If no such triplets are found, return an empty array.
Each triplet can be arranged in any order, and the output can be returned in any order.
Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]
"""


def triplet_sum(nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    triplets = set()

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                sort_trip = tuple(sorted((nums[i], nums[left], nums[right])))
                triplets.add(sort_trip)
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1
    return [list(triplet) for triplet in triplets]


"""Problem 2
Largest Container
You are given an array of numbers, each representing the height of a vertical line on a graph. 
A container can be formed with any pair of these lines, along with the x-axis of the graph. 
Return the amount of water which the largest container can hold.
"""


def largest_container(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_water = 0

    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_water


# Staged Traversal Two Pointer
"""Problem 3
Next Lexicographical Sequence
Medium
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical order among all possible arrangements, return the arrangement that's first in lexicographical order.

4 Steps to solve this type of problem
1. Find the pivot 
2. If no pivot, reverse the given string else 
2. Swap the pivot with the last value 
3. Reverse everything after pivot 

Similar Leetcode:
31. Next Permutation: the same problem, on an integer array.
556. Next Greater Element III: the same algorithm applied to the digits of a number.
1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number: uses next permutation as a step.
"""


def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    pivot = len(letters) - 2

    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1

    if pivot == -1:
        return "".join(reversed(letters))

    rightmost_successor = len(letters) - 1
    while letters[rightmost_successor] <= letters[pivot]:
        rightmost_successor -= 1

    letters[pivot], letters[rightmost_successor] = (
        letters[rightmost_successor],
        letters[pivot],
    )
    letters[pivot + 1 :] = reversed(letters[pivot + 1 :])

    return "".join(letters)


# ==================== Part 2: LeetCode ====================
# ===== Inward traversal =====


# --- Easy ---
# 345. Reverse Vowels of a String
def reverseVowels(self, s: str) -> str:
    letters = list(s)
    vowels = "aeiouAEIOU"
    left = 0
    right = len(letters) - 1

    while left < right:
        while left < right and letters[left] not in vowels:
            left += 1
        while left < right and letters[right] not in vowels:
            right -= 1
        letters[left], letters[right] = (letters[right], letters[left])
        left += 1
        right -= 1

    return "".join(letters)


# 344. Reverse String
def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


# 680. Valid Palindrome II
def validPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            string1 = s[:left] + s[left + 1 :]
            string2 = s[:right] + s[right + 1 :]
            return string1 == string1[::-1] or string2 == string2[::-1]
        else:
            left += 1
            right -= 1
    return True


# 4030. Check ASCII Palindromic
def isPalindromic(self, s: str) -> bool:
    char_int = []
    for ch in s:
        char_int.append(ord(ch))
    binary = []
    for n in char_int:
        d = format(n, "08b")
        binary.append(d)
    binary_string = "".join(binary)

    left = 0
    right = len(binary_string) - 1
    while left < right:
        if binary_string[left] != binary_string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


# --- Medium ---
# 167. Two Sum II - Input Array Is Sorted
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left + 1, right + 1]
        elif curr > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]


# 15. 3Sum
def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = set()
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            triplet_sum = nums[i] + nums[left] + nums[right]
            if triplet_sum == 0:
                ans.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif triplet_sum > 0:
                right -= 1
            else:
                left += 1

    return list(ans)


# 11. Container With Most Water
def maxArea(self, height: list[int]) -> int:
    # to calculate the max water, the rule is
    # min(left_h_value, right_h_value) * (right - left)
    # first bit before * takes the smaller vertical line,
    # second section after * figure out the width
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        curr_water_amount = min(height[left], height[right]) * (right - left)
        max_water = max(curr_water_amount, max_water)
        # this section fo if else traverse through the entire array by moving left and right if left is smaller
        # then right, it move one step forward, and if left is greater than right, moves right to smaller value if equal both pointer moves
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water


# 881. Boats to Save People
def numRescueBoats(self, p: list[int], limit: int) -> int:
    p.sort()
    l, r = 0, len(p) - 1
    c = 0
    while l <= r:
        if p[l] + p[r] < limit:
            c += 1
            l += 1
            r -= 1
        elif p[l] + p[r] > limit:
            c += 1
            r -= 1
        else:
            c += 1
            l += 1
            r -= 1
    return c


# ===== Unidirectional traversal =====

# --- Easy ---
# 283. Move Zeroes: see shift_zeros_to_the_end in Part 1


# 392. Is Subsequence
def isSubsequence(self, s: str, t: str) -> bool:
    sp = tp = 0
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
    return sp == len(s)


# 844. Backspace String Compare


# --- Medium ---
# 80. Remove Duplicates from Sorted Array II
# 2486. Append Characters to String to Make Subsequence
# 524. Longest Word in Dictionary through Deleting

# ===== Staged traversal =====
# --- Easy ---
# 228. Summary Ranges
# 830. Positions of Large Groups
# 696. Count Binary Substrings

# --- Medium ---
# 443. String Compression
# 1759. Count Number of Homogenous Substrings
# 1578. Minimum Time to Make Rope Colorful
