class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])


        for i in range(m):
            el = matrix[i][0]
            ii = i
            jj = 0
            while ii != m and jj != n:
                if matrix[ii][jj] != el:
                    return False
                ii += 1
                jj += 1

        for j in range(n):
            el = matrix[0][j]
            ii = 0
            jj = j
            while ii != m and jj != n:
                if matrix[ii][jj] != el:
                    return False
                ii += 1
                jj += 1
        

        return True
