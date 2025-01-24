"""
Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

Time Complexity: O(m * n)
- 모든 셀을 한 번씩 방문
- 여기서 m은 행, n은 열을 의미함

Space Complexity: O(m * n)
- 최악의 경우(모든 셀이 '1'일 때) m * n 만큼의 재귀 호출 스택 사용

풀이 방법:
1. 2중 for문으로 그리드의 모든 셀을 순회
2. '1'을 발견하면 DFS로 연결된 모든 땅을 방문하고 '0'으로 표시
3. '1'을 발견할 때마다 islands 카운트를 1씩 증가
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.visit_island(grid, i, j)
                    islands += 1
        return islands
    
    def visit_island(self, grid, i, j):
        if (i < 0 or i >= len(grid) or 
            j < 0 or j >= len(grid[0]) or 
            grid[i][j] != '1'):
            return
        
        grid[i][j] = '0'
        
        self.visit_island(grid, i+1, j)  # 위
        self.visit_island(grid, i-1, j)  # 아래
        self.visit_island(grid, i, j+1)  # 오른쪽
        self.visit_island(grid, i, j-1)  # 왼쪽
