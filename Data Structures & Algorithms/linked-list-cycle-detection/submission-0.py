# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        history = set()

        temp = head
        while temp:
            if temp.val in history:
                return True
            else:
                history.add(temp.val)
            temp = temp.next
        return False
        