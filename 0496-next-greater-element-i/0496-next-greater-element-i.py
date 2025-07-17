class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for i in nums2:
            while stack and i > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = i
            stack.append(i)
        
        return [next_greater.get(j, -1) for j in nums1]