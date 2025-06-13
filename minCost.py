class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

    
        memo = {}
        def backtracking(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(backtracking(i+1), backtracking(i+2))
            return memo[i]
        return min(backtracking(0), backtracking(1))


        
