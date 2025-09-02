class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def ok(L: int) -> bool:
            p = strs[0][:L]
            return all(s.startswith(p) for s in strs)

        lo, hi = 0, min(map(len, strs))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return strs[0][:lo]