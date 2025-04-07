# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val > q.val:
            p,q = q,p

        while(root):
            if root.val < p.val:
                root = root.right
            elif root.val > q.val: 
                root = root.left
            else:
                return root
        return None
