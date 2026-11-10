class Hashing:
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
