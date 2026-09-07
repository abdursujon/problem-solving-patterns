'''
Binary search is a classic search algorithm that locates the index of a target value by adjusting the search interval by half within a sorted array. 
'''

'''
Problem 1: Given a sorted integer array without duplicates and an input target, find the index of the target
For example, when target = 3, inputArray = {1, 2, 3, 4, 5, 6, 7}, we should find target index as 2.
'''

def findTarget(target, nums):
    if(nums == None or len(nums) == 0):
        return -1 

    left, right = 0, len(nums) - 1
    
    while(left <= right):
        mid = int((left + right) / 2)
        curr_val = nums[mid]
        
        if(curr_val == target): 
            return mid
        if(curr_val > target):
            right = mid - 1
        else: 
            left = mid + 1 

    return -1

print(findTarget(333, [1, 4, 8, 9, 11, 22, 333]))
