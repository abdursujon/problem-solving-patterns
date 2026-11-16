class FixedLengthSlidingWindow:
    #============= Easy Leetcode =============# 
    # 643. Maximum Average Subarray I
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        left = 0
        max_sum = window_sum 
        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[left]
            max_sum = max(window_sum, max_sum)
            left+=1
        return max_sum / k


     #============= Medium Leetcode =============# 
