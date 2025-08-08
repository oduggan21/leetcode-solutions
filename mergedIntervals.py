class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = []
        currL, currR = intervals[0]
        for L, R in intervals[1:]:
            if L <= currR:
                currR = max(currR, R)
            else:
                merged.append([currL,currR])
                currL, currR = L, R
        merged.append([currL,currR])
        return merged

