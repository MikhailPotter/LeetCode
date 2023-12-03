class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(n//2 + n % 2):
            for j in range(n//2 + 1):
                matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] = \
                matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]
        