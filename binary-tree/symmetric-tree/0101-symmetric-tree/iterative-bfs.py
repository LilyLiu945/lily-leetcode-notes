# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(root, root)]) # Start with root paired with itself
        
        while queue:
            t1, t2 = queue.popleft()
            
            # Both nodes are null → symmetric at this position
            if not t1 and not t2:
                continue
                
            # One is null, one is not → not symmetric
            if not t1 or not t2:
                return False
                
            # Values do not match → not symmetric
            if t1.val != t2.val:
                return False
                
            # Enqueue mirror node pairs for further comparison
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
            
        return True
