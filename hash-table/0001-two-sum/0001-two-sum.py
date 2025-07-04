# Time Complexity: O(n), Space Complexity: O(n)

# Smart Optimization:
# - The map is built as we iterate — no need to build it beforehand.
# - Often, we find the answer before scanning the entire array.
# - HashMap lookups and inserts are both O(1) on average.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key: number, value: index
        for i, num in enumerate(nums): 
            x = target - num
            if x in hashmap:
                return [hashmap[x], i]
            hashmap[num] = i
