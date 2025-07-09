class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        # Convert string to list to allow in-place modification
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in every 2k segment
            s[i:i+k] = s[i:i+k][::-1]
        return ''.join(s) # Convert list back to string
