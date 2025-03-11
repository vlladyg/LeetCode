class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max([len(str(el)) for el in col]) for col in zip(*grid)]
