"""

	풀이 : 
		dfs를 이용해서 인자로 들어온 row, col부터 matrix를 순회하며 0을 찾는다
		0 찾으면 column 1 증가시켜 dfs호출 후 해당 행,열을 0으로 설정 후 return
		모든 matrix 순회하면 return

	m * n matrix

	TC : O(M * N)
		전체 matrix를 한번 순회하므로
	
	SC : O(M * N)
        0의 개수만큼 재귀호출스택이 쌓이는데 최악의 경우 M * N만큼 호출되므로


    - 다른풀이
        첫째 행과 첫째 열을 각 행렬에 대한 0여부 저장하는 flag로 사용
        첫째 행과 첫째 열의 0 여부는 따로 변수 2개로 저장
        공간복잡도를 O(1)로 개선할 수 있음
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        def dfs(row: int, col: int) -> None :
            while row < n_rows :
                while col < n_cols :
                    if matrix[row][col] == 0 :
                        dfs(row,col + 1)
                        for i in range(n_rows) :
                            matrix[i][col] = 0
                        for j in range(n_cols) :
                            matrix[row][j] = 0
                        return
                    col += 1
                col = 0
                row += 1
            return
        dfs(0,0)
