# 26. Remove Duplicates from Sorted Array and return size of the array
class TwoPointersLeetcode:
    def remove_duplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[k - 1]):
                nums[k] = nums[i] # second and first position not same 
                k += 1
        del nums[k:]
        return k

two_point = TwoPointersLeetcode()
print(two_point.remove_duplicates([1, 4, 5, 5, 66]))