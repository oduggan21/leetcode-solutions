class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_list = []

        def backTracking(start, current_list):
            if sum(current_list)==target:
                final_list.append(list(current_list))
            if sum(current_list) > target:
                return
            
            for i in range(start, len(candidates)):
                current_list.append(candidates[i])
                backTracking(i,current_list)
                current_list.pop()
                
        backTracking(0,[])
        return final_list
