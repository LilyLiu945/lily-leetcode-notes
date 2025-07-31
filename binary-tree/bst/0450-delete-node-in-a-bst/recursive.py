# If key < root.val: recurse into left subtree
# If key > root.val: recurse into right subtree
# If key == root.val:
#   - Case 1: No children or only right => return right
#   - Case 2: Only left => return left
#   - Case 3: Two children
#     - Find inorder successor from right subtree (smallest node)
#     - Replace current node’s value with successor
#     - Delete successor from right subtree

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
