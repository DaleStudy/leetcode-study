package youngDaLee

func containsDuplicate(nums []int) bool {
	numMap := make(map[int]bool)
	for _, num := range nums {
		if _, exists := numMap[num]; exists {
			return true
		}
		numMap[num] = true
	}
	return false
}
