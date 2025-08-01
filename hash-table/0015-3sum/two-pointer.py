class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate a
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate b
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate c
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move inward
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # need bigger sum
                else:
                    right -= 1  # need smaller sum

        return res
