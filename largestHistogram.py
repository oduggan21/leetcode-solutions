class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] -1
                max_area = max(max_area, width * height)
            stack.append(i)
        
        #how this problm works is by keeping an ascended order in the stack and calculating 
        #max area as we pop values, we pop values when we find a new low value and keep popping until 
        #it is in the correct place on the stack, also we set the area
        #if we pop a bar and it makes the stack empty we know it extends all the way to the left
        #otherwise we say that we need to calculate the distnace in between
        return max_area
