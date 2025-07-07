from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
      
# "Counter(ransomNote) - Counter(magazine)" keeps all the insufficient characters in magazine
# "not" indicates that the result is empty, suggesting that magazine is sufficient to cover ransomNote

# Slightly inferior performance: 
# The internal structure of Counter and subtraction both need to traverse the string and dictionary once.
