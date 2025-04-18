class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        cur_length = 0
        min_length = -1
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            cur_length += 1

            while cur_sum >= target:
                if min_length > r - l + 1 or min_length == -1:
                    min_length = r - l + 1

                cur_length -= 1
                cur_sum -= nums[l]
                l += 1
        if min_length == -1:
            return 0
        return min_length




