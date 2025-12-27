class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    temp.append((i, j))
        
        for t in temp:
            for i in range(n):
                matrix[i][t[1]] = 0
            for j in range(m):
                matrix[t[0]][j] = 0
    
