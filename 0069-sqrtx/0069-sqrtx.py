# Better Version:
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x # Special cases: sqrt(0) = 0, sqrt(1) = 1

        left, right = 1, x // 2 # Binary search in range [1, x // 2]

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right

# Original Version:
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right)//2
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
