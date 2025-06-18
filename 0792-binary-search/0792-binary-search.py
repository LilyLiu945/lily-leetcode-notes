# 704. Binary Search(Easy):
# Link: https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.
# Solution:

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
