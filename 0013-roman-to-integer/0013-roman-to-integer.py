class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)
        ans = 0
        for i in range(n):
            cur = val[s[i]] # value of current symbol

            # if next symbol exists and is larger, subtract current
            if i + 1 < n and cur < val[s[i + 1]]:
                ans -= cur
            else:
                ans += cur
        return ans