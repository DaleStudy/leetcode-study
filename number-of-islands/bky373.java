/*
 * time: O(M * N)
 * - M is the number of rows
 * - N is the number of columns
 * space: O(min(M, N))
 * - M is the number of rows
 * - N is the number of columns
 * in worst case where the grid is filled with lands, the size of queue can grow up to min(𝑀,𝑁).
 */
class Solution {

    private char[][] grid;

    public int numIslands(char[][] grid) {
        this.grid = grid;
        int numOfIslands = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    numOfIslands++;
                    bfs(i, j);
                }
            }
        }
        return numOfIslands;
    }

    private void bfs(int i, int j) {
        Queue<Integer> que = new LinkedList<>();
        que.add(i);
        que.add(j);
        grid[i][j] = 0;

        int[] yDir = {0, -1, 0, 1};
        int[] xDir = {1, 0, -1, 0};

        while (!que.isEmpty()) {
            int y = que.poll();
            int x = que.poll();

            for (int d = 0; d < 4; d++) {
                int ny = y + yDir[d];
                int nx = x + xDir[d];

                if (ny < 0 || ny >= grid.length || nx < 0 || nx >= grid[0].length) {
                    continue;
                }

                if (grid[ny][nx] == '1') {
                    grid[ny][nx] = '0';
                    que.add(ny);
                    que.add(nx);
                }
            }
        }
    }
}
