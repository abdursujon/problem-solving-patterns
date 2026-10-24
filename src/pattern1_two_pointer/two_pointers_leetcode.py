'''Easy'''

'''
Problem 1: 
Leetcode: 345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''
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

    return ''.join(letters)


'''
Problem 2: 
Leetcode: 
'''

'''
Problem 3: 
Leetcode: 
'''

'''
Problem 4: 
Leetcode: 
'''

'''
Problem 5: 
Leetcode: 
'''

'''Medium'''

'''
Problem 1: 
Leetcode: 
'''

'''
Problem 2: 
Leetcode: 
'''

'''
Problem 3: 
Leetcode: 
'''

'''
Problem 4: 
Leetcode: 
'''

'''
Problem 5: 
Leetcode: 
'''


# ===== Inward traversal =====
# 344. Reverse String
# 125. Valid Palindrome
# 680. Valid Palindrome II
# 345. Reverse Vowels of a String
# 917. Reverse Only Letters
# 541. Reverse String II
# 977. Squares of a Sorted Array
# 905. Sort Array By Parity
# 832. Flipping an Image
# 2697. Lexicographically Smallest Palindrome
# 2108. Find First Palindromic String in the Array

# ===== Unidirectional traversal =====
# 283. Move Zeroes
# 26. Remove Duplicates from Sorted Array
# 27. Remove Element
# 88. Merge Sorted Array
# 392. Is Subsequence
# 349. Intersection of Two Arrays
# 350. Intersection of Two Arrays II
# 1768. Merge Strings Alternately
# 844. Backspace String Compare
# 925. Long Pressed Name
# 2540. Minimum Common Value

# ===== Staged traversal =====
# 2000. Reverse Prefix of Word
# 557. Reverse Words in a String III
# 228. Summary Ranges
# 830. Positions of Large Groups
# 1446. Consecutive Characters
# 696. Count Binary Substrings
# 1869. Longer Contiguous Segments of Ones than Zeros
