class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for chars in zip(*strs): # *: argument unpacking
            if len(set(chars)) == 1:
                res.append(chars[0])
            else:
                break
        return "".join(res)
