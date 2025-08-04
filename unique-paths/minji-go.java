/**
 * <a href="https://leetcode.com/problems/unique-paths/">week07-4. unique-paths</a>
 * <li>Description: return the number of possible unique paths to reach the bottom-right corner</li>
 * <li>Topics: Math, Dynamic Programming, Combinatorics </li>
 * <li>Time Complexity: O(M×N), Runtime 2ms             </li>
 * <li>Space Complexity: O(M×N), Memory 40.76MB         </li>
 */
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dirs = {{1, 0}, {0, 1}};
        int[][] dp = new int[m][n];
        dp[0][0] = 1;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cr = cur[0];
            int cc = cur[1];

            for (int i = 0; i < 2; i++) {
                int nr = cr + dirs[i][0];
                int nc = cc + dirs[i][1];

                if (nr > m - 1 || nc > n - 1) {
                    continue;
                }

                if (dp[nr][nc] == 0) {
                    queue.add(new int[]{nr, nc});
                }
                dp[nr][nc] += dp[cr][cc];
            }
        }

        return dp[m - 1][n - 1];
    }
}
