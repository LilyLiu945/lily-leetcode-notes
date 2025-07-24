# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        res = []

        def dfs(node, path):
            if not node:
                return

            # Append current node's value to the path
            path += str(node.val)

            # If it's a leaf node, add the path to result
            if not node.left and not node.right:
                res.append(path)
                return

            # If not a leaf, continue DFS with updated path
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res
