# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.prev = None
        self.cur_count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Update current count
            if self.prev == node.val:
                self.cur_count += 1
            else:
                self.cur_count = 1

            # Compare with max_count
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.modes = [node.val]
            elif self.cur_count == self.max_count:
                self.modes.append(node.val)

            self.prev = node.val  # update previous value

            inorder(node.right)

        inorder(root)
        return self.modes