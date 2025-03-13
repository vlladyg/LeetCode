class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        res = []
        ii = 0
        jj = 0
        up = True
        while len(res) != n*m:
            if up:
                while ii >= 0 and jj < m:
                    res.append(mat[ii][jj])
                    
                    ii -= 1
                    jj += 1

                if jj == m:
                    jj -= 1
                    ii += 2
                else:
                    ii += 1


                up = False
            else:
                while ii < n and jj >= 0:
                    res.append(mat[ii][jj])

                    jj -= 1
                    ii += 1

                if ii == n:
                    jj += 2
                    ii -= 1
                else:
                    jj += 1
                
                up = True

        return res
