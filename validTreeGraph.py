class unite:
    def __init__(self,size):
        self.parents = list(range(size))
    def find(self,num):
        if self.parents[num] == num:
            return num
        
        return self.find(self.parents[num])
    def united(self,num1, num2):
        num1new = self.find(num1)
        num2new = self.find(num2)

        if num1new == num2new:
            return False
        self.parents[num1new] = num2new
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        uq = unite(n)

        for a, b in edges:
            if not uq.united(a,b):
                return False
        
        return True
