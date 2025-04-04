class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [0]*m
        dp[m - 1] = 1

        # Time O(m*n) Space: O(m)

        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if obstacleGrid[row][col]:
                    dp[col] = 0
                elif col + 1 < m:
                    dp[col] = dp[col] + dp[col + 1]


        return dp[0]
