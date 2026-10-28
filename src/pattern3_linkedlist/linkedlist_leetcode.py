from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2

        return dummy.next

        # 83. Remove Duplicates from Sorted List
        def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
            current = head
            if head == None:
                return head
            while current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    current = current.next
            return head