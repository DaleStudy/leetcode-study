class Solution {

    public int numIslands(char[][] grid) {
        /**
        1.prob:섬 개수 구하기
        2.constraints: 
        - 원소값 0 or 1
        - m,n 길이는 최소 = 1, 최대 = 300
        3.solution: dfs
         */

        //m: 세로, n: 가로 길이
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1' && grid[i][j] != '#') {
                    dfs(i, j, grid, m, n);
                    count += 1;
                }
            }
        }
        return count;
    }
     void dfs(int i, int j, char[][] grid, int m, int n) {
            if(i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') {
                return;
            }
            //이미 visited
            if(grid[i][j] == '#') {
                return;
            }
            //방문 체크
            grid[i][j] = '#';

            dfs(i+1, j, grid, m, n);
            dfs(i-1, j, grid, m, n);
            dfs(i, j+1, grid, m, n);
            dfs(i, j-1, grid, m, n);
        }
}
