# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode()
        node = dummy
        nums = []

        for head in lists:
            current = head
            while current:
                nums.append(current.val)
                current = current.next

        nums.sort()
        for n in nums:
            node.next = ListNode(n)
            node = node.next

        return dummy.next