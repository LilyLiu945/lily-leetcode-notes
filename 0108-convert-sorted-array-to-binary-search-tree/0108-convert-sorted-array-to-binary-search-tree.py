# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2  # Choose middle as root for balance
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)   # Build left subtree
            root.right = helper(mid + 1, right) # Build right subtree
            return root

        return helper(0, len(nums) - 1)