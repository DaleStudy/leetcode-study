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
1. numIslands 메서드: 그리드를 순회하며 '1'을 찾고 섬의 개수를 세는 역할
2. visit_island 메서드: 하나의 섬을 완전히 탐색하고 방문한 땅을 '0'으로 바꾸는 역할
3. 두 함수가 작동하는 방식:
- numIslands는 섬의 시작점('1')을 찾아 카운트를 증가시킴
- visit_island는 찾은 섬을 완전히 탐색하고 방문 표시('0'으로 변경)
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
        # base case: 위치가 범위를 벗어나거나 '1'이 아니면 함수를 종료
        if (i < 0 or i >= len(grid) or 
            j < 0 or j >= len(grid[0]) or 
            grid[i][j] != '1'):
            return
        
        # 방문한 땅을 '0'으로 표시하여 다시 방문하지 않도록 함
        grid[i][j] = '0'
        
        # 네 방향(아래, 위, 오른쪽, 왼쪽)으로 DFS 재귀 호출
        self.visit_island(grid, i+1, j)  # 아래
        self.visit_island(grid, i-1, j)  # 위
        self.visit_island(grid, i, j+1)  # 오른쪽
        self.visit_island(grid, i, j-1)  # 왼쪽
