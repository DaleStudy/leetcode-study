func twoSum(nums []int, target int) []int {
	for i, ni := range nums {
		for j, nj := range nums {
			if i != j && ni+nj == target {
				return []int{i, j}
			}
		}
	}

	return nil
}
