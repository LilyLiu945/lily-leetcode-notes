class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) # Descending order
        h = 0
        for i, c in enumerate(citations, 1):  # i start from 1
            if c >= i:
                h = i
            else:
                break
        return h
