class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        n = len(mat)
        m = len(mat[0])
        #counter = 0

        #ind = []
        #tot_ind = list(range(n))
        
        #for j in range(m):
        #    for i in range(n):
        #        if mat[i][j] == 0 and i not in ind:
        #            ind.append(i)
        #            tot_ind.remove(i)
        #            counter += 1
        #            if counter == k:
        #                return ind

        sums_dict = {j: [] for j in range(m+1)}
        for i in range(n):
            for j in range(m):
                if j != m - 1:
                    if mat[i][j] == 0:
                        sums_dict[j].append(i)
                        break
                else:
                    if mat[i][j] == 0:
                        sums_dict[j].append(i)
                    else:
                        sums_dict[j+1].append(i)


        ind = []
        counter = 0
        for j in range(m+1):
            ind += sums_dict[j][:k - counter]
            counter += len(sums_dict[j])
            if counter >= k:
                return ind[:k]

        return ind
