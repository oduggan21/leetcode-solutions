# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.val = None
       
        def helper(root, count):

            if not root:
                return None

            left_value = helper(root.left, count)
            if left_value != None: 
                count = left_value
            count += 1
            if count == k:
                self.val = root.val

            right_value = helper(root.right, count)

            if right_value != None:
                count = right_value
            
            return count

        helper(root, 0)
        return self.val

