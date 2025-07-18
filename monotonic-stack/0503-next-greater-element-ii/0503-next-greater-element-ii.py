# Time complexity: O(n)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = [] # Stack stores "indices", not values
        
        for i in range(2 * n): # Simulate circular array
            cur = nums[i % n]
            
            while stack and nums[stack[-1]] < cur:
                prev = stack.pop()
                res[prev] = cur
                
            if i < n: # Only push index in first pass
                stack.append(i)
                
        return res 
