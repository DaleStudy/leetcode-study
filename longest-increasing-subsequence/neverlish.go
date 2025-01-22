// 시간복잡도: O(n^2)
// 공간복잡도: O(n)

package main

import "testing"

func TestLengthOfLIS(t *testing.T) {
	result1 := lengthOfLIS([]int{10, 9, 2, 5, 3, 7, 101, 18})

	if result1 != 4 {
		t.Errorf("Expected 4, but got %v", result1)
	}

	result2 := lengthOfLIS([]int{0, 1, 0, 3, 2, 3})

	if result2 != 4 {
		t.Errorf("Expected 4, but got %v", result2)
	}

	result3 := lengthOfLIS([]int{7, 7, 7, 7, 7, 7, 7})

	if result3 != 1 {
		t.Errorf("Expected 1, but got %v", result3)
	}
}

func lengthOfLIS(nums []int) int {
	result := 0

	dp := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		dp[i] = 1

		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}

		result = max(result, dp[i])
	}

	return result

}
