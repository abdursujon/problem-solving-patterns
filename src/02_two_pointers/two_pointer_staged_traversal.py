class TwoPointerInwardTraversal:
    """
    In this approach, we traverse with one pointer, and when it lands on an 
    element that meets a certain condition, we traverse with the second pointer: 
    Similar to unidirectional traversal, both pointers serve different purposes. Here, the first pointer 
    is used to search for something, and once found, a second pointer finds additional information 
    concerning the value at the first pointer.
    
    Difference between Unidirectional and Staged Traversal
    
    Unidirectional: both pointers run through the array in the same pass. The right pointer looks 
    at every element, and the left pointer marks a position, such as where to write next. 
    Neither one waits for the other.
	
    Staged: the second pointer stays put until the first pointer finds something. 
    Only then does the second pointer start, and it does a separate scan that is about that particular element.
    """
    
    
    # 392. Is Subsequence
    def isSubsequence(self, s: str, t: str) -> bool:
        left = right = 0
        while left<len(s) and right<len(t):
            if s[left] == t[right]:
                left+=1
            right+=1
        return left == len(s)
