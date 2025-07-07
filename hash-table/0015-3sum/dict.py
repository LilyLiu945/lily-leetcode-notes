class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # a + b + c = 0
        # a = nums[i], b = nums[j], c = -(a + b)
        for i in range(len(nums)):
            # If the first element >0 after sorting, it is impossible to find the triplet
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: # Skip duplicate a
                continue
            d = {}
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j-1] == nums[j-2]: # Skip duplicate b
                    continue
                c = 0 - (nums[i] + nums[j])
                if c in d:
                    result.append([nums[i], nums[j], c])
                    d.pop(c) # Skip duplicate c
                else:
                    d[nums[j]] = j
        return result
