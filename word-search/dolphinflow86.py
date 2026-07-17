# 1) Use dfs and backtracking to search for a word in the board.
# TC: O(N*M*3^W) where N is len(row), M is len(col) and W is len(word)
# SC: O(N*M) representing the maximum depth of the recursion tack.
class Solution:
    def dfs(self, board: List[List[str]], word: str, row: int, col: int, wordIdx: int) -> bool:
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        
        if wordIdx >= len(word) or board[row][col] != word[wordIdx]:
            return False

        if wordIdx == len(word) - 1:
            return True
        
        temp = board[row][col]
        board[row][col] = '#'

        found = (
            self.dfs(board, word, row + 1, col, wordIdx + 1) or
            self.dfs(board, word, row - 1, col, wordIdx + 1) or
            self.dfs(board, word, row, col + 1, wordIdx + 1) or
            self.dfs(board, word, row, col - 1, wordIdx + 1)
        )

        board[row][col] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        w = len(word)

        # Early return if the board contains fewer cells than the word length.
        if n * m < w: return False

        for i in range(n):
            for j in range(m):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False
