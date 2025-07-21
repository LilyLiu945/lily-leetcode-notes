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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        leftmost = root # Start from the top level (root)
        
        # Since it's a perfect binary tree, if leftmost has a left child, it must also have a right child
        while leftmost.left:
            head = leftmost # Pointer to traverse the current level
            
            while head:
                # Connect the left and right child of the same parent
                head.left.next = head.right
                
                # Connect right child to the next subtree's left child, if it exists
                if head.next:
                    head.right.next = head.next.left
                    
                # Move to the next node in the same level
                head = head.next
                
            # Move down to the next level (always the leftmost node)
            leftmost = leftmost.left
        return root
