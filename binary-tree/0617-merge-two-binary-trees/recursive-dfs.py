# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If either tree is empty, return the other one
        if not root1:
            return root2
        if not root2:
            return root1

        # Merge current nodes
        merged = TreeNode(root1.val + root2.val)
        # Recursively merge left and right children
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged
