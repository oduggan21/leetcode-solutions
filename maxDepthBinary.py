# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        if not root:
            return 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return 1 + max(left_max, right_max)

        #return the max of the left or right + 1 


