/*
Time Complexity: O(m * n)
Space Complexity: O(n)
*/
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }

        for (int i = 1; i < m; i++) {
            int prev = dp[0];
            for (int j = 1; j < n; j++) {
                dp[j] += prev;
                prev = dp[j];
            }
        }

        return dp[n - 1];
    }
}
