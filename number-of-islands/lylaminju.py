'''
시간 복잡도: O(m * n)
- 각 셀을 한 번씩 방문하며, DFS를 통해 연결된 모든 셀을 확인하므로 grid의 모든 셀에 대해 O(1) 작업이 수행됩니다.

공간 복잡도: O(m * n)
- 최악의 경우, DFS의 호출 스택이 격자의 모든 셀에 대해 쌓일 수 있습니다. 이 경우 스택에 저장되는 셀의 개수는 최대 m * n 입니다.
'''

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])

        def exploreIsland(row: int, col: int):
            withinBounds = (0 <= row < m) and (0 <= col < n)
            if not withinBounds or grid[row][col] != "1":
                return

            grid[row][col] = "#"
            
            exploreIsland(row + 1, col)
            exploreIsland(row - 1, col)
            exploreIsland(row, col + 1)
            exploreIsland(row, col - 1)

        # Iterate through all cells in the grid
        for i in range(m):
            for j in range(n):
                # if a cell is "1", increment count and mark the whole island as "#"
                if grid[i][j] == "1":
                    count += 1
                    exploreIsland(i, j)
        
        return count
