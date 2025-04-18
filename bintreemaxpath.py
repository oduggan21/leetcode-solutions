# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_total = float('-inf')

        def recursiveFunction(root):
            if not root:
                return 0
            
            value_left = recursiveFunction(root.left)
            value_right = recursiveFunction(root.right)
            greater_side = max(value_left, value_right)
            total_three = value_left + value_right +root.val
            max_three = max(total_three, greater_side+root.val)
            max_three = max(max_three, root.val)


            self.max_total = max(self.max_total, max_three)

            return max(root.val, greater_side+root.val)
        
        recursiveFunction(root)
        return self.max_total
