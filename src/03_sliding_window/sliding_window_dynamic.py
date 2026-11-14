class DynamicSlidingWindow:
    #=========== Easy Leetcode ==========#
    # 485. Max Consecutive Ones
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l = c = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            curr = r - l + 1
            c = max(c, curr)

        return c
        
        
    # 674. Longest Continuous Increasing Subsequence
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        l = c = 0
        all_e = set(nums)
        
        if len(nums) == 1 or len(all_e) == 1:
            return 1 
        
        for r in range(1, len(nums)):
            if nums[r] <= nums[r - 1]:
                l = r 
            curr = r - l + 1 
            c = max(c, curr)
                
        return c