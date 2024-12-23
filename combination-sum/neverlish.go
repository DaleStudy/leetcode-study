// 시간복잡도: O(n^2)
// 공간복잡도: O(n^2)

package main

import "testing"

func TestCombinationSum(t *testing.T) {
	result1 := combinationSum([]int{2, 3, 6, 7}, 7)

	if len(result1) != 2 {
		t.Errorf("Expected 2, got %d", len(result1))
	}

	if len(result1[0]) != 3 && len(result1[1]) != 1 {
		t.Errorf("Expected [[7], [2, 2, 3]], got %v", result1)
	}

	result2 := combinationSum([]int{2, 3, 5}, 8)

	if len(result2) != 3 {
		t.Errorf("Expected 3, got %d", len(result2))
	}

	if len(result2[0]) != 2 && len(result2[1]) != 3 && len(result2[2]) != 3 {
		t.Errorf("Expected [[2, 2, 2, 2], [2, 3, 3], [3, 5]], got %v", result2)
	}
}

func combinationSum(candidates []int, target int) [][]int {
	dp := make([][][]int, target+1)

	dp[0] = [][]int{{}}

	for _, candidate := range candidates {
		for i := candidate; i <= target; i++ {
			for _, combination := range dp[i-candidate] {
				newCombination := append([]int{candidate}, combination...)
				dp[i] = append(dp[i], newCombination)
			}
		}
	}

	return dp[target]
}
