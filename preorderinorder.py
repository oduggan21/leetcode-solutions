# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
         
        if not preorder or not inorder:
            return None
        
        val = preorder[0]
        newNode = TreeNode(val)

        index_inorder = inorder.index(val)

        newNode.left = self.buildTree(preorder[1:index_inorder+1], inorder[:index_inorder])
        

        newNode.right = self.buildTree(preorder[index_inorder+1:], inorder[index_inorder+1:])

        return newNode

