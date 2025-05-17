'''
문제 의도: 
2차원 grid에서 '1'로 연결된 부분의 개수를 세는 문제임
'1'이 상하좌우로 연결되어 있으면 같은 섬임
'0'은 바다임

해결 방법: 
모든 칸을 하나씩 확인하면서, '1'을 만나면 섬 개수를 1 증가시키고,
그 섬에 속한 모든 '1'을 '0'으로 바꿔줌(방문 표시).
이때 DFS(깊이 우선 탐색)로 연결된 섬을 모두 방문함.

시간 복잡도: O(m × n)
    모든 칸을 한 번씩만 방문함
공간 복잡도: O(m × n) (최악의 경우 재귀 호출 스택)
    땅이 모두 연결되어 있으면 재귀 깊이가 m×n까지 갈 수 있음
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid가 비어있으면 섬이 없으니 0 반환
        if not grid:
            return 0

        # 행과 열의 개수 저장
        rows = len(grid)
        cols = len(grid[0])

        # 섬의 개수 세는 변수
        count = 0

        # (x,y) 위치에서 상하좌우로 연결된 모든 섬을 방문하는 함수
        def dfs(x, y):
            # 범위를 벗어나거나, 이미 방문했거나, 바다면 함수 종료
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == "0":
                return
            grid[x][y] = "0"  # 방문 표시(섬을 물로 바꿔서 중복 방문 방지)
            
            # 상하좌우로 이동하며 연결된 섬을 모두 방문
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        # 모든 칸을 하나씩 확인 
        for i in range(rows):
            for j in range(cols):

                # 새로운 섬 발견하면 count 1 증가, 깊이우선탐색으로 연결된 섬 모두 방문
                if grid[i][j] == "1":  
                    count += 1
                    dfs(i, j)  
        # 섬의 개수 반환
        return count



