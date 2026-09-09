'''
The Modified Binary Search pattern involves adapting the classic binary search algorithm to solve various problems, 
often related to searching in a sorted array or finding the boundary of a condition

Usage
    • Sorted Arrays: Perfect for problems involving searching or making decisions based on sorted arrays.
    • Finding Boundaries: Useful for finding the start or end of a condition in a sorted array.
Pros and Cons
    • Pros:
        ◦ Efficiency: Provides a logarithmic time complexity solution for searching problems, making it highly efficient.
        ◦ Versatility: Can be adapted to solve a wide range of problems beyond simple searching.
    • Cons:
        ◦ Applicability: Mainly beneficial for problems involving sorted arrays or conditions with clear boundaries.
        ◦ Implementation Nuances: Requires careful implementation to handle edge cases and avoid infinite loops.
Example Problems from Grokking the Coding Interview
    1. Order-agnostic Binary Search: Given a sorted array of numbers, find the index of a given number. 
    The array could be sorted in ascending or descending order.
    2. Ceiling of a Number: Given an array of numbers sorted in ascending order, find the ceiling of a given number. 
    The ceiling of a number is the smallest number in the given array greater than or equal to the given number.
    3. Next Letter: Given an array of lowercase letters sorted in ascending order, find the smallest letter in 
    the given array greater than a given ‘key’.
'''    


'''
1. Order-agnostic Binary Search: Given a sorted array of numbers, find the index of a given number. 
The array could be sorted in ascending or descending order.
'''
def findTarget(target, nums):
    if(nums == None or len(nums) == 0):
        return -1 
    
    left, right = 0, len(nums) - 1

    # If first element is larger than last element of nums, we know the order is descending 
    if (nums[left] > nums[right]):
        while(left <= right):
            mid = int((left + right) /2)
            curr_val = nums[mid]
            if(curr_val == target):
                return mid
            if(curr_val > target):
                left = mid + 1
            else:
                right = mid - 1

    # Else the sorted array is in ascending order 
    if(nums[left] < nums[right]):
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

# Test the findTarget in both ascending and decending order 
print(findTarget(1, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # Should be 9 (0 index base)
print(findTarget(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Should be 0