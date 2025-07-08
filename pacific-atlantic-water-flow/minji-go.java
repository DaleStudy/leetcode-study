/**
 * <a href="https://leetcode.com/problems/pacific-atlantic-water-flow/">week9-2. pacific-atlantic-water-flow</a>
 * <li>Description: Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. </li>
 * <li>Topics: Array, Depth-First Search, Breadth-First Search, Matrix</li>
 * <li>Time Complexity: O(MN), Runtime 9ms   </li>
 * <li>Space Complexity: O(MN), Memory 45.18MB</li>
 */
class Solution {
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;

        Queue<int[]> pacificQueue = new LinkedList<>();
        boolean[][] pacific = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            pacific[i][0] = true;
            pacificQueue.offer(new int[]{i, 0});
        }
        for (int i = 0; i < n; i++) {
            pacific[0][i] = true;
            pacificQueue.offer(new int[]{0, i});
        }
        bfs(heights, pacificQueue, pacific);

        Queue<int[]> atlanticQueue = new LinkedList<>();
        boolean[][] atlantic = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            atlantic[i][n - 1] = true;
            atlanticQueue.offer(new int[]{i, n - 1});
        }
        for (int i = 0; i < n; i++) {
            atlantic[m - 1][i] = true;
            atlanticQueue.offer(new int[]{m - 1, i});
        }
        bfs(heights, atlanticQueue, atlantic);

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(List.of(i, j));
                }
            }
        }
        return result;
    }


    private void bfs(int[][] heights, Queue<int[]> queue, boolean[][] visit) {
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int cr = curr[0];
            int cc = curr[1];

            for (int[] dir : directions) {
                int nr = cr + dir[0];
                int nc = cc + dir[1];

                if (nr < 0 || nr > heights.length - 1 || nc < 0 || nc > heights[0].length - 1 || visit[nr][nc]) {
                    continue;
                }
                if (heights[nr][nc] >= heights[cr][cc]) {
                    visit[nr][nc] = true;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }
}
