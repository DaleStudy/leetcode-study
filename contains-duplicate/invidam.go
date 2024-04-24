func containsDuplicate(nums []int) bool {
	appeared := make(map[int]bool)

	for _, num := range nums {
		if appeared[num] {
			return true
		}
		appeared[num] = true
	}
}
