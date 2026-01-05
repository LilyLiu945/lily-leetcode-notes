class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        MAX_POS = 1000
        diff = [0] * (MAX_POS + 2)  # +2 to be extra safe for indexing

        max_end = 0
        for p, start, end in trips:
            diff[start] += p
            diff[end] -= p
            if end > max_end:
                max_end = end

        cur = 0
        for pos in range(max_end + 1):
            cur += diff[pos]
            if cur > capacity:
                return False
        return True