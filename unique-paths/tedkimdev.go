// TC: O(m * n)
// SC: O(m * n)
func uniquePaths(m int, n int) int {
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	dp[m-1][n-1] = 1

	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			dp[i][j] += dp[i+1][j] + dp[i][j+1]
		}
	}

	return dp[0][0]
}
