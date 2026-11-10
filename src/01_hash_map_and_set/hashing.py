class Hashing:
  #================ Medium Leetcode ================#
  # 49. Group Anagrams
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      groups = defaultdict(list)
      for s in strs:
          groups[''.join(sorted(s))].append(s)
      return list(groups.values())
