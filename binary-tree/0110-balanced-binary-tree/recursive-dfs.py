# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Base case: an empty tree is balanced with height 0
            if not node:
                return 0

            # Recursively check left and right subtree heights
            left = dfs(node.left)
            right = dfs(node.right)

            # If either subtree is unbalanced, or the height difference is > 1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
                
            # Return current node's height if balanced
            return 1 + max(left, right)

        # Start recursion from root and check if result is not -1 (balanced)
        return dfs(root) != -1
