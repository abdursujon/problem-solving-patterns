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
    Problem 2: Maximum Number of Balloons
    You are given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
    You can use each character in text at most once. Return the maximum number of instances that can be formed.
    '''
    def maxNumberOfBalloons(self, text):
        count = {}
        for t in text:
            if t not in 'balon':
                continue
            count[t] = count.get(t, 0) + 1
            
        result = 0    
        need = {'b': 1, 'a': 1, 'l': 2, 'o':2, 'n': 1}
        while all(count.get(k, 0) >= need[k] for k in need):
            for k in need:
                count[k] -= need[k]
            result += 1
            
        return result

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