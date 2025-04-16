class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        nums = set(nums)
        res = list()
        for i in range(len_nums):
            if i + 1 not in nums:
                res.append(i+1)
        
        return res