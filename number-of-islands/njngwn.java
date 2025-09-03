// Time Complexity: O(m*n), m: number of row, n: number of column
// Space Complexity: O(m*n), m: number of row, n: number of column, because of call stack
class Solution {
    void findLand(char[][] grid, int row, int col) {
        if (row < 0 || row > grid.length-1 || col < 0 || col > grid[0].length-1) return;
        if (grid[row][col] == '0') return;

        grid[row][col] = '0';   // make element '0'(water)

        findLand(grid, row-1, col);
        findLand(grid, row+1, col);
        findLand(grid, row, col-1);
        findLand(grid, row, col+1);
    }

    public int numIslands(char[][] grid) {
        int num = 0;

        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[0].length; ++j) {
                if (grid[i][j] == '1') {
                    findLand(grid, i, j);
                    num++;
                }
            }
        }

        return num;
    }
}