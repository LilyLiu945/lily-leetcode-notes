# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        self.total = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)        # Visit right subtree
            self.total += node.val             # Accumulate sum
            node.val = self.total              # Update current node
            reverse_inorder(node.left)         # Visit left subtree

        reverse_inorder(root)
        return root
