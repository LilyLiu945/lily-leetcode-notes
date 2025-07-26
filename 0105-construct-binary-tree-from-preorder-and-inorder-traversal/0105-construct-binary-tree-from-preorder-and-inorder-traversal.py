# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # The root node is the first element of the preorder
        root_val = preorder[0]
        root = TreeNode(root_val) 

        # Locate the position of the inorder root and divide the left and right subtrees
        index = inorder.index(root_val)

        # Recursively Construct left and right subtrees
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])

        return root