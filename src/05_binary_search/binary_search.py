class BinarySearch:
    #============ Easy Leetcode ===============#
    
    #============ Medium Leetcode ===========#
    # 34. Find First and Last Position of Element in Sorted Array
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def binary_search(nums, target, is_searching_left):
            left, right = 0, len(nums) - 1
            index=-1
            
            while left<=right:
                mid = (left+right)//2
                if nums[mid]>target:
                    right = mid -1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    index=mid
                    if is_searching_left:
                        right=mid-1
                    else:
                        left=mid+1
                        
            return index
            
        left=binary_search(nums,target,True)
        right=binary_search(nums,target,False)
        
        return [left,right]
    
