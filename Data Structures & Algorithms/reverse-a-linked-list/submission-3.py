# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = mid = None
        front = head

        while front:
            print(front.val)
            mid = front
            front = front.next

            mid.next = prev
            prev = mid

        return prev
        

            
