class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = [0 for _ in range(len(nums))]
        last_good = len(nums) - 1
        for i in range(len(pos) - 2, -1, -1):
            if nums[i] >= last_good - i:
                last_good = i
        if last_good == 0:
            return True
        return False
        