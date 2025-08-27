# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0
            lt, ls = dfs(node.left) # lt: left-take, ls: left-skip
            rt, rs = dfs(node.right) # rt: right-take, rs: right-skip
            take = node.val + ls + rs
            skip = max(lt, ls) + max(rt, rs)
            return take, skip
        
        take, skip = dfs(root)
        return max(take, skip)
