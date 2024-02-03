class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_elem = nums[0]
        for n in nums:
            if n < min_elem:
                min_elem = n
        return sum(nums) - len(nums) * min_elem