func containsDuplicate(nums []int) bool {
	appeared := make(map[int]bool, len(nums))

	for _, num := range nums {
		if _, found := appeared[num]; found {
			return true
		}
		appeared[num] = true
	}

	return false
}