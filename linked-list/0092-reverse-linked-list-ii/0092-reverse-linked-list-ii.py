# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        pre = dummy

        # 1) move `pre` to the node right before the `left`-th node
        for _ in range(left - 1):
            pre = pre.next

        # 2) `cur` points to the first node of the sublist to reverse
        cur = pre.next

        # 3) head-insertion: take `next_node` after `cur` and insert it right after `pre`
        for _ in range(right - left):
            next_node = cur.next          # node to move to the front of the sublist
            cur.next = next_node.next     # unlink next_node from its current place
            next_node.next = pre.next     # place next_node right after pre
            pre.next = next_node          # now next_node is at the front of the reversed part

        return dummy.next
