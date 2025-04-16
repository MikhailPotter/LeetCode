class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for value in nums:
            res = res ^ value
        
        return res
        