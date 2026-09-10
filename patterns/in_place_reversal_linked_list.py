'''
The standard in-place reversal of a singly linked list in Python uses an iterative approach with O(n) time and O(1) space complexity.  
It involves maintaining three pointers: prev, current, and next, updating the current node's pointer to point to prev in each iteration 
until the list is fully reversed
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

# Trace through {1 > 2 > 3 > None} for clarity 
def in_place_reversal_linked_list(head: ListNode) -> ListNode:
    prev = None 
    curr = head 

    while curr: 
        next_node = curr.next 
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Test our code to check if it works as intended 
head = ListNode(1)
curr = head 
for i in range(2, 11):
    curr.next = ListNode(i)
    curr = curr.next

reversed_head = in_place_reversal_linked_list(head)
curr = reversed_head
while curr:
    print(curr.val)
    curr = curr.next 