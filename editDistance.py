class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)
        if m > n:
            word1, word2 = word2, word1
            n, m = m, n

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        
        for i in range(1, n+1):
            for j in range(1, j+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )
        return dp[n][m]

