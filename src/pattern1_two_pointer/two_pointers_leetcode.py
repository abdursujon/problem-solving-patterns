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
            right-=

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
# 11. Container With Most Water
# 881. Boats to Save People

# ===== Unidirectional traversal =====
# --- Easy ---
# 283. Move Zeroes
# 392. Is Subsequence
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
