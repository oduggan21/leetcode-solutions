class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        max_heap = [-n for n in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x > y:
                x -= y
                heapq.heappush(max_heap, -x)
        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0
