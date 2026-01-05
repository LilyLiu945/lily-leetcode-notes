class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for p, start, end in trips:
            events.append((start, p))
            events.append((end, -p))
        events.sort()

        cur = 0
        for _, delta in events:
            cur += delta
            if cur > capacity:
                return False
        
        return True