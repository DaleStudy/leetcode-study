// 시간복잡도: O(n)
// 공간복잡도: O(n)

package main

import "testing"

func TestMaxSubArray(t *testing.T) {
	result1 := maxSubArray([]int{-2,1,-3,4,-1,2,1,-5,4})

	if result1 != 6 {
		t.Errorf("Expected 6, got %d", result1)
	}

	result2 := maxSubArray([]int{1})

	if result2 != 1 {
		t.Errorf("Expected 1, got %d", result2)
	}

	result3 := maxSubArray([]int{5,4,-1,7,8})

	if result3 != 23 {
		t.Errorf("Expected 23, got %d", result3)
	}
}

func max(nums ...int) int {
	result := nums[0]

	for _, num := range nums[1:] {
		if num > result {
			result = num
		}
	}

	return result
}

func maxSubArray(nums []int) int {
	dp := make([]int, len(nums))

	dp[0] = nums[0]

	for index, num := range nums[1:] {
		dp[index+1] = max(0, dp[index]) + num
		
	}

	return max(dp...)
}
