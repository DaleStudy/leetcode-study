// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import (
	"testing"
)

func Test(t *testing.T) {
	result1 := climbStairs(2)

	if result1 != 2 {
		t.Fatal("failed test1")
	}

	result2 := climbStairs(3)

	if result2 != 3 {
		t.Fatal("failed test2")
	}
}

func climbStairs(n int) int {
	
	if n == 1 {
		return 1
	}

	if n == 2 {
		return 2
	}
	dp := make([]int, n+1)

	dp[1] = 1
	dp[2] = 2

	for i := 3; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}

	return dp[n]
}
