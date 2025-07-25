# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        # current node, current path sum, path list
        queue = deque([(root, root.val, [root.val])])
        while queue:
            node, total, path = queue.popleft()
            if not node.left and not node.right:
                if total == targetSum:
                    res.append(path)
            if node.left:
                queue.append((node.left, total + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, total + node.right.val, path + [node.right.val]))
        return res
