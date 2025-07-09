class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0

        def build_prefix_table(pattern):
            n = len(pattern)
            next = [0] * n
            j = 0  # length of the previous longest prefix suffix
            for i in range(1, n):
                while j > 0 and pattern[i] != pattern[j]:
                    j = next[j - 1]  # backwards
                if pattern[i] == pattern[j]:
                    j += 1
                next[i] = j
            return next

        next = build_prefix_table(needle)

        # find match
        j = 0  # pointer of needle 
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]  # backwards
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1  
        return -1
