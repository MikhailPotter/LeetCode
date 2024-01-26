class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums and path not in res: 
                res.append(path) 
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
        res = [] 
        backtrack(nums, []) 
        return res