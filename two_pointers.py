'''
The Two Pointers technique is a clever strategy used in algorithm design, particularly when dealing with arrays or linked lists. Imagine you have two fingers, and you place each at different ends or positions of an array. These ‘fingers’ or pointers then traverse through the array, helping you to compare, search, or even manipulate the data efficiently.

Usage
    • Ordered Data Structures: This pattern shines when applied to ordered arrays or lists, allowing for intelligent, position-based decisions that can significantly optimize the algorithm.
    • Efficiency: By reducing the need for nested loops, the Two Pointers technique helps in achieving linear time complexity, making your algorithm faster and more efficient.
Pros and Cons
    • Pros:
        ◦ Efficiency: Achieves O(n) time complexity for problems that might otherwise require O(n^2).
        ◦ Simplicity: Once mastered, it provides a straightforward and elegant solution.
    • Cons:
        ◦ Applicability: Mainly beneficial for problems involving sequences or intervals.
        ◦ Initial Complexity: It might take some time to get the hang of this pattern and understand where and how to move the pointers.
Example Problems from Grokking the Coding Interview
    1. Pair with Target Sum: Find a pair in an array that adds up to a specific target sum.
    2. Triplet Sum to Zero: Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
'''

# Pair with Target Sum: Find a pair in an array that adds up to a specific target sum.
def target_sum(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    while(l < r):
        current_sum = nums[l] + nums[r]
        if(current_sum == target):
            return [l, r]
        elif(current_sum < target):
            l += 1
        else: 
            r -= 1
    return [-1, -1]            

print(target_sum([1, 4, 7, 9, 4], 8))     


# Triplet Sum to Zero: Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
