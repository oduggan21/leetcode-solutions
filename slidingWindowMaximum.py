class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        results = []

        for i, num in enumerate(nums):

            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)

            if i >= k - 1:
                results.append(nums[deq[0]])

        return results
