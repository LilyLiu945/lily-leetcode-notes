# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left,node.right = node.right,node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root

# Preorder Traversal (root → left → right)
# However, traversal order does not matter in this problem, since we only need to invert every node once
