"""
Time Complexity: O(m * n)
Space Complexity: O(m + n)

과정:
1. 0이 있는 행과 열을 따로 집합에 기록해둠
2. 만들어진 행과 열을 기반으로 0으로 바꿔줌
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        array = []
        for x in range(m):
            for y in range(n):
                if matrix[y][x] == 0:
                    array.append((x, y))
        a, b = set(), set()
        for x, y in array:
            a.add(x)
            b.add(y)
        for x in range(m):
            for i in b:
                matrix[i][x] = 0
        for y in range(n):
            for i in a:
                matrix[y][i] = 0
