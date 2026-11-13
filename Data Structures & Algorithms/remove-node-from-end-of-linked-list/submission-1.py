# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current != None:
            length += 1
            current = current.next

        count = length - n + 1
        current = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        counter = 0
        while current != None:
            counter += 1
            if counter == count:
                prev.next = current.next
            prev = current
            current = current.next
        
        return dummy.next
        