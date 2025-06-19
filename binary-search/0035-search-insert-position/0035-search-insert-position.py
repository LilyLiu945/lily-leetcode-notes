class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
# Why return 'left' or 'right + 1' instead of 'mid' or 'mid + 1':
# - Loop exits when left > right (i.e., right == left - 1)
# - 'left' and 'right' are valid after the loop
# - 'mid' is only meaningful within the loop, and its value at exit may equal 'left' or 'right'
# → 'left' is guaranteed to be the first valid insertion index ✅
