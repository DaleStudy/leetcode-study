// Time complexity, O(n)
// Space complexity, O(n)
func containsDuplicate(nums []int) bool {
	hashMap := map[int]bool{}
	for _, num := range nums {
		if hashMap[num] {
			return true
		} else {
			hashMap[num] = true
		}
	}
	return false
}