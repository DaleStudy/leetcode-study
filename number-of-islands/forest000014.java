/*
# Time Complexity: O(m * n)
모든 격자를 최대 2번씩(2중 for loop, dfs 호출) 방문

# Space Complexity: O(m * n)
최악의 경우, 모든 격자가 '1'인 경우에 m * n회 dfs() 재귀 호출이 이뤄진다. 각 콜 스택에서의 파라미터와 지역변수가 상수개 필요하므로, O(m * n)
*/
class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != '1') {
                    continue;
                }
                dfs(grid, i, j, dr, dc);
                ans++;
            }
        }
        return ans;
    }

    private void dfs(char[][] grid, int r, int c, int[] dr, int[] dc) {
        grid[r][c] = '2'; // mark as visited

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length
                    || grid[nr][nc] != '1') {
                continue;
            }
            dfs(grid, nr, nc, dr, dc);
        }
    }
}
