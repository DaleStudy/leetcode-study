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
