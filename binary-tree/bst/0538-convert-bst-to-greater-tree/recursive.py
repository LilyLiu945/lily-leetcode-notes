# Traverse the tree in reverse inorder (right -> root -> left)
# Accumulate sum in a variable (self.total)
# Update each node's value with total so far

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        self.total = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)        # Visit right subtree
            self.total += node.val             # Accumulate sum
            node.val = self.total              # Update current node
            reverse_inorder(node.left)         # Visit left subtree

        reverse_inorder(root)
        return root
