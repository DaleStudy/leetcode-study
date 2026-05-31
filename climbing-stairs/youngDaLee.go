package youngDaLee

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}

	dp := make([]int, n+1)
	dp[1] = 1
	dp[2] = 2

	for i := 3; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n]
}

/*
Limit Exceeded
func climbStairs(n int) int {
	return dfs(0, n)
}

func dfs(now, n int) int {
	if now > n {
		return 0
	}
	if now == n {
		return 1
	}

	return dfs(now+1, n) + dfs(now+2, n)
}
*/
