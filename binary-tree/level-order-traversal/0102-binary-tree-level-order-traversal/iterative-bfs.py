# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root]) # BFS uses a queue (FIFO)
        
        while queue:
            level = [] # Holds current level's node values
            
            for _ in range(len(queue)): # Only process nodes of the current level
                node = queue.popleft()
                level.append(node.val)

                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(level) # Add current level to result
        return res
