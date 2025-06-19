class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        
# Why return slow + 1 here (unlike return slow in Problem 27)?
# - In this problem (26), 'slow' is the index of the last unique element.
# - Since we start from fast = 1 and always write to nums[slow + 1], 
#   the total number of unique elements is slow + 1.
# - In contrast, in Problem 27, 'slow' counts the number of valid (non-val) elements directly,
#   so no +1 is needed there.        
