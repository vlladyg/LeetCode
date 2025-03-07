class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [(sr, sc)]
        color_old = image[sr][sc]
        image[sr][sc] = color


        n = len(image)
        m = len(image[0])
        visited = [[False]*m for _ in range(n)]
        visited[sr][sc] = True
        while len(queue) > 0:
            i, j = queue.pop(0)
            #print(visited)
            if i > 0 and image[i-1][j] == color_old and not visited[i-1][j]:
                queue.append((i-1, j))
                visited[i-1][j] = True
                image[i-1][j] = color

            if i < n - 1 and image[i+1][j] == color_old and not visited[i+1][j]:
                queue.append((i+1, j))
                visited[i+1][j] = True
                image[i+1][j] = color

            if j > 0 and image[i][j-1] == color_old and not visited[i][j-1]:
                queue.append((i, j-1))
                visited[i][j-1] = True
                image[i][j-1] = color

            if j < m - 1 and image[i][j+1] == color_old and not visited[i][j+1]:
                    queue.append((i, j+1))
                    visited[i][j+1] = True
                    image[i][j+1] = color


        return image
