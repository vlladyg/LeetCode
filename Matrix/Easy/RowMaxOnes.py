class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_sum = -1
        ind = 0
        for i in range(len(mat)):
            sum_tmp = sum(mat[i])
            if sum_tmp > max_sum:
                ind = i
                max_sum = sum_tmp


        return [ind, max_sum]
