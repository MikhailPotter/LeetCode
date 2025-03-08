class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            fixed = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + fixed == 0:
                    
                    if [fixed, nums[l], nums[r]] not in res:
                        res.append([fixed, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + fixed > 0:
                    r -= 1
                else:
                    l += 1
        return res