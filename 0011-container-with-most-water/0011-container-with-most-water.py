class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = -1

        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])

            cur_water = h * (right - left)  
            if cur_water > max_water or max_water == -1:
                max_water = cur_water
            
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return max_water