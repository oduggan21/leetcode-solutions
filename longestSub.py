class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        if n == 1:
            return 1
        
        for i in range(1,n):
            for j in range(i-1,-1,-1):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    


        val = max(dp)
        return val



        
