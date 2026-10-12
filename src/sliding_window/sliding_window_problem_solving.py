class SlidingWindowProblemSolving:
    # ==== 5 Easy =====
    '''
    Problem 1:
    Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
    Note: A subarray is a contiguous part of any given array.
    '''
    def maxSubarraySum(self, arr, k):
        if (len(arr) < k):
            return -1

        # first window 
        curr_sum = sum(arr[:k])
        max_sum = curr_sum

        # sliding window 
        for i in range(k, len(arr)):
            curr_sum = curr_sum - arr[i - k] + arr[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum

    '''
    Problem 2:
    '''

    '''
    Problem 3:
    '''

    '''
    Problem 4:
    '''

    '''
    Problem 5:
    '''

    # ==== 10 Medium ====
    '''
    Problem 1:
    '''

    '''
    Problem 2:
    '''

    '''
    Problem 3:
    '''

    '''
    Problem 4:
    '''

    '''
    Problem 5:
    '''

    '''
    Problem 6:
    '''

    '''
    Problem 7:
    '''

    '''
    Problem 8:
    '''

    '''
    Problem 9:
    '''

    '''
    Problem 10:
    '''

    # ==== 5 Hard ====
    '''
    Problem 1:
    '''

    '''
    Problem 2:
    '''

    '''
    Problem 3:
    '''

    '''
    Problem 4:
    '''

    '''
    Problem 5:
    '''