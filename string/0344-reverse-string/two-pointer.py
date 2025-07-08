class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap characters at the two pointers
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
"""
Explanation:
- The tuple assignment `s[i], s[j] = s[j], s[i]` is safe in Python.
  It first evaluates the right-hand side expressions (s[j], s[i]),
  then assigns them simultaneously to the left-hand side (s[i], s[j]).
  So even if s[i] and s[j] refer to the same memory, no values are lost.

- We don't need to return `s` because the list is modified in-place.
  In Python, lists are mutable and passed by reference, so the caller
  will see the changes automatically.
"""
