class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [ nums[i % len(nums)] for i in range(len(nums)*2)]