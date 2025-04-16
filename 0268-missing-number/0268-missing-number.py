class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums) + 1
        met_values = [0] * len_nums

        for value in nums:
            met_values[value] = 1
        
        return met_values.index(0)
        