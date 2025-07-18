# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root # Pointer to current node
        
        while curr or stack:
            # Step 1: Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # Step 2: Left is done, now pop from stack    
            curr = stack.pop() # Pop the last unvisited node
            res.append(curr.val) # Visit the node (in-order: after left)
            
            # Step 3: Move to right child
            curr = curr.right # Now explore the right subtree
        return res
