"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if not node:
                return None
            if id(node) in visited:
                return visited[id(node)]       
            new_node = Node(node.val)
            visited[id(node)] = new_node
            for neighbor in node.neighbors:
                    new_node.neighbors.append(dfs(neighbor))
           
            
            return new_node
        
        return dfs(node)




        
