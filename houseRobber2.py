class Solution:
    def rob(self, nums: List[int]) -> int:

        #they way it works now is we take the max path of the node in front of us or 
        #the node two in front of us plus the current

        if len(nums) == 1:
            return nums[0]
        memo = {} 
        memo2 = {}

        def backtracking(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(backtracking(i+1), (nums[i] + backtracking(i+2)))
            return memo[i]

        def backtracking2(i):
            if i >= len(nums):
                return 0
            if i in memo2:
                return memo2[i]
            memo2[i] = max(backtracking2(i+1), (nums[i] + backtracking2(i+2)))
            return memo2[i]
        
        return max(backtracking(0), backtracking2(1))

        
