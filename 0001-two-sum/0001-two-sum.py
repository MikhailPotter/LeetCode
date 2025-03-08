class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, val in enumerate(nums):
            if val in hmap:
                return hmap[val], i
            else:
                hmap[target - val] = i