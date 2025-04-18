class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        res = list()
        prev = None
        
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] > 0:
                break
            if prev is None or prev != sorted_nums[i]:
                prev = sorted_nums[i]
            else:
                continue
            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] != 0:
                    if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] < 0:
                        l += 1
                    else:
                        r -= 1
                else: 
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1

                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
        return res