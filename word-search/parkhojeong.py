class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True

        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int):
        if board[i][j] != word[0] or board[i][j] == "-1":
            return False
        if len(word) == 1:
            return True

        temp_cell = board[i][j]
        board[i][j] = "-1"
        word = word[1:]
        if i >= 1 and self.dfs(board, word, i - 1, j):
            return True

        if j >= 1 and self.dfs(board, word, i, j - 1):
            return True

        if i < len(board) - 1 and self.dfs(board, word, i + 1, j):
            return True

        if j < len(board[0]) - 1 and self.dfs(board, word, i, j + 1):
            return True

        board[i][j] = temp_cell
        return False
