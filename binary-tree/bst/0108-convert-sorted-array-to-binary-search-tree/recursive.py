# Recursively choose the middle element as the root to maintain balance
# Build left subtree from left half
# Build right subtree from right half
# Stop recursion when left > right (no elements left)

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
