class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                c = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = c

        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix
