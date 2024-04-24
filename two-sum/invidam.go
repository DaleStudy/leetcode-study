func twoSum(nums []int, target int) []int {
	need := make(map[int]int, len(nums))
	for i, n := range nums {
		if j, ok := need[n]; ok {
			return []int{i, j}
		}
		need[target-n] = i
	}
	return nil
}
