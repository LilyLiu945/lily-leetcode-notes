# Easy but not recommended
# Time complexity: O(n log n)
# Space complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
