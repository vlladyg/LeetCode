class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        area = 0
        n, m = len(mat[0]), len(mat)
        dp = [ [0]*n for i in range(m) ]
        for i in range(m):
            for j in range(n):
                if mat[i][j]=="1":
                    if i==0 or j==0:dp[i][j]=1
                    else:dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    if dp[i][j]>area:area=dp[i][j]
        return area**2
