# Step 1: Check if the lengths are equal — if not, they can't be anagrams
# Step 2: Create a dictionary (hashmap) to store character counts from string s
# Step 3: For each character in t, subtract from the hashmap
# - If any count drops below 0, it means t has more of that character than s → not an anagram
# - Because the lengths are the same, one char being extra means another must be missing
# → So we only need to check if any count < 0 (no need to check > 0)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            # If char is not in the dictionary, it defaults to 0

        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] < 0:
                return False

        return True
