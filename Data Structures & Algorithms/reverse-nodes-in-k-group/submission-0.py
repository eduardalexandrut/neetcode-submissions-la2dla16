# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break
            
            groupNext = kth.next
            # Reverse

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Update the pointers to connect the reversed group
            tmp = groupPrev.next # This was the old start, now the new end
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next


    def getKth(self, node, k):
        temp = node
        count = 0

        while temp and count < k:
            temp = temp.next
            count += 1
        return temp