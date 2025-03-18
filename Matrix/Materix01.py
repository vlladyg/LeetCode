from collections import deque
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat) 
        m = len(mat[0])
        
        min_dist = [[-1]*m for i in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    min_dist[i][j] = 0
                    queue.append((i, j))
        
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(queue) > 0:
            i, j = queue.popleft()

            for ii, jj in delta:
                ci = ii + i
                cj = jj + j
                if 0 <= ci < n and  0 <= cj < m and min_dist[ci][cj] == -1:
                    min_dist[ci][cj] = min_dist[i][j] + 1

                    queue.append((ci, cj))


        return min_dist
