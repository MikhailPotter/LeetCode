class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = list()
        min_sq_value = -1

        for i, value in enumerate(nums):
            if abs(value) < min_sq_value or min_sq_value == -1:
                min_sq_value = abs(value)
                min_index = i
        
        res.append(nums[min_index]**2)
        l = min_index - 1
        r = min_index + 1

        while r < len(nums) and l > -1:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[r]**2)
                r += 1
            else:
                res.append(nums[l]**2)
                l -= 1
        
        while r < len(nums): 
            res.append(nums[r]**2)
            r += 1
        
        while l > -1:
            res.append(nums[l]**2)
            l -= 1
        
        return res

