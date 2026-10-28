from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Linked List Reversal    
    def linked_list_reversal(self, head: ListNode) -> ListNode:
        curr_node, prev_node = head, None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node 
            curr_node = next_node 
        return prev_node

    # Remove the Kth Last Node From a Linked List
    def remove_kth_last_node(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head 
        for _ in range(k):
            if fast == None:
                return head
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    # Intersection of two linked list 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA

            # can be written as 
            # a = a.next if a else headB
            # b = b.next if a else headA

        return a