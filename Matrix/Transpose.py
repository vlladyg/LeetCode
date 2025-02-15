class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        if n == m:
            for i in range(n):
                for j in range(i, m):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        matrix_trans = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                matrix_trans[j][i] = matrix[i][j]

        return matrix_trans
