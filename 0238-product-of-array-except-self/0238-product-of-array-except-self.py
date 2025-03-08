class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        if nums.count(0) > 1:
            return [0 for _ in nums]
        for i in nums:
            if i != 0:
                a *= i
        res = []
        flg = 0 in nums
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(a)
            else:
                if flg:
                    res.append(0)
                else:
                    res.append(a // nums[i])
        return res