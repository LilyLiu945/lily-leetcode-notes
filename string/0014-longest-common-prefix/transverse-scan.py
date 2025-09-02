class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix): # s.startswith(prefix, start=0, end=len(s))
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
