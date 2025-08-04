from typing import List

class Solution:
    """
        - Time Complexity: O(mn), m = len(matrix), n = len(matrix[0])
        - Space Complexity: O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Update row and column with a flag (infinite) if the value is not zero
        def updateRowCol(i, j):
            for k in range(m):
                if matrix[k][j] != 0:
                    matrix[k][j] = float("inf") 
            for k in range(n):
                if matrix[i][k] != 0:
                    matrix[i][k] = float("inf") 

        # Visit all and update row and column if the value is zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    updateRowCol(i, j)
        
        # Update flagged data to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

tc = [
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
]

sol = Solution()
for i, (m, e) in enumerate(tc, 1):
    sol.setZeroes(m)
    print(f"TC {i} is Passed!" if m == e else f"TC {i} is Failed! - Expected: {e}, Result: {m}")
