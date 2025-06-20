# Sliding Window:

# This method works efficiently when:
# 1. The array contains only positive numbers (or the condition is monotonic)
# 2. The problem asks for an optimal subarray (like minimum length or maximum sum)
# 3. The subarray must be continuous

# It does not explore all combinations like brute-force,
# but it guarantees the optimal solution due to the properties of the data.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right-left+1)
                window_sum -= nums[left]
                left += 1
                  
        return 0 if min_len == float('inf') else min_len
