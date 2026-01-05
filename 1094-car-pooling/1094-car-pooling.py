class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = defaultdict(int)
        for p, start, end in trips:
            diff[start] += p
            diff[end] -= p

        cur = 0
        for pos in sorted(diff):
            cur += diff[pos]
            if cur > capacity:
                return False
        return True