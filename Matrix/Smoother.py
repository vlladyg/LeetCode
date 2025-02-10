class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])

        new_img = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                tot_sum, counter = 0, 0
                for si in range(i-1, i + 2):
                    for sj in range(j - 1, j + 2):
                        if 0 <= si < n and 0 <= sj < m:
                            tot_sum += img[si][sj]
                            counter += 1
                
                new_img[i][j] = tot_sum // counter

        return new_img
