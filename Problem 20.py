# Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # A dummy node helps handle edge cases like removing the head node
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 1: Move 'right' n steps forward
        while n > 0 and right:
            right = right.next
            n = n - 1

        # Step 2: Move both pointers until 'right' reaches the end
        while right:
            left = left.next
            right = right.next
        
        # Step 3: Delete the node (left.next is the node to be removed)
        left.next = left.next.next

        return dummy.next
