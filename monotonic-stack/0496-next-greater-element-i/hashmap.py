# Time complexity: O(m + n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # Stores specific numbers, not indexes
        next_greater = {} # Record the "next greater value" mapping for each number
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        return [next_greater.get(num, -1) for num in nums1]
