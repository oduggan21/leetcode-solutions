class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache
        INF = 10**9

        @lru_cache(maxsize = None)
        def best(a):
            if a == 0:
                return 0
            if a < 0:
                return float(INF)
            return 1 + min(best(a-c) for c in coins)
        ans =  best(amount)
        return ans if ans < INF else -1
