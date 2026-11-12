class ArrayProblems:
    #============ Easy Leetcode ================#
        def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs:
            return ""
        n = min(len(s) for s in strs)
        pre =""
        for i in range(n):
            chars = [s[i] for s in strs]
            if all(c == chars[0] for c in chars):
                pre+=chars[0]
            else:
                break 
            
        return pre   
        
        
    #============ Medium Leetcode =============#
    # 75. Sort Colors
    def sortColors(self, nums: list[int]) -> None:
        freq = {0: 0, 1: 0, 2: 0}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        red = freq.get(0)
        white = freq.get(1)
        blue = freq.get(2)
        i = 0
        while red != 0:
            nums[i] = 0
            red -= 1
            i += 1
        while white != 0:
            nums[i] = 1
            white -= 1
            i += 1
        while blue != 0:
            nums[i] = 2
            blue -= 1
            i += 1
