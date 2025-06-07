class united:
    def __init__(self,size):
        self.parents = list(range(size))
    
    def find(self,num1):
        if self.parents[num1] == num1:
            return num1
        
        return self.find(self.parents[num1])

    def unite(self,num1,num2):

        num1_new = self.find(num1)
        num2_new = self.find(num2)

        self.parents[num1_new] = num2_new


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dq = united(n)

        for a,b in edges:
            dq.unite(a,b)
        
        final_list = set(dq.find(i) for i in range(n))
        return len(final_list)
