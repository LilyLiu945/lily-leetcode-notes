class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)

        return sell2

# Each day's states depend only on the previous day's states.
# Update each price to achieve O(n) time and O(1) space.
