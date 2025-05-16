"""
	풀이 : 
		오른쪽, 아래쪽으로 이동할 땐 각각 column과 row가 증가하므로 direction 1
		왼쪽, 위쪽은 감소하므로 direction -1
		로 설정하고 n_row 또는 n_col만큼 direction을 이동하면서 ans에 담아준다
		각 for문이 끝날 때마다 n_row 또는 n_col을 감소시켜 주고
		둘 중 하나가 0이 될 때까지 계속 진행

		- col이 -1부터 시작해서 matrix[0][0]부터 append할 수 있도록 유의
		- n_cols, n_rows 둘 중 하나만 0이되도 끝남에 유의

	TC : O(M * N)
		matrix 전체를 한번씩 순회해야하므로
	
	SC : O(1)
		return할 리스트 외에는 추가적인 메모리 사용이 상수개(5개)이므로
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        row = 0
        col = -1
        direction = 1

        while n_cols and n_rows :
            for _ in range(n_cols):
                col += direction
                ans.append(matrix[row][col])
            n_rows -= 1

            for _ in range(n_rows):
                row += direction
                ans.append(matrix[row][col])
            n_cols -= 1

            direction *= -1

        return ans
