class Solution:

    '''Medium'''
    
    # Problem 1: Permutation in String (leetcode 567)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        res = []
        left = 0
        k = len(s1) - 1

        for right in range(k, len(s2)):
            curr_str = s2[left:right+1]
            curr_str = ''.join(sorted(curr_str))
            res.append(curr_str)
            left += 1
            
        if s1 in res:
            return True

        return False 

s = Solution()

# Problem 1: Permutation in String (leetcode 567) Tests 
tests = [
    ("ab", "adafbacdafa", True),
    ("kf", "kndtkadfk", True),
    ("cd", "dfafdacad", False),
    ("dka", "afdafakdaakad", True),
    ("kfadid", "kdfieafakk", False)
]

for s1, s2, expected in tests:
    result = s.checkInclusion(s1, s2)
    print(s1, s2, expected, "OK" if result == expected else f"FAIL expexted {expected}")