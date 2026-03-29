# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        #We find the middle point by using the slow and fast pointer.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Now we have to revert the second half
        second = slow.next#We set second to the start of the second half
        prev = slow.next = None 
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #We merge the 2 halves:
        #We use this condition, because the second half might be shorter and thus reach the end faster.
        first = head
        second = prev#prev will be pointing to the end of the list(begining of second half)
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        