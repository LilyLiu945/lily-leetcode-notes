class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations, 1):  # i = 1..n
            if c >= i:
                h = i
            else:
                break
        return h
