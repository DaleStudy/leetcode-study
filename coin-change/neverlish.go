// 시간복잡도: O(n*m)
// 공간복잡도: O(n*m)

package main

import "testing"

func TestCoinChange(t *testing.T) {
	result1 := coinChange([]int{1, 2, 5}, 11)
	if result1 != 3 {
		t.Errorf("Expected 3 but got %d", result1)
	}

	result2 := coinChange([]int{2}, 3)

	if result2 != -1 {
		t.Errorf("Expected -1 but got %d", result2)
	}

	result3 := coinChange([]int{1}, 0)

	if result3 != 0 {
		t.Errorf("Expected 0 but got %d", result3)
	}
}

func coinChange(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}

	dp := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		dp[i] = amount + 1
	}

	for i := 1; i <= amount; i++ {
		for _, coin := range coins {
			if coin <= i {
				dp[i] = min(dp[i], dp[i-coin]+1)
			}
		}
	}

	if dp[amount] > amount {
		return -1
	}

	return dp[amount]
}
