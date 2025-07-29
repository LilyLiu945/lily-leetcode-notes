# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1
        
        # Use a queue to store node pairs
        queue = deque([(root1, root2)])
        
        while queue:
            node1, node2 = queue.popleft()
            # Merge values
            node1.val += node2.val
            
            # Merge left children
            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left  # take node2's subtree
            
            # Merge right children
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right
        
        return root1  # root1 is now the merged tree
