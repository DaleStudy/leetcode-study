package week01

func containsDuplicate(nums []int) bool {
	dup := make(map[int]bool, 0)
	for _, n := range nums {
		if _, ok := dup[n]; !ok {
			dup[n] = true
		} else {
			return true
		}
	}

	return false
}
