# TC:O(n * m), SC:O(n * m)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        def dfs(r: int, c: int) :
            grid[r][c] = "0"
            for y, x in [(r, c + 1), (r + 1, c), (r - 1, c), (r, c - 1)]: # 현재 r,c 좌표에 대해 상하좌우 탐색
                if 0 <= y < row and 0 <= x < col:
                    if grid[y][x] == "1":
                        dfs(y, x)
            return

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1": #땅 발견 시 cnt 증가하고, 발견된 땅과 연결된 땅들을 제거
                    cnt += 1    
                    dfs(r, c)
        return cnt
