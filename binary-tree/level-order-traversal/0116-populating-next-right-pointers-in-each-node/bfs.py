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
        queue = deque([root])
        while queue:
            prev = None # Used to connect nodes at the same level
            # Traverse all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.next = node # Connect the previous node to the current one
                prev = node # Update prev to the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
             # At the end of the level, the last node's next is already None by default
             # But you can explicitly write: if prev: prev.next = None
        return root
