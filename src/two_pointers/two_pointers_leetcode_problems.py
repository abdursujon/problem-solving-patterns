'''
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
class TwoPointersLeetcode():
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while(left < right):
            left_str = s[left]
            s[left] = s[right]
            s[right] = left_str
            left += 1
            right -= 1
        print(s)

tpLeet = TwoPointersLeetcode()
tpLeet.reverseString(["h","e","l","l","o"])
tpLeet.reverseString(["H","a","n","n","a","h"])