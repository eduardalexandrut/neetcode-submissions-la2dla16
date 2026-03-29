# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = prev = ListNode()
        dummy.next = head
        succ = head
        length = n

        #Move succ n positions forward
        while length > 0:
            succ = succ.next
            length -= 1

        while succ:
            prev = prev.next
            succ = succ.next

        prev.next = prev.next.next

        return dummy.next
            
        