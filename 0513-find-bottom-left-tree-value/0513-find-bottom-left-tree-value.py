# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        self.max_depth = -1
        self.leftmost_val = 0

        def dfs(node, depth):
            if not node:
                return

            # If it's the first node at a new depth level
            if depth > self.max_depth:
                self.max_depth = depth
                self.leftmost_val = node.val
                
            # Prioritize left children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.leftmost_val