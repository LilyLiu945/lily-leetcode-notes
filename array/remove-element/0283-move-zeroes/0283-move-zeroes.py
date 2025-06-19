class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if slow != fast: # A zero has been skipped
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1 # Valid element found so move the write pointer

# - 'fast' scans through the array.
# - 'slow' marks the position to place the next non-zero value.
