from typing import List
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

    return ''.join(letters)

    
# 344. Reverse String 
def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right= len(s) -1
        while left < right:
            temp = s[left]
            s[left]=s[right]
            s[right] = temp
            left+=1
            right-=1


# 680. Valid Palindrome II 
def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                string1 = s[:left] + s[left+1:]
                string2 = s[:right] + s[right+1:]
                return string1 == string1[::-1] or string2 == string2[::-1]
            else:
                left+=1
                right-=1
        return True

    
# 4030. Check ASCII Palindromic
def isPalindromic(self, s: str) -> bool:
    char_int = []
    for ch in s:
        char_int.append(ord(ch))
    binary = []
    for n in char_int:
        d = format(n, '08b')
        binary.append(d)
    binary_string = ''.join(binary)
    
    left = 0
    right = len(binary_string) - 1
    while left < right:
        if binary_string[left] != binary_string[right]:
            return False
        else:
            left+=1
            right-=1
    return True


# --- Medium ---
# 167. Two Sum II - Input Array Is Sorted
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left+1, right+1]
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
                left+=1
                right-=1
            elif triplet_sum > 0:
                right-=1
            else:
                left+=1
                
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
            left+=1
            right-=1
    return max_water 


# 881. Boats to Save People
def numRescueBoats(self, p: list[int], limit: int) -> int:
        p.sort()
        l,r=0,len(p)-1
        c=0
        while l<=r:
            if p[l]+p[r]<limit:
                c+=1
                l+=1
                r-=1
            elif p[l]+p[r]>limit:
                c+=1
                r-=1
            else:
                c+=1
                l+=1
                r-=1
        return c

# ===== Unidirectional traversal =====

# --- Easy ---
# 283. Move Zeroes
def shift_zeros_to_the_end(nums: List[int]) -> None:
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


# 392. Is Subsequence
def isSubsequence(self, s: str, t: str) -> bool:
    sp = tp = 0
    while(sp < len(s) and tp < len(t)):
        if s[sp] == t[tp]:
            sp += 1
        tp +=1
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
