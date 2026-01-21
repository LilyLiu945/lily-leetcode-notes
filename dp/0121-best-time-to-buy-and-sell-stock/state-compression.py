class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        best = 0
        for p in prices:
            min_p = min(p, min_p)
            best = max(best, p - min_p)
        return best

# dp[i] = max(prices[i] - min(prices[0..i]), dp[i-1]) # sell or not
# O(n) time and O(1) space.
