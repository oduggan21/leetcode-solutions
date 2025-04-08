# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.list = []
        self.depth = 0

        def recursiveFunc(root, depth_node):
            if not root:
                return 

            if depth_node >= self.depth:
                self.list.append(root.val)
                self.depth += 1
            
            recursiveFunc(root.right, depth_node+1)
            recursiveFunc(root.left, depth_node+1)
        
        recursiveFunc(root, 0)
        return self.list
            
            

