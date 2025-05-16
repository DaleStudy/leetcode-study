"""
    풀이 : 
        전체 매트릭스를 순회하면서 visited set에 없는 땅('1')을 만나면 
        dfs 함수를 통해 이어진 땅을 전부 visited에 넣고 섬 cnt += 1
    
    matrix의 크기 m * n

    TC : O(M * N)
        전체 매트릭스를 순회하므로

    SC : O(M * N)
        set의 크기 및 dfs 호출 스택은 전체 매트릭스 크기에 비례하므로

    - 주어진 grid를 직접 변경해도 되면 set를 활용하지 않고 직접 값을 바꿔서 visited를 표현할 수도 있다
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = set()
        def dfs(i : int, j : int) :
            if i < 0 or i == n_rows or j < 0 or j == n_cols:
                return
            if (i, j) in visited or grid[i][j] == '0':
                return
            if grid[i][j] == '1' :
                visited.add((i,j))
            for r, c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                dfs(r, c)

        cnt = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if not (i, j) in visited and grid[i][j] == '1':
                    dfs(i, j)
                    cnt +=1
        return cnt
