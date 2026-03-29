# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Good solution, but space complexity O(n)
#def hasCycle(self, head: Optional[ListNode]) -> bool:
#        history = set()
#
#        temp = head
#        while temp:
#            if temp.val in history:
#                return True
#            else:
#                history.add(temp.val)
#            temp = temp.next
#        return False
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False