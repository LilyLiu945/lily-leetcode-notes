# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast.next: # When 'fast' reaches the end, 'slow' will be at the node before the one to remove
            slow = slow.next
            fast = fast.next
      
        slow.next = slow.next.next

        return dummy.next # Return dummy.next instead of head, because head might have been deleted
