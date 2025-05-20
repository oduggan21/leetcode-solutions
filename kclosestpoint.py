class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for num in points:
            distance = -((num[0]**2) + (num[1]**2))
            heapq.heappush(heap,(distance, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        while heap:
            _, val = heapq.heappop(heap)
            result.append(val)
        return result

        
