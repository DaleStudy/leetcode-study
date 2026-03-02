// Time complexity: O(n)
// Space complexity: O(n)
func longestConsecutive(nums []int) int {
	if len(nums) == 0 || len(nums) == 1 {
		return len(nums)
	}

	numSet := map[int]struct{}{}
	for _, num := range nums {
		numSet[num] = struct{}{}
	}

	longest := 1
	for num := range numSet {
		if _, ok := numSet[num-1]; ok {
			length := 0
			for {
				if _, ok := numSet[num+length]; ok {
					length++
				} else {
					break
				}
			}
			longest = Max(length+1, longest)
		}
	}

	return longest
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}