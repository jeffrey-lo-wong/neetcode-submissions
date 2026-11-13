# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next
        
        # my first idea is to have one pointer be at the back and do it that way
        # but I'm not sure if that's very efficient 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second != None:
            temp = second.next # save the rest of the list
            second.next = prev # point this node backward
            prev = second  
            second = temp  # move forward

        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


