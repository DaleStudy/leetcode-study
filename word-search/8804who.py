class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_y, max_x = len(board)-1, len(board[0])-1

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]


        def dfs(y, x, idx):
            if idx == len(word):
                return True
            for move in moves:
                moved_y, moved_x = y+move[0], x+move[1]
                if max_y >= moved_y  and moved_y >= 0 and max_x >= moved_x and moved_x >= 0:
                    if board[moved_y][moved_x] == word[idx] and not visited[moved_y][moved_x]:
                        visited[moved_y][moved_x] = True
                        if dfs(moved_y, moved_x, idx+1):
                            return True
                        visited[moved_y][moved_x] = False


        for y in range(max_y+1):
            for x in range(max_x+1):
                if board[y][x] == word[0]:
                    visited[y][x] = True
                    if dfs(y, x, 1):
                        return True
                    visited[y][x] = False
        
        return False
    
