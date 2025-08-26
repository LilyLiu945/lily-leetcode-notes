# O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        bucket = [0] * (n + 1) # bucket[i] stores how many papers have exactly i citations
        for c in citations:
            bucket[min(c, n)] += 1 # All papers with >= n citations are grouped into bucket[n]

        papers = 0 # papers = number of papers with at least current h citations
        for h in range(n, -1, -1): # Try h from high to low. 
            papers += bucket[h]
            if papers >= h: #The first h that satisfies papers >= h is the answer.
                return h 
        return 0
