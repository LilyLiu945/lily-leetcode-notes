# If current node < low, discard left subtree and recurse on right
# If current node > high, discard right subtree and recurse on left
# Otherwise, trim both sides and keep current node

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
