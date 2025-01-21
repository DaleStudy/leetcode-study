# 시간 복잡도 : O(m * n)
# 공간 복잡도 : O(1)
# 문제 유형 : 구현
class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		row, col = len(matrix), len(matrix[0])
		up, down, left, right = 0, row - 1, 0, col - 1
		result = []
		while True:
			for i in range(left, right + 1):
				result.append(matrix[up][i])
			up += 1
			if up > down:
				break
			for i in range(up, down + 1):
				result.append(matrix[i][right])
			right -= 1
			if right < left:
				break
			for i in range(right, left - 1, -1):
				result.append(matrix[down][i])
			down -= 1
			if down < up:
				break
			for i in range(down, up - 1, -1):
				result.append(matrix[i][left])
			left += 1
			if left > right:
				break
		return result

