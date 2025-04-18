class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        rounds = 0
        res = list()

        max_possible_i = len(matrix) - 1
        max_possible_j = len(matrix[0]) - 1

        res_len = (max_possible_j+1) * (max_possible_i+1)

        while len(res) < res_len:

            while j <= max_possible_j - rounds and len(res) < res_len:  # -->
                res.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1

            while i < max_possible_i - rounds and len(res) < res_len:  # down
                res.append(matrix[i][j])
                i += 1

            while j >= rounds and len(res) < res_len:  # <--
                res.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1

            while i > rounds and len(res) < res_len:
                res.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1

            rounds += 1
        return res
