class Solution:
    # O(m*n), m*n = board's width,heigh
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = False

        def dfs(i, j, visited, w):
            nonlocal result
            if (i, j) in visited:
                return
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
                return
            w += board[i][j]
            if not (word[:len(w)] == w):
                return
            visited.add((i, j))
            if w == word:
                result = True
                return
            for d in dirs:
                dfs(i + d[0], j + d[1], visited, w)
            visited.remove((i, j))  # backtracking

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, set(), "")
                if result:
                    return True
        return False
