class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        n = len(matrix)
        m = len(matrix[0])

        for j in range(m):
            max_el = -2
            replace_list = []
            for i in range(n):
                if matrix[i][j] > max_el:
                    max_el = matrix[i][j]
                if matrix[i][j] == -1:
                    replace_list.append((i, j))
            for i, j in replace_list:
                matrix[i][j] = max_el

        return matrix
