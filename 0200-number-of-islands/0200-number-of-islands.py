class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j, visited):
            stack = [(i, j)]
            visited.add((i, j))
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            while stack:
                i, j = stack.pop()
                for direct in directions:
                    cur_i = i + direct[0]
                    cur_j = j + direct[1]

                    if cur_i >= 0 and cur_j >= 0 and cur_i < len(grid) and cur_j < len(grid[0]):
                        if (cur_i, cur_j) not in visited and grid[cur_i][cur_j] == "1":
                            visited.add((cur_i, cur_j))
                            stack.append((cur_i, cur_j))
            
            return visited

        count = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    visited = dfs(i, j, visited)
                    count += 1
        
        return count



        