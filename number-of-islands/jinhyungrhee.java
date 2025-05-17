class Solution {

    public int numIslands(char[][] grid) {

        int[][] dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if ('1' == grid[i][j] && !visited[i][j]) {
                    dfs(grid, visited, dir , i, j);
                    count++;
                }
            }
        }
        return count;
    }

    public void dfs(char[][] grid, boolean[][] visited, int[][] dir, int x, int y) {

        if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length
                && !visited[x][y] && '1' == grid[x][y]) {

            visited[x][y] = true;
            for (int i = 0; i < 4; i++) {
                int dx = x + dir[i][0];
                int dy = y + dir[i][1];
                dfs(grid, visited, dir ,dx, dy);
            }
        }
    }
}
