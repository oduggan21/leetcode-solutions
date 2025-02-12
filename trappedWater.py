 def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        leftMax, rightMax = 0,0

        while(left <= right):
            if(leftMax <= rightMax):
                if(height[left] > leftMax):
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if(height[right] > rightMax):
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1

        return water
