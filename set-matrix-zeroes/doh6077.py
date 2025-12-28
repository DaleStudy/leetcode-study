
# 73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroIndex = []
        # Brute Force
        # 1. first find which columns have zero
        # 2. set the entire row to zero
        for subIndex, sublist in enumerate(matrix):
            for elementIndex, element in enumerate(sublist):
                print(f"Checking element at row {subIndex}, column {elementIndex}: {element}"   )
                if element == 0:
                    zeroIndex.append(elementIndex)  
                    sublist = [0] * len(sublist)
                    matrix[subIndex] = sublist
        for subIndex, sublist in enumerate(matrix):
            for elementIndex, element in enumerate(sublist):
                if elementIndex in zeroIndex:
                    sublist[elementIndex] = 0           
        print(zeroIndex)    

sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
print(matrix)  # Output should be [[1,0,1],[0,0,0],[1,0,1]]
