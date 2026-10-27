from collections import Counter
class HashingProblemSolving:
    # ==== 5 Easy =====
    '''
    Problem 1:
    Given an array nums containing n integers in the range [0, n] without any duplicates, 
    return the single number in the range that is missing from nums.
    '''
    def missingNumber(self, nums) -> int:
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
    Unique Email Addresses, NeetCode 150 hashing problems 
    '''
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()
        for e in emails: 
            local, domain = e.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            valid = local + "@" + domain
            unique.add(valid)
        return len(unique)


    '''
    Problem 4:
    Isomorphic Strings
    You are given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the 
    order of characters. No two characters may map to the same character, but a character may map to itself.
    Example 1:
    Input: s = "egg", t = "add"
    Output: true
    '''
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_index_map, t_index_map = {}, {}
        for i in range(len(s)):
            if s[i] not in s_index_map:
                s_index_map[s[i]] = i
            if t[i] not in t_index_map:
                t_index_map[t[i]] = i
            if s_index_map[s[i]] != t_index_map[t[i]]:
                return False 
        return True 
    

    '''
    Problem 5:
    You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i in range(len(nums)):
            temp_num = nums[i]
            complement = target - temp_num
            if complement in nums_map:
                return [nums_map[complement], i]
            nums_map[temp_num] = i
        return [-1, -1]


    '''
    Problem 6: 290. Word Pattern
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
    '''
    def wordPattern(self, patterns: str, s: str) -> bool:
       words = s.split()
       if len(patterns) != len(words):
        return False
       word_to_pattern = {}
       pattern_to_word = {}
       for pattern, word in zip(patterns, words):
        # if previously stored word not equal to current word 
        if pattern in pattern_to_word and pattern_to_word[pattern] != word:
            return False
        # if previously stored pattern not equal to current pattern for this word, means pattern is mappig to different words 
        if word in word_to_pattern and word_to_pattern[word] != pattern:
            return False
        word_to_pattern[word] = pattern
        pattern_to_word[pattern] = word

       return True

    '''
    Problem 7: 350. Intersection of Two Arrays II
    '''
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        freq = dict(Counter(nums1))
        """ Steps: 
        - nums2 = [2, 2]
        - for index 0 = 2 if 2 is in freq? 
        - if so reduce by 1 and add 2 two the res
        - if index 1 = 2 if 2 is in freq? 
        - if so reduce by 1 and add 2 two the res
        - return res
        """
        for i in range(len(nums2)):
            if nums2[i] in freq and freq[nums2[i]] > 0: # you can't reduce more than how many item that exist in freq
                freq[nums2[i]] -= 1
                res.append(nums2[i])
            else:
                continue
        return res

    '''
    Problem 8: 409. Longest Palindrome
    '''
    def longestPalindrome(self, s: str) -> int:
        odd_found = False
        mp = dict(Counter(s))
        length = 0
        for count in mp.values():
            if count % 2 == 0:
                length += count
            if count % 2 != 0:
                length += count - 1
                odd_found = True
        if odd_found:
            length += 1
        return length

    '''
    Problem 9: 1346. Check If N and Its Double Exist
    '''
    def checkIfExist(self, arr: list[int]) -> bool:
        # store value:index
        # for i in range all keys, check if there is a key which is half the current key and not same index
        # if found return true 
        # return false
        mp = {}
        for i, num in enumerate(arr):
            mp[num] = i
        for i, num in enumerate(arr):
            complement = num / 2
            if complement in mp and mp[complement] != i:
                return True
        return False

    '''
    Problem 10:
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