class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
    
    def addNum(self, num: int) -> None:
        if not self.min_heap or num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if not self.min_heap and not self.max_heap:
            return []
        total_length = len(self.min_heap) + len(self.max_heap)
        if total_length % 2 == 0:
            val1 = self.min_heap[0]
            val2 = -self.max_heap[0]
            return (val1 + val2) / 2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
            
        
            
        
