class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        # helper to solve the linear version (LC 198) on a subarray
        def rob_linear(arr: List[int]) -> int:
            prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
            for x in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1

        # case 1: use houses [0..n-2]; case 2: use houses [1..n-1]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
