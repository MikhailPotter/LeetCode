class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j, t = queue.popleft()
            time = max(time, t)
            for dir_i, dir_j in directions:
                cur_i, cur_j = i + dir_i, j + dir_j  
                if 0 <= cur_i < rows and 0 <= cur_j < cols and grid[cur_i][cur_j] == 1:
                    grid[cur_i][cur_j] = 2  
                    fresh -= 1
                    queue.append((cur_i, cur_j, t + 1))

        return time if fresh == 0 else -1
        