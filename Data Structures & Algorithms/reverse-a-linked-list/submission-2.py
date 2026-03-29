# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = next = None

        while curr:
            # Inverti
            next = curr.next
            curr.next = prev

            #Sposti
            prev = curr
            curr = next
        return prev
        

            
