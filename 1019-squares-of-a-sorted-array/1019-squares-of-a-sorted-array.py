class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  # 预留结果数组
        left, right = 0, n - 1
        pos = n - 1  # 从后往前放

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1  # 填下一个位置
        
        return res
