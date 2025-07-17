class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                if nums2[stack[-1]] in nums1:
                    j = nums1.index(nums2[stack[-1]])
                    res[j] = nums2[i]
                stack.pop()
            stack.append(i)
        return res