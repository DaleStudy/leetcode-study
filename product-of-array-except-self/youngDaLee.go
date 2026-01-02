package youngDaLee

func productExceptSelf(nums []int) []int {
	n := len(nums)
	result := make([]int, n)

	// Calculate left products
	leftProduct := 1
	for i := 0; i < n; i++ {
		result[i] = leftProduct
		leftProduct *= nums[i]
	}

	// Calculate right products and combine with left products
	rightProduct := 1
	for i := n - 1; i >= 0; i-- {
		result[i] *= rightProduct
		rightProduct *= nums[i]
	}
	return result
}
