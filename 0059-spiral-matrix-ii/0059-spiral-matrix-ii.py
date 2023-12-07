class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [['' for _ in range(n)] for _ in range(n)]
        i, j, direction, curr_number = 0, 0, 0, 1
        r, l, d, u = n - 1, 0, n - 1, 1
        while curr_number <= n**2:
            # going right
            if direction == 0:
                matrix[i][j] = curr_number
                j += 1
                curr_number += 1
                if j == r:
                    direction = 1
                    r -= 1
                    
            # going down
            elif direction == 1:
                matrix[i][j] = curr_number
                i += 1
                curr_number += 1
                if i == d:
                    d -= 1
                    direction = 2
                    
            # going left    
            elif direction == 2:
                matrix[i][j] = curr_number
                j -= 1
                curr_number += 1
                if j == l:
                    l += 1
                    direction = 3
                    
            # going up                   
            elif direction == 3:
                matrix[i][j] = curr_number
                i -= 1
                curr_number += 1
                if i == u:
                    u += 1
                    direction = 0
        return matrix
        