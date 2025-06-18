class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right: # Missed the last position without equal
            mid = (left + right)//2 # Find the midpoint
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # Skip the midpoint itself
            else:
                right = mid - 1
        return -1



        