// Time complexity: O(n)
// Space complexity: O(1)
func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}

	prevTwo := nums[0]
	prevOne := Max(nums[0], nums[1])

	for i := 2; i < len(nums); i++ {
		// take
		m1 := prevTwo + nums[i]
		// skip
		m2 := prevOne

		currentMax := Max(m1, m2)
		prevTwo = prevOne
		prevOne = Max(currentMax, prevOne)
	}

	return prevOne
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}