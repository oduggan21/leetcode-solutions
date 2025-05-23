class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        list_final = []
        candidates.sort()
        def backTracking(start,list_temp):
            total = sum(list_temp)
            if total == target:
                list_final.append(list(list_temp))
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                list_temp.append(candidates[i])
                backTracking(i+1, list_temp)
                list_temp.pop()
        backTracking(0, [])
        return list_final
        
