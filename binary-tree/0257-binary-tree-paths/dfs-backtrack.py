# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []

        def backtrack(node, path):
            if not node:
                return

            # Add current node value to the path
            path.append(str(node.val))

            # If it's a leaf node, join the path into a string and add to result
            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                # Continue DFS traversal for left and right children
                backtrack(node.left, path)
                backtrack(node.right, path)

            # Backtrack: remove the current node value before returning
            path.pop()

        # Start backtracking from the root with an empty path
        backtrack(root, [])
        return res
