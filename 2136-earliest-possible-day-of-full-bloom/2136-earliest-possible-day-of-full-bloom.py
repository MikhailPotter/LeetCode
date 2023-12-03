class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            ans = max(ans, grow) + plant
        return ans
        