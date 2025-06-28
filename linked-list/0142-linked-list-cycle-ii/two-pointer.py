# Solution: Use fast and slow pointers to detect a cycle.
# - 'slow' moves 1 step at a time, 'fast' moves 2 steps.
# - If there is a cycle, they will eventually meet inside the cycle.

# Let:
#   a = distance from head to the cycle's entry
#   b = distance from the entry to the meeting point
#   c = distance from the meeting point back to the entry (so the cycle length is b + c)

# When they meet:
#   slow has traveled a + b
#   fast has traveled 2(a + b)
# Since fast moves in a cycle, extra distance is k * (b + c):
#   2(a + b) = a + b + k(b + c)
# → a = c + (k - 1)(b + c)

# Therefore:
#   If one pointer starts at head, and one at the meeting point,
#   and both move one step at a time,
#   they will meet at the cycle entry after a steps.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            return None  # No cycle

        # Phase 2: Find the entry point of the cycle
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        
        return ptr
