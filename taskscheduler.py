class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       
        from collections import Counter

        count = Counter(tasks)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            i = 0
            temp = []
            while i <= n:
                if max_heap: #this is only entered if we still have values within the heap
                    val = heapq.heappop(max_heap)
                    if val + 1 < 0:
                        temp.append(val + 1)
                time += 1
                
                if not max_heap and not temp:
                    break
                i += 1
            for val in temp:
                heapq.heappush(max_heap,val)
        return time
    
