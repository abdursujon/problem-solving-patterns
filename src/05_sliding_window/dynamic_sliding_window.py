"""
A generic template for dynamic sliding window finding max window length
"""
def longest_window(nums, condition):
    i = 0
    max_length = 0
    result = None

    for j in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Shrink the window if the condition is violated
        while not condition():  
            # Shrink the window from the left
            # Remove nums[i] from the current window logic
            i += 1

        # Update the result if the current window is larger
        if j - i + 1 > max_length:
            max_length = j - i + 1
            # Add business logic to update result

    return result


''' HOW MOST DYNAMIC SLIDING WINDOW SUBSTRING PROBLEM LOOKS LIKE 
# three variable 

# for loop
    # expand the window which add arr[j] to current window 
    
    # shrink the window if the condition is violated 

    # update the window if curr window is lorger/smaller

# return the count
'''

# 3. Longest Substring Without Repeating Characters
# 209. Minimum Size Subarray Sum
# 424. Longest Repeating Character Replacement
# 904. Fruit Into Baskets
# 1004. Max Consecutive Ones III
# 1493. Longest Subarray of 1's After Deleting One Element
# 713. Subarray Product Less Than K
# 1658. Minimum Operations to Reduce X to Zero
# 1358. Number of Substrings Containing All Three Characters
# 1838. Frequency of the Most Frequent Element