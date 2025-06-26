# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
        
# Solution Summary:
# - Use a dummy node to simplify head removal cases.
# - Traverse the list with two pointers: `prev` (tracks last safe node) and `curr` (scans current node).
# - When curr.val == val, skip the node by setting `prev.next = curr.next`.
# - Otherwise, move `prev` forward.
# - In all cases, `curr` continues moving forward until the end.
