// Time complexity: O(n)
// Space complexity: O(n)
func containsDuplicate(nums []int) bool {
	seen := map[int]struct{}{}

	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		}
		seen[num] = struct{}{}
	}
	return false
}
