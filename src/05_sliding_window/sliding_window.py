class Solution:
    # 643. Maximum Average Subarray I
    def findMaxAverage(self, nums: list[int], k: int) -> float:
       left = 0
       max_avg = float('-inf')
       window_sum = 0
       
       if len(nums) <= k:
        return sum(nums) / k

       for right in range(len(nums)):
        window_sum += nums[right]
        if right - left + 1 == k:
            curr_avg = window_sum / k
            max_avg = max(max_avg, curr_avg)
            window_sum-=nums[left]
            left+=1
       return max_avg

    # 576. Permutation in String
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

    # 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left = 0
        window_sum = 0
        count = 0
        for right in range(len(arr)):
            # current window sum up to right index
            window_sum += arr[right]
            average = window_sum / k 

            # sliding window, matching length of k and moves left and updates window_sum
            if right - left + 1 == k:
                if average >= threshold:
                    count+=1
                window_sum -= arr[left]
                left+=1
        return count


def main():
    s = Solution()

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

if __name__ == '__main__':
    main()
