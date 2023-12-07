class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def adjacent_cells(i, j):
            c1, c2, c3, c4 = (i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)
            adj_cells = [c1, c2, c3, c4]
            
            return [cell for cell in adj_cells if (0 <= cell[0] and cell[0] < m) and (0 <= cell[1] and cell[1] < n)]
        
        m, n = len(grid), len(grid[0])
        orange_counter = {
            0: [],
            1: [],
            2: [],
        }
        for i in range(m):
            for j in range(n):
                orange_counter[grid[i][j]].append((i, j))

        step = 0
        while len(orange_counter[1]) != 0 and len(orange_counter[2]) != 0:
            step += 1
            rotten_during_curr_step = []
            for curr_rotten_i, curr_rotten_j in orange_counter[2]:
                adj = adjacent_cells(curr_rotten_i, curr_rotten_j)
                print(adj)
                for cell in adj:
                    if cell in orange_counter[1]:
                        orange_counter[1].remove(cell)
                        rotten_during_curr_step.append(cell)
            orange_counter[2] = rotten_during_curr_step
            
        if len(orange_counter[1]) != 0:
            return -1
        else:
            return step
        