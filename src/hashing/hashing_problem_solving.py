class HashingProblemSolving:
    # ==== 5 Easy =====
    '''
    Problem 1:
    Given an array nums containing n integers in the range [0, n] without any duplicates, 
    return the single number in the range that is missing from nums.
    '''
    def missingNumber(nums) -> int:
        num_set = set()
        limit = max(nums) + 1

        for i in range(0, limit):
            num_set.add(i)

        for num in num_set:
            if num not in nums:
                return num
            else:
                continue
                
        return max(nums) + 1

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