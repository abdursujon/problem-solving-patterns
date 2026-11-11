class TwoPoinerterInwardTraversal:
  #================== Easy Leetcode ======================#
  # 125. Valid Palindrome
  def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    res = [ch for ch in s if ch.isalnum()]
    pal_str_one = "".join(res)
    pal_str_two = "".join(reversed(res))
    return pal_str_one == pal_str_two

  
  # 917. Reverse Only Letters
  def reverseString(self, s: list[str]) -> None:
      """
      Do not return anything, modify s in-place instead.
      """
      left, right = 0, len(s) - 1
      while left <= right:
          temp = s[left]
          s[left] = s[right]
          s[right] = temp
          left += 1
          right -= 1

        
  # 345. Reverse Vowels of String
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

    
  # 680. Valid Palindrome II
  def validPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left <= right:
        if s[left] != s[right]:
            string1 = s[:left] + s[left+1:]
            string2 = s[:right] + s[right+1:]
            return string1 == string1[::-1] or string2 == string2[::-1]
        left+=1
        right-=1
    return True

  
  # 917. Reverse Only Letters
  def reverseOnlyLetters(self, s: str) -> str:
  left, right = 0, len(s) - 1
  l = list(s)
  while left < right: 
      if l[left].isalpha() and l[right].isalpha():
          temp = l[left]
          l[left] = l[right]
          l[right] = temp 
          left+=1
          right-=1
      elif l[left].isalpha() == False:
          left+=1
      elif l[right].isalpha() == False:
          right-=1

  s = ''.join(l)
  return s

  
  #================== Medium Leetcode ====================#
  # 167. Two Sum II - Input Array is Sorted
  # 11. Contain With Most Water 
  # 15. 3Sum 
  # 16. 3Sum Closest 
  # 881. Boats to Save People 
