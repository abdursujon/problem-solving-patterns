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
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
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

        # 21. Merge Two Sorted Lists
        def mergeTwoLists(
            self, list1: ListNode | None, list2: ListNode | None
        ) -> ListNode | None:
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
