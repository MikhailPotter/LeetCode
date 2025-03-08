class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr  = set(nums)
        for i in range(1, len(arr)+2):
            if i not in arr:
                return i