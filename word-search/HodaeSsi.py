class Solution:
	def dfs (self, board, word, visited, y, x, word_idx):
		if word_idx == len(word):
			return True
		
		if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or visited[y][x] or board[y][x] != word[word_idx]:
			return False
		
		visited[y][x] = True
		for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
			if self.dfs(board, word, visited, y + dy, x + dx, word_idx + 1):
				return True
		visited[y][x] = False
		return False

	def exist(self, board: List[List[str]], word: str) -> bool:
		visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

		# find fisrt letter in board
		for y in range(len(board)):
			for x in range(len(board[0])):
				if board[y][x] == word[0]:
					visited[y][x] = True
					for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
						if self.dfs(board, word, visited, y + dy, x + dx, 1):
							return True
					visited[y][x] = False
		return False
					
