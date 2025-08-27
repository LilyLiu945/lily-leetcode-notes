class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        
        res = []
        slow = 0
        for fast in range(n):
            if fast == n - 1 or nums[fast] + 1 != nums[fast + 1]:
                if slow < fast:
                    res.append(f"{nums[slow]}->{nums[fast]}")
                elif slow == fast:
                    res.append(str(nums[slow]))
                slow = fast + 1
                
        return res        