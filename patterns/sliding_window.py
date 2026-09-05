'''
The Sliding Window pattern involves creating a ‘window’ over a portion of data and sliding it across to solve problems efficiently. 
This technique is particularly useful for array or list-based problems where you need to find or calculate something among all
the contiguous subarrays or sublists of a given size.

Usage
Contiguous Subarrays: Ideal for problems that require you to deal with contiguous subarrays or sublists.
Variable Sized Window: Can be adapted for problems where the window size is not fixed and needs to be adjusted based on certain conditions.
Pros and Cons

Pros:
Efficiency: Provides a way to reduce time complexity from O(n^2) to O(n) for specific problems.
Versatility: Can be used for a variety of problems, including maximum sum subarray, smallest subarray with a given sum, 
and longest substring with K distinct characters.

Cons:
Initial Complexity: Understanding how to adjust the window size and when to slide the window can be challenging initially.
Specificity: Mainly beneficial for problems involving contiguous subarrays or sublists.

Example Problems from Grokking the Coding Interview
Maximum Sum Subarray of Size K: Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Fruits Into Baskets: Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket.
Longest Substring with K Distinct Characters: Given a string, find the length of the longest substring in it with no more than K distinct characters.
'''

class SlidingWindow: 

    '''
    Problem where window size k is given 
    Maximum Sum Subarray of Size K: Given an array of positive numbers and a 
    positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
    '''
    def max_sum_of_subarray(self, arr, k):
        
        if(len(arr) < k): 
            return -1

        # Sum of first window 
        current_window_sum = sum(arr[:k])
        max_sum = current_window_sum 
        

        # Sliding window 
        for i in range(k, len(arr)):
            # deduct value of first index and add value of next index arr[i]
            current_window_sum = current_window_sum - arr[i - k] + arr[i]
            max_sum = max(max_sum, current_window_sum)

        return max_sum
        
    
    '''
    Slinding Window where window size is dynamic 
    Fruits Into Baskets: Given an array of characters where each character represents a fruit tree, you are given two baskets,
    and your goal is to put maximum number of fruits in each basket.
    '''

def main(): 
    sw = SlidingWindow()
    print(sw.max_sum_of_subarray([1, 3, 4, 55, 66, 2, 34], 3))

main()

