# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_depth = 0

        def depth(root):
            if not root:
                return 0
            
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            self.max_depth = max(self.max_depth, left_depth+right_depth)

            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return self.max_depth
  

