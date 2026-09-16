'''
The Two Pointers technique is a clever strategy used in algorithm design, particularly when dealing with arrays or linked lists. 
Imagine you have two fingers, and you place each at different ends or positions of an array.
These ‘fingers’ or pointers then traverse through the array, helping you to compare, search, or even manipulate the data efficiently.

Usage
    • Ordered Data Structures: This pattern shines when applied to ordered arrays or lists, allowing for intelligent,
    position-based decisions that can significantly optimize the algorithm.
    • Efficiency: By reducing the need for nested loops, the Two Pointers technique helps in achieving linear 
    time complexity, making your algorithm faster and more efficient.
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
class TwoPointers: 
    def find_target_sum(self, arr, target): 
        left, right = 0, len(arr) - 1 
        while(left < right): 
            current_sum = arr[left] + arr[right]
            if(current_sum == target): 
                return [left, right]
            if(target > current_sum): 
                left += 1
            else: 
                right -= 1
        return [-1, -1]

def main():
    pointer = TwoPointers()
    print(pointer.find_target_sum([1, 33, 89, 33, 12, 33], 66))
    print(pointer.find_target_sum([1, 33, 89, 33, 12, 33], 100))

main()
# Triplet Sum to Zero: Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
