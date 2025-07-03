# Why use a set to detect cycles?

# If a number is not a happy number, the process of summing the squares of digits 
# will eventually repeat a previous number and fall into a cycle.

# For example: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 ...

# Once a number repeats, it means we are stuck in a loop and will never reach 1.
# So we use a set to store all the numbers we've seen so far.
# If we ever see the same number again, we know we're in a cycle and can return False.
# Otherwise, if we reach 1, it's a happy number and we return True.

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10) # Split off the last digit
                # Return the quotient and remainder of the division simultaneously
                total += digit * digit
            return total
            
        # Use a set to track seen numbers and detect cycles    
        seen = set() 
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
