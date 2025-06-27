class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Will i repeately see the same problem?
        #describe the state, in this case what set of numbers will define where I am ?
        #set the base cases of answers we know trivially
        #write the rule for the recurrence problem
        #choose engine

        n = len(nums)

        if not nums:
            return 
        res = float('-inf')

        mem = {}
        def product(index):
            nonlocal res
            if index == n-1:
                if nums[index] >= 0:
                    res = max(res, nums[index])
                    return (nums[index],0)
                else:
                    res = max(res, nums[index])
                    return(0, nums[index])
            
            tuple_val = product(index+1)
            if nums[index] >= 0:
                positive = max(nums[index], nums[index]*tuple_val[0])
                negative = min(nums[index], nums[index]*tuple_val[1])
           
            else:
                positive = max(nums[index], nums[index]*tuple_val[1])
                negative = min(nums[index], nums[index]*tuple_val[0])
            
            mem[index] = (positive,negative)
            res = max(res, positive,negative)
            
            return mem[index]

        product(0)
        return res
            
