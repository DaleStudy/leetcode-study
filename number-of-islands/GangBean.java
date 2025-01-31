class Solution {
    /**
    1. understanding
    - for each grid cell, if it is land, then move horizontally and vertically, to find connecting lands
    2. complexity
    - time: O(N * M) where grid is N * M matrix
    - space: O(1)
     */
    public int numIslands(char[][] grid) {
        int ret = 0;
        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    findIsland(grid,i,j,'.');
                    ret++;
                }
            }
        }
        return ret;
    }

    private void findIsland(char[][] grid, int i, int j, char color) {
        if (grid[i][j] == '1') {
            grid[i][j] = color;
        }
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};

        for (int dir=0; dir<4; dir++) {
            int nx = i + dx[dir];
            int ny = j + dy[dir];
            if (0<= nx&&nx<grid.length && 0<=ny&&ny<grid[0].length && grid[nx][ny]=='1') {
                findIsland(grid,nx,ny,color);
            }
        }
    }
}

