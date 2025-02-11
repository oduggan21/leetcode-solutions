class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0 
        right = len(height) - 1
        maxVol = 0

        while(left < right):
            if(height[left] <= height[right]):
                volume = height[left] * (right - left)
                left += 1
            else:
                volume = height[right] * (right - left)
                right -= 1
            maxVol = max(maxVol, volume)   
        return maxVol

