class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def backtracking(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(backtracking(i+1), (nums[i] + backtracking(i+2)))
            return memo[i]
        return backtracking(0)

        
