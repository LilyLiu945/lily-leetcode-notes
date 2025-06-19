class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeft(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left           
# For left bound: right overstepped left → return left     
        
        def findRight(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
# For right bound: left overstepped right → return right
        
        left = findLeft(nums, target)
        right = findRight(nums, target)
        if left <= right:
            return [left,right]
        else:
            return [-1,-1]
