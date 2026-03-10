// TC: O(n)
// SC: O(n)
func productExceptSelf(nums []int) []int {
	result := make([]int, 0)

	left := make([]int, len(nums))
	left[0] = 1

	right := make([]int, len(nums))
	right[len(nums)-1] = 1

	for i := 1; i < len(nums); i++ {
		left[i] = nums[i-1] * left[i-1]
	}

	for i := len(nums) - 2; i >= 0; i-- {
		right[i] = nums[i+1] * right[i+1]
	}

	for i := 0; i < len(nums); i++ {
		result = append(result, left[i]*right[i])
	}
	return result
}
