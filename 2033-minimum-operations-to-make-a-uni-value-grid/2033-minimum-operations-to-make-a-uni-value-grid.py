class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [elem for row in grid for elem in row]
        a = flat_grid[0] % x
        for number in flat_grid:
            if number % x != a:
                return -1
            
        flat_grid.sort()
        length = len(flat_grid)
        target = flat_grid[length // 2]
        res = 0
        for n in flat_grid:
            res += abs(target - n) // x
        return res
            
        