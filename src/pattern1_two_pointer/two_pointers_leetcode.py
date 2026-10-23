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