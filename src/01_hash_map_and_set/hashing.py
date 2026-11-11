from collections import Counter 
from collections import defaultdict


class Hashing:
  #================ Easy Leetcode ==================#
  # 1. Two Sum
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i in range(len(nums)):
        temp = nums[i]
        complement = target - temp
        if complement in nums_map:
            return [nums_map[complement], i]
        nums_map[temp] = i
    return [-1, -1]

  
  # 242. Valid Anagram
  def isAnagram(self, s: str, t: str) -> bool:
      freq1 = Counter(s)
      freq2 = Counter(t)
      return freq1 == freq2

  
  # 217. Contains Duplicate
  def containsDuplicate(self, nums: list[int]) -> bool:
    freq = Counter(nums)
    for v in freq.values():
        if v > 1:
            return True
    return False 

  
  # 383. Ransom Note
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    freq = Counter(ransomNote)
    freq2 = Counter(magazine)
    
    for k in freq.keys():
        if k not in freq2:
            return False 
        if freq[k] <= freq2[k]:
            continue
        if freq[k] > freq2[k]:
            return False

    return True

  # 205. Isomorphic Strings
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

  
  #================ Medium Leetcode ================#
  # 49. Group Anagrams
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      groups = defaultdict(list)
      for s in strs:
          groups[''.join(sorted(s))].append(s)
      return list(groups.values())

  
  # 128. Longest Consecutive Sequence
  def longestConsecutive(self, nums: list[int]) -> int:
      nums_set = set(nums)
      longest = 0
      for n in nums_set:
          if n - 1 not in nums_set:
              length = 1
              
              while n + length in nums_set:
                  length+=1
              
              longest = max(longest, length)
      return longest


  # 36. Valid Sudoku
  def isValidSudoku(self, board: list[list[str]]) -> bool:
      rows = [[False] * 9 for _ in range(9)] # create a 2d array of 9 rows and 9 column with all false
      cols = [[False] * 9 for _ in range(9)]
      boxes = [[False] * 9 for _ in range(9)]

      for i in range(9):
          for j in range(9):
              if board[i][j] != '.':
                  num = int(board[i][j]) - 1
                  box_index = (i // 3) * 3 + (j // 3) 
                  if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                      return False
                  rows[i][num] = cols[j][num] = boxes[box_index][num] = True
      return True 

    
    # 454. 4Sum II
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        pair_sum_freq = {}
        for a in nums1:
            for b in nums2:
                pair_sum = a + b
                pair_sum_freq[pair_sum] = pair_sum_freq.get(pair_sum, 0 ) + 1
        
        count = 0
        for c in nums3:
            for d in nums4:
                needed = -(c+d)
                count+= pair_sum_freq.get(needed, 0) # if needed found add it's value else 0
        return count
      

    # 1657. Determine if Two Strings Are Close
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_w1 = Counter(word1)
        freq_w2 = Counter(word2)

        sorted_w1 = sorted(freq_w1.values())
        sorted_w2 = sorted(freq_w2.values())

        keys_match = freq_w1.keys() == freq_w2.keys()
        return sorted_w1 == sorted_w2 and keys_match
