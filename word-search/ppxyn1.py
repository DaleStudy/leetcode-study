# idea : dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False]*COLS for _ in range(ROWS)]

        def dfs(r, c, index):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if visited[r][c] or board[r][c] != word[index]:
                return False

            if index == len(word) - 1:
                return True
            
            visited[r][c] = True
            
            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))
            
            # For next backtracking
            visited[r][c] = False
            
            return found
        
        # Run DFS from every cell as a starting point
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False



