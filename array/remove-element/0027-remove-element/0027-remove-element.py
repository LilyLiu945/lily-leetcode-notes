# Use two pointers: 'fast' scans the array
# 'slow' points to the latest position of a non-val element (the size of the valid prefix)
# When nums[fast] ≠ val, 'overwrite' nums[slow] with nums[fast]
# This way, all valid elements are moved to the front of the array

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1 # 'slow' points to the next position to store a non-val element after writing
        return slow
