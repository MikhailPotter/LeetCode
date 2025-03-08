class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        min_delta = 3*10**4
        for i in range(len(nums)):
            fixed = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + fixed
                if abs(min_delta - target) > abs(curr_sum - target):
                    min_delta = curr_sum
                if curr_sum == target:
                    return target
                elif curr_sum > target:
                    r -= 1
                else:
                    l += 1
        return min_delta