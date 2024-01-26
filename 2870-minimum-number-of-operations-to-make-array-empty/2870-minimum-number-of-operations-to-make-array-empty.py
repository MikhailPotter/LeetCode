from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        if 1 in nums_counter.values():
            return -1
        
        res = 0
        for num, c_num in nums_counter.items():
            if c_num in (2, 3):
                res += 1
                continue
            res += (c_num - 3) // 3
            c_num = c_num % 3 + 3
            if c_num in (4, 5):
                res += 2
            else:
                res += 1
                
        return res