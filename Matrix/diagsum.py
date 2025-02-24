class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_ = 0
        n = len(mat)
        for i in range(n):
            sum_ += mat[i][i] + mat[i][n - 1 - i]

        if n % 2 == 0:
            return sum_
        else:
            return sum_ - mat[n // 2][i // 2]
