class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        for i, value in enumerate(nums):
            if target - value in set_nums and i != nums.index(target-value):
                res = [i, nums.index(target-value)]
                return res
        
                