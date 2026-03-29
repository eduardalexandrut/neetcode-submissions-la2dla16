# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        beginning = prev = ListNode()
        beginning.next = head
        succ = head
        count = 0

        while succ:
            succ = succ.next
            count +=1

        pos = count - n
        succ = head

        count = 0
        while succ:
            if count == pos:
                #
                prev.next = succ.next
                #succ = None
            else:
                prev = succ
                succ = succ.next
            count += 1
        return beginning.next
        