class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        def check_equalindromic(number: int) -> bool:
            if number % 10 == 0:
                return False
            return str(number)[::-1] == str(number)
        if len(nums) == 1:
            return 0
        
        nums.sort()
        if len(nums) % 2 == 1:
            target = nums[len(nums) // 2 + 1]
            if check_equalindromic(target):
                res = 0
                for number in nums:
                    res += abs(number - target)
                
        median = nums[len(nums) // 2]
        l, r = median, median
        while not check_equalindromic(r):
            r += 1
        while not check_equalindromic(l):
            l -= 1

        res_l, res_r = 0, 0
        for number in nums:
            res_l += abs(number - r)
            res_r += abs(number - l)
            
        return min(res_l, res_r)
        