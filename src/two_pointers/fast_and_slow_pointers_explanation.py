'''
The Fast & Slow Pointers technique involves two pointers traversing through a data structure at different speeds. 
This ingenious approach is particularly useful in identifying cycles, finding middle elements, and solving various
other problems related to linked lists and arrays.

Usage
    • Cycle Detection: Perfect for identifying cycles in a linked list or array, which is a common interview question.
    • Finding Middle Elements: Efficiently find the middle element of a linked list without knowing the length beforehand.
    • Problem-Specific Solutions: Solve specific problems like finding the start of a cycle in a linked list.
Pros and Cons
    • Pros:
        ◦ Space Efficiency: Achieves solutions without the need for extra space, adhering to O(1) space complexity.
        ◦ Versatility: Applicable to a variety of problems, making it a versatile pattern to know.
    • Cons:
        ◦ Initial Complexity: Understanding how to move the pointers and at what speed can be tricky at first.
        ◦ Specificity: While versatile, it is mostly beneficial for problems related to linked lists and certain array problems.
Example Problems from Grokking the Coding Interview
    1. LinkedList Cycle: Determine if a linked list has a cycle.
    2. Middle of the LinkedList: Find the middle node of a linked list.
    3. Palindrome LinkedList: Check if a linked list is a palindrome.
'''

# 1. LinkedList Cycle: Determine if a linked list has a cycle.
class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None

class FastAndSlowPointer:
    def hasCycle(self, head: ListNode | None) -> bool:
        if(head == None or head.next == None): 
            return False 
        
        slow = head
        fast = head.next

        # loop runs until fast and slow points to same object or fast has no cycle 
        while(fast != slow):
            if(fast.next == None or fast.next.next == None):
                return False
            slow = slow.next
            fast = fast.next.next

        return True 

def main():
    node1, node2, node3, node4, node5 = [ListNode(i) for i in range(1, 6)]
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # We create a cyle by refering node5 back to node2
    node5.next = node2
    
    fast_and_slow = FastAndSlowPointer()
    print(fast_and_slow.hasCycle(node1))

main()
