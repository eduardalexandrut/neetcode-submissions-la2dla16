# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        back = None

        while front:
            temp = front.next
            front.next = back
            back = front
            front = temp


        return back

            
