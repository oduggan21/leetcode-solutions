class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        return_list = []
        nums.sort()
        def backtracking(start, path):
      
            return_list.append(list(path))

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()

        backtracking(0, [])
        return return_list
        
