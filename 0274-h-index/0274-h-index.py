class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        nums = 0
        while papers > 0:
            for i in range(0, len(citations)):
                if citations[i] >= papers:
                    nums += 1
            if papers <= nums:
                return papers
            else:
                nums = 0
            papers -= 1
        return 0