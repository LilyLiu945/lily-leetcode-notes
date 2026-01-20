class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)
        ns, ne = newInterval

        while i < n and intervals[i][1] < ns:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= ne:
            ns = min(intervals[i][0], ns)
            ne = max(intervals[i][1], ne)
            i += 1
        ans.append([ns, ne])    

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans  
        
# 1. Check index bounds (i < n) before accessing intervals[i].
# 2. Expand newInterval first. Don't Append merged intervals multiple times.
# 3. Once newInterval is finalized, all remaining intervals can be appended directly.
