class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        row = [0]*n
        col = [0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if row[i] < 2:
                        row[i] += 1
                    else:
                        break

        for j in range(m):
            for i in range(n):
                if mat[i][j] == 1:
                    if col[j] < 2:
                        col[j] += 1
                    else:
                        break
        
        print(row)
        print(col)
        out = 0
        for i in range(n):
            if row[i] == 1:
                for j in range(m):
                    if col[j] == 1 and mat[i][j] == 1:
                        out += 1
                        break
        
        return out
