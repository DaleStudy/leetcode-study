class Solution:
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i: int, j: int, k: int):
            if k == len(word):
                return True
            
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[k]:
                return False

            current = board[i][j]
            board[i][j] = ''

            if dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1):
                return True
            
            board[i][j] = current
            return False

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        
        return False
