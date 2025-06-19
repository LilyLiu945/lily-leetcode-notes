class Solution:
    def mySqrt(self, x: int) -> int:
        # Special cases: sqrt(0) = 0, sqrt(1) = 1
        if x < 2:
            return x

        # Binary search in range [1, x // 2]
        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        # Loop ends when left > right
        # → right is the largest number where right * right <= x
        return right
