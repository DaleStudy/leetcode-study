'''
TC: O(r * c)
SC: O(r * c)
'''

class Solution:
	def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
		r_size = len(heights)
		c_size = len(heights[0])
		pcf = set()
		atl = set()

		def recur(visited, row, col) -> None :
			if (row, col) in visited:
				return
			visited.add((row, col))
			for r, c in ([row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]):
				if 0 <= r < r_size and 0 <= c < c_size \
					and heights[r][c] >= heights[row][col]:
					recur(visited, r, c)
		for r in range(r_size):
			recur(pcf, r, 0)
			recur(atl, r, c_size - 1)
		for c in range(c_size):
			recur(pcf, 0, c)
			recur(atl, r_size - 1, c)
		result = [[r, c] for r, c in pcf & atl]
		return result
