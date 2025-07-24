# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, is_left):
            if not node:
                return 0

            # If this is a leaf node
            if not node.left and not node.right:
                # Return its value only if it's a left leaf
                return node.val if is_left else 0

            # Mark left child as is_left=True, right child as is_left=False
            return dfs(node.left, True) + dfs(node.right, False)

        # Start DFS from root, which is not a left child
        return dfs(root, False)    
