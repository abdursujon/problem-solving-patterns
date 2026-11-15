class UnidirectionalTwoPointer:
  #=================== Easy Leetcode ================#
  # 27. Remove Element (Without Two Pointer 
  def removeElement(self, nums: list[int], val: int) -> int:
    nums[:] = [x for x in nums if x != val]
    return len(nums)
    
  def removeElement(self, nums: list[int], val: int) -> int:
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left+=1
    del nums[left:]

  # 283. Move Zeroes
  def moveZeroes(self, nums: list[int]) -> None:
      left = 0
      for right in range(len(nums)):
          if nums[right] != 0:
              nums[left], nums[right] = nums[right], nums[left]
              left+=1
            
  #=================== Medium Leetcode ==============#

