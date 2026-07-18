# 1) Use dfs and backtracking to search for a word in the board.
# TC: O(N*M*3^W) where N is len(row), M is len(col) and W is len(word)
# SC: O(N*M) representing the maximum depth of the recursion tack.
class Solution:
    def dfs(self, board: List[List[str]], word: str, row: int, col: int, word_idx: int) -> bool:
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        
        if word_idx >= len(word) or board[row][col] != word[word_idx]:
            return False

        if word_idx == len(word) - 1:
            return True
        
        temp = board[row][col]
        board[row][col] = '#'

        found = (
            self.dfs(board, word, row + 1, col, word_idx + 1) or
            self.dfs(board, word, row - 1, col, word_idx + 1) or
            self.dfs(board, word, row, col + 1, word_idx + 1) or
            self.dfs(board, word, row, col - 1, word_idx + 1)
        )

        board[row][col] = temp

        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        column_len = len(board[0])
        word_len = len(word)

        # Early return if the board contains fewer cells than the word length.
        if row_len * column_len < word_len: return False

        for i in range(row_len):
            for j in range(column_len):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False
