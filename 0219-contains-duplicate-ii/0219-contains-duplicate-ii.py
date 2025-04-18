class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = dict()
        for i, num in enumerate(nums):
            if num in positions and i - positions[num] <= k:
                return True
            positions[num] = i
        return False
