# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
 

    def serialize(self, root):
        
        if not root:
            return ""
        
        seq = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                seq.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                seq.append('null')
        
        result = ','.join(seq)
        return result

        

    def deserialize(self, data):
        if not data:
            return None
        
        lst = data.split(',')
        root = TreeNode(int(lst[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if lst[i] != 'null':
                node.left = TreeNode(int(lst[i]))
                queue.append(node.left)
            i += 1
            if lst[i] != 'null':
                node.right = TreeNode(int(lst[i]))
                queue.append(node.right)
            i += 1
        
        return root


