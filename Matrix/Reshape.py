class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) > 0 and len(mat) * len(mat[0]) != r*c:
            return mat

        m = len(mat)
        n = len(mat[0])
        new_mat = [[0 for j in range(c)] for i in range(r)]

        for i in range(r):
            for j in range(c):
                new_ind = i*c + j
                new_mat[i][j] = mat[new_ind // n][new_ind % n]

        return new_mat
