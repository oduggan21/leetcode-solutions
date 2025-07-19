class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [1] + [0] * m

        for ch in s:
            for j in range(m-1, -1, -1):
                if ch == t[j]:
                    dp[j+1] += dp[j]
        return dp[m]
