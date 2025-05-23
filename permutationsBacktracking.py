class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_list = []

        def backTracking( temp_list):
            if len(temp_list) == len(nums):
                final_list.append(list(temp_list))
                return
            for i in range(len(nums)):
                if nums[i] not in temp_list:
                    temp_list.append(nums[i])
                    backTracking(temp_list)
                    temp_list.pop()
        
        backTracking([])
        return final_list
        
