// TC: O(n ^ 2)
// SC: O(n)
func lengthOfLIS(nums []int) int {
	dp := make([]int, len(nums))

	for i := range dp {
		dp[i] = 1
	}

	for i := len(nums) - 2; i >= 0; i-- {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] < nums[j] {
				if dp[i] < 1+dp[j] {
					dp[i] = 1 + dp[j]
				}
			}
		}
	}

	maxLength := 1
	for _, length := range dp {
		maxLength = max(maxLength, length)
	}
	return maxLength
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
