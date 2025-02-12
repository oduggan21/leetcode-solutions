class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        left = 0
        right = 1
        while(right < len(prices)):
            if(prices[right] < prices[left]):
                #meaning that we find a cheaper price
                left = right
            else:
                maximum = max(maximum,prices[right]- prices[left])
            right += 1
        return maximum
