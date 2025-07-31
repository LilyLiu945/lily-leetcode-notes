# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1 & 2: node has at most one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: node has two children
            # Find successor (smallest in right subtree)
            min_larger_node = self.getMin(root.right)
            root.val = min_larger_node.val  # Replace value
            # Delete the successor node recursively
            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node