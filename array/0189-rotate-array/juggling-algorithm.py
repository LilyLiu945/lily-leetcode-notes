class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from math import gcd

        n = len(nums)
        if n == 0: 
            return
        k %= n
        if k == 0:
            return

        count = 0
        for start in range(gcd(n, k)):
            cur = start
            prev = nums[start]
            while True:
                nxt = (cur + k) % n
                nums[nxt], prev = prev, nums[nxt]
                cur = nxt
                count += 1
                if cur == start:
                    break
            if count == n:
                break
