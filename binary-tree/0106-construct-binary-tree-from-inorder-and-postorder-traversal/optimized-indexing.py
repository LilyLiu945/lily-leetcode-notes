# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(post_left, post_right, in_left, in_right):
            if post_left > post_right:
                return None
            
            root_val = postorder[post_right]
            root = TreeNode(root_val)

            index = inorder_index_map[root_val]
            left_size = index - in_left

            root.left = helper(post_left, post_left + left_size - 1, in_left, index - 1)
            root.right = helper(post_left + left_size, post_right - 1, index + 1, in_right)
            
            return root
        
        return helper(0, len(postorder)-1, 0, len(inorder)-1)
