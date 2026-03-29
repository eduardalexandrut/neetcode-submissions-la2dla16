# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first, second = dummy, dummy

        # Move the first pointer to the position of the node to be removed
        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next