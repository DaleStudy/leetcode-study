/**
 * TC : O(m * n)
 * - 그리드 원소 갯수 m * n 만큼 순회하므로
 * SC : O(m * n)
 * - 그리드 원소 갯수 m * n 만큼 재귀 호출이 발생할 수 있으므로
 */
class Solution {
    char[][] grid;
    int rLen = 0;
    int cLen = 0;

    public int numIslands(char[][] grid) {
        this.grid = grid;
        this.rLen = grid.length;
        this.cLen = grid[0].length;
        int count = 0;

        for(int row=0; row<rLen;row++) {
            for(int col=0; col<cLen; col++) {
                if(grid[row][col] == '1') {
                    count++;
                    cover(row, col);
                }
            }
        }

        return count;
    }

    void cover(int row, int col) {
        if(row < 0 || col < 0 || row >= this.rLen || col >= this.cLen || this.grid[row][col] != '1') {
            return;
        }

        this.grid[row][col] = '2';

        // 좌우상하 다 처리
        cover(row + 1, col);
        cover(row - 1, col);
        cover(row, col + 1);
        cover(row, col - 1);
    }
} 
