class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        flag = True
        for i in range(n):
            if flag:
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        flag = False
                        break
            else:
                break
        if flag:
            return True


        for _ in range(3): 
            print(mat)
            mat = list(zip(*mat))[::-1]  # Perform 90-degree rotation

            flag = True
            for i in range(n):
                if flag:
                    for j in range(n):
                        if mat[i][j] != target[i][j]:
                            flag = False
                            break
                else:
                    break
            if flag:
                return True

        return False
