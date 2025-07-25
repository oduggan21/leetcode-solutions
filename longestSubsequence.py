class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
         n1, n2, = len(text1), len(text2)

         dp = [[0]* (n2+1) for _ in range (n1+1)]

         for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

         return dp[0][0]
        
