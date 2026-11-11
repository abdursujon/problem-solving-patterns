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
