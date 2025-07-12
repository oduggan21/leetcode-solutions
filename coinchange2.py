class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if abs(target) > total:
            return 0
        dp = [0] * ((2*(total)) + 1)
        offset = total
        dp[offset] = 1

        for n in nums:
            np = [0] * ((2*(total)) + 1)
            for i in range(-total, total+1):
                if dp[i + offset]:
                    np[i+offset+n] += dp[i+offset]
                    np[i+offset-n] += dp[i+offset]
            dp = np
        return dp[offset+target]

