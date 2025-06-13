class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def backtracking(path):
            if path > n:
                return 0
            elif path == n:
                return 1
            elif path in memo:
                return memo[path]
            memo[path] = backtracking(path+1) + backtracking(path+2)
            return memo[path]
        return backtracking(0)

