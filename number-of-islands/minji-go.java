/**
 * <a href="https://leetcode.com/problems/number-of-islands/">week07-3. number-of-islands</a>
 * <li>Description: return the number of islands is surrounded by water("0")        </li>
 * <li>Topics: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix  </li>
 * <li>Time Complexity: O(M×N), Runtime 5ms     </li>
 * <li>Space Complexity: O(M×N), Memory 52.11MB </li>
 */
class Solution {
    private char[][] grid;
    private int m;
    private int n;
    private boolean[][] visit;
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int numIslands(char[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        this.visit = new boolean[m][n];

        int num = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1' && !visit[r][c]) {
                    findIsland(r, c);
                    num++;
                }
            }
        }
        return num;
    }

    public void findIsland(int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        visit[r][c] = true;
        queue.offer(new int[]{r, c});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cr = cur[0];
            int cc = cur[1];

            for (int[] dir : directions) {
                int nr = cr + dir[0];
                int nc = cc + dir[1];
                if (nr < 0 || nr > m - 1 || nc < 0 || nc > n - 1) {
                    continue;
                }
                if (grid[nr][nc] == '1' && !visit[nr][nc]) {
                    visit[nr][nc] = true;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }

}
