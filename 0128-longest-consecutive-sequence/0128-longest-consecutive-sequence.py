class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        if len(a) == 0:
            return 0
        max_ = 1
        max = 1 
        for i in range(1, len(a)):
            if a[i] - a[i-1] == 1:
                max += 1
                if max_ < max:
                   max_ = max
            else:
                max = 1
        return max_

