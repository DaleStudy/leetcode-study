// TC: O(n * m)
// retrieve all elemetns, grid.length * grid[0].length
// SC: O(n * m(
// need to change all elements from 1 to 0 in the worst case
class Solution {
    int output = 0;
    public int numIslands(char[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    output += 1;
                    countIslands(i, j, grid);
                }
            }
        }
        return output;
    }

    private void countIslands(int i, int j, char[][] grid) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) return;
        if (grid[i][j] == '0') return;
        grid[i][j] = '0';
        countIslands(i+1, j, grid);
        countIslands(i-1, j, grid);
        countIslands(i, j+1, grid);
        countIslands(i, j-1, grid);
    }
}
