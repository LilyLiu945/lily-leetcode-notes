class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# This greedy solution is a special case of DP.
# By summing all positive price differences, we achieve the same result
# as the DP solution with states (hold, cash), but in a simpler form.
