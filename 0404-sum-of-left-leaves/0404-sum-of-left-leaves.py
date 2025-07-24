# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        queue = deque([root])
        while queue:
            node = queue.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res