class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        count = 0
  
        currR = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] < currR:
                count += 1
            else:
                currR = intervals[i][1]
       
        return count

        
