class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        s = len(s2)

        if n + s != len(s3):
            return False

        dp = [[False] * (s+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n+1):
            for j in range(s+1):
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i-1][j]
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] |= dp[i][j-1]
        return dp[n][s]
        
