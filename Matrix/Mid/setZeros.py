class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        ir = set()
        jr = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    ir.add(i)
                    jr.add(j)

        for i in ir:
            for j in range(m):
                matrix[i][j] = 0
        
        for j in jr:
            for i in range(n):
                matrix[i][j] = 0
        
