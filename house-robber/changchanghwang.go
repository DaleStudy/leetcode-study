// time complexity: O(n)
// space complexity: O(1)
func rob(nums []int) int {
	prev := 0
	curr := 0

	for _, num := range nums {
		temp := curr
		curr = max(prev+num, curr)
		prev = temp
	}

	return curr
}
