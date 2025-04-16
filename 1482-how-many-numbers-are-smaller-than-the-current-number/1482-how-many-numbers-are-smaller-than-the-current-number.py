class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_dict = dict()
        sorted_nums = sorted(nums)

        for i, value in enumerate(sorted_nums):
            if value not in num_dict.keys():
                num_dict[value] = i
        
        res = list()
        for i in nums:
            res.append(num_dict[i])

        return res
        