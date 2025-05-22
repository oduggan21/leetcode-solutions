class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        list_final = []
        def backTracking(start, nums_list):
            list_final.append(list(nums_list))
            for i in range(start, len(nums)):
                nums_list.append(nums[i])
                backTracking(i+1,nums_list)
                nums_list.pop()
        
        backTracking(0, [])
        return list_final

        
