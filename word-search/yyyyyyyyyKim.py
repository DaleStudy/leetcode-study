class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # 백트래킹, DFS, 재귀
        def dfs(x, y, idx):
            # 모든 글자를 다 찾았다면 True 리턴해서 종료
            if idx == len(word):
                return True

            # 범위벗어나거나, 다른글자라면 False 리턴해서 종료(pruning가지치기)
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[idx]:
                return False

            t = board[x][y]     # 현재값 t에 임시저장
            board[x][y] = ' '   # 방문표시

            # 모든 방향(상하좌우) 탐색
            for i, j in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(x+i, y+j, idx+1):
                    return True

            board[x][y] = t # 방문복원
            
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False