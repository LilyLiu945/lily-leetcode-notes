"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
            
        curr = root # Pointer to current level
        while curr:
            dummy = Node(0) # Dummy head for the next level
            tail = dummy # Tail tracks the end of the next level

            # Traverse the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                    
                curr = curr.next # Move to next node in the same level
            # Move down to the next level
            curr = dummy.next # Start from the leftmost node of the next level
        return root
