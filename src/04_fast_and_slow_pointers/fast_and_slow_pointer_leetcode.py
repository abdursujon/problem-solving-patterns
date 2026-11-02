class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

"""Slow and Fast Pointer"""
class Solution:
    # 141 LinkedList Cycle 
    def linked_list_loop(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False 


    # 202. Happy Number 
    def isHappy(self, n: int) -> bool:
        def get_sqaure_sum(n:int)->int:
            sum = 0
            while n > 0:
                last_digit = n % 10
                n //= 10 # remaining part of the digit n
                sum+=last_digit**2
            return sum
        
        slow = fast = n 
        while True:
            slow = get_sqaure_sum(slow)
            fast = get_sqaure_sum(get_sqaure_sum(fast))
            if fast == 1:
                return True
            
            # cycle detected 
            elif slow == fast:
                return False

            
    # 876. Middle of the LinkedList     
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow