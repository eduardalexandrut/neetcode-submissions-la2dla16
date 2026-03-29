# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        s1 = []
        s2 = []

        temp = l1
        while temp:
            s1.append(temp.val)
            temp = temp.next
        
        temp = l2
        while temp:
            s2.append(temp.val)
            temp = temp.next
        
        while len(s1) > 0:
            num1 += str(s1.pop())
        
        while len(s2) > 0:
            num2 += str(s2.pop())
        
        tot = str(int(num1) + int(num2))

        reversed_tot = tot[::-1]
        print(reversed_tot)

        head = ListNode(reversed_tot[0])
        temp = head
        for s in reversed_tot[1:]:
            temp.next = ListNode(s)
            temp = temp.next
        return head