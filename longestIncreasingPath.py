class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0

        j = len(matrix[0])
        n = len(matrix)
        max_path = 0

        dp = [[0] * j for _ in range(n)]
    

        def recurs(i, k):
            if dp[i][k] : 
                return dp[i][k]

            best = 1
            for ji, jk in ((1,0), (0,1), (-1, 0), (0, -1)):
                ni, nj = i+ji, k+jk
                if 0 <= ni < n and 0 <= nj < j and matrix[ni][nj] > matrix[i][k]:
                    best = max(best, 1 + recurs(i+ji, k+jk))
            dp[i][k] = best
            return dp[i][k]
        
        for i in range(n):
            for k in range(j):
                max_path = max(max_path, recurs(i, k))

        return max_path
