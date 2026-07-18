# TC : O(m * n * 4^L)
# SC : O(m * n + L)

class Solution:
    answer = False
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for yy in range(len(board)):
            for xx in range(len(board[0])):
                if board[yy][xx] == word[0]:
                    self.visited = [ [False] * len(board[0]) for _ in range(len(board))]
                    self.visited[yy][xx] = True
                    self.dfs(board, word, xx, yy, 0)
                    

        return self.answer

    def dfs(self, board, word, cx, cy, idx):
        print(cx, cy, idx)
        if idx == len(word) - 1:
            self.answer = True

        for i in range(4):
            nx = cx + self.dx[i]
            ny = cy + self.dy[i]

            if 0 <= nx and nx < len(board[0]):
                if 0 <= ny and ny < len(board):
                    if self.visited[ny][nx] == False:
                        if idx + 1 <= len(word) - 1 and word[idx+1] == board[ny][nx]:
                            self.visited[ny][nx] = True
                            self.dfs(board, word, nx, ny, idx + 1)
                            self.visited[ny][nx] = False


# ---

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        x_len , y_len = len(board[0]) , len(board)

        visited = [[False] * x_len for _ in range(y_len)]

        def go(xx: int, yy: int, pos: int) -> bool:
            
            if pos >= len(word) - 1:
                return True
            
            for d in range(4):
                nx = xx + dx[d]
                ny = yy + dy[d]

                if 0 <= nx and nx < x_len and 0 <= ny and ny < y_len:
                    if not visited[ny][nx] and board[ny][nx] == word[pos + 1]:
                        visited[ny][nx] = True
                        if go(nx,ny,pos+1):
                            return True
                        visited[ny][nx] = False
            return False

        for y in range(y_len):
            for x in range(x_len):
                if board[y][x] == word[0]:
                    visited[y][x] = True
                    if go(x,y,0):
                        return True
                    visited[y][x] = False
            
        return False
