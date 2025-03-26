# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        

        def getDepth(root):
            if not root:
                return 0
            
            left_depth = getDepth(root.left)
            right_depth = getDepth(root.right)
            if abs(right_depth-left_depth) > 1:
                self.isBalanced = False

            return 1 + max(left_depth, right_depth)


        getDepth(root)

        return self.isBalanced
        
