class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = 0
        for fast in range(len(s)):
            if slow > 0 and res[slow - 1] == s[fast]:
                slow -= 1
            else:
                res[slow] = s[fast]
                slow += 1
        return ''.join(res[:slow])