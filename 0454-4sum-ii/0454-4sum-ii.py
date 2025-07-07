class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def get_sum(numsx: List[int],numsy: List[int]) -> dict:
            freq = {}
            for x in numsx:
                for y in numsy:
                    num_sum = x + y
                    freq[num_sum] = freq.get(num_sum, 0) + 1
            return freq

        freq1 = get_sum(nums1, nums2)
        freq2 = get_sum(nums3, nums4)
        number = 0

        for num_sum1 in freq1:
            for num_sum2 in freq2:
                if num_sum1 + num_sum2 == 0:
                    number = number + freq1[num_sum1] * freq2[num_sum2]
        
        return number