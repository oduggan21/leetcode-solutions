class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        hold, buy, rest = -prices[0], 0, 0

        for p in prices[1:]:
            hold, buy, rest = (
                max(hold, rest-p), #hold is going to be if we own a current stock our maxium profit
                hold + p, #buy is going to be our current price + whatever the hold is which considers rese;;s
                max(rest, buy) #our current buy nothing or a previous buy
            )
        
        return max(rest, buy)

