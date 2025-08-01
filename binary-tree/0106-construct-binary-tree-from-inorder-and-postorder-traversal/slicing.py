# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)

        index = inorder.index(root_val)

        # Note the sequence: Construct the right subtree first, then the left subtree
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])

        return root
