class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums) + 1

        sum_nums = sum(nums)
        needed_sum = sum([i for i in range(len_nums)])
        
        return needed_sum - sum_nums
        